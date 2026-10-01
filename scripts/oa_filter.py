"""Open Archieven search with filters. Usage: python scripts/oa_filter.py "naam" [type] [van-tot] [plaatsdeel]
type e.g. Begrafenis, Doop, Trouwen, 'Notariële'; range e.g. 1690-1800. Pages through up to 1000 results."""
import sys, json, subprocess, urllib.parse
sys.stdout.reconfigure(encoding="utf-8")
q = sys.argv[1]; typ = sys.argv[2] if len(sys.argv) > 2 else ""; rng = sys.argv[3] if len(sys.argv) > 3 else ""
plc = sys.argv[4].lower() if len(sys.argv) > 4 else ""
lo, hi = (int(x) for x in rng.split("-")) if rng else (0, 9999)
seen = set()
for start in range(0, 1000, 100):
    u = "https://api.openarch.nl/1.0/records/search.json?" + urllib.parse.urlencode(
        {"name": q, "lang": "nl", "number_show": 100, "start": start})
    d = json.loads(subprocess.run(["curl", "-s", "-A", "oosterom-familie research", u], capture_output=True).stdout.decode("utf-8", "replace"))
    docs = d["response"].get("docs", [])
    for r in docs:
        e = r.get("eventdate") or {}; y = e.get("year") or 0
        pl = ",".join(r.get("eventplace") or [])
        if not (lo <= int(y or 0) <= hi) or (plc and plc not in pl.lower()) or (typ and typ.lower() not in str(r.get("eventtype")).lower()):
            continue
        i = r.get("url", "").split("/")[-1]
        if i in seen or i.startswith("rel:"):
            continue
        seen.add(i)
        print(f"{y}-{e.get('month','')}-{e.get('day','')} | {r.get('eventtype')} | {r.get('personname')} ({r.get('relationtype')}) | {pl} | {i}")
    if len(docs) < 100:
        break
