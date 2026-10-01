"""One short line per Open Archieven record: date, type, place, every person with role, age, occupation.
Usage: python scripts/oa_kind.py hua:ID [smh:ID ...]"""
import sys, json, subprocess, time
sys.stdout.reconfigure(encoding="utf-8")


def flat(o):
    """Strip the a2a_ prefixes and the doubled {"X": {"X": value}} wrapping."""
    if isinstance(o, list):
        return [flat(x) for x in o]
    if isinstance(o, dict):
        o = {k.replace("a2a_", ""): v for k, v in o.items()}
        if len(o) == 1 and not isinstance(list(o.values())[0], (dict, list)):
            return list(o.values())[0]
        return {k: flat(v) for k, v in o.items()}
    return o


def lst(x):
    return x if isinstance(x, list) else ([x] if x else [])


for ident in sys.argv[1:]:
    a, i = ident.split(":", 1)
    t = subprocess.run(["curl", "-s", f"https://api.openarch.nl/1.0/records/show.json?archive={a}&identifier={i}&lang=nl"],
                       capture_output=True).stdout.decode("utf-8", "replace")
    time.sleep(0.3)
    try:
        j = flat(json.loads(t))
    except Exception:
        time.sleep(2); continue
    j = j[0] if isinstance(j, list) else j
    names = {}
    for p in lst(j.get("Person")):
        n = p.get("PersonName") or {}
        nm = " ".join(str(n.get(k)) for k in ("PersonNameFirstName", "PersonNamePrefixLastName", "PersonNameLastName") if n.get(k))
        age = p.get("Age") or {}
        extra = [str(age.get("PersonAgeLiteral") or age.get("PersonAgeYears") or "")] if isinstance(age, dict) else [str(age)]
        if p.get("Profession"):
            extra.append(str(p["Profession"]))
        if p.get("Residence"):
            r = p["Residence"]
            extra.append("woont " + str(r.get("Place") if isinstance(r, dict) else r))
        extra = [e for e in extra if e and e != "{}"]
        names[p.get("pid")] = nm + (f" ({', '.join(extra)})" if extra else "")
    ev = lst(j.get("Event"))[0] if j.get("Event") else {}
    dt = ev.get("EventDate") or {}
    date = "-".join(str(dt.get(k, "")) for k in ("Day", "Month", "Year"))
    place = ev.get("EventPlace") or ""
    place = place.get("Place", "") if isinstance(place, dict) else place
    roles = [f"{r.get('RelationType')}: {names.get(r.get('PersonKeyRef'), '?')}" for r in lst(j.get("RelationEP"))]
    print(f"{date} {ev.get('EventType', '')} {place} | " + "; ".join(roles) + f" | {ident}")
