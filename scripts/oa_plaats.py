"""All Open Archieven records of a surname in one place. Usage: python scripts/oa_plaats.py Naam Plaats [van-tot] [-doop]
-doop hides baptisms. Output sorted by date."""
import sys, json, subprocess, urllib.parse
sys.stdout.reconfigure(encoding="utf-8")
name, place = sys.argv[1], sys.argv[2]
rng = next((a for a in sys.argv[3:] if "-" in a and a[0].isdigit()), "0-9999")
lo, hi = map(int, rng.split("-"))
nodoop = "-doop" in sys.argv
rows, seen = [], set()
for start in range(0, 2000, 100):
    u = "https://api.openarch.nl/1.0/records/search.json?" + urllib.parse.urlencode(
        {"name": name, "eventplace": place, "lang": "nl", "number_show": 100, "start": start})
    d = json.loads(subprocess.run(["curl", "-s", "-A", "oosterom-familie research", u], capture_output=True).stdout.decode("utf-8", "replace"))
    docs = d["response"].get("docs", [])
    for r in docs:
        if r.get("archive_code") == "rel":
            continue
        e = r.get("eventdate") or {}
        y = int(e.get("year") or 0)
        if not lo <= y <= hi or (nodoop and r.get("eventtype") == "Doop"):
            continue
        k = (r.get("identifier"), r.get("personname"))
        if k in seen:
            continue
        seen.add(k)
        rows.append((y, int(e.get("month") or 0), int(e.get("day") or 0), r.get("eventtype"), r.get("personname"),
                     r.get("relationtype"), r.get("archive_code") + ":" + r.get("identifier")))
    if len(docs) < 100:
        break
for y, m, dd, t, n, rel, i in sorted(rows):
    print(f"{dd}-{m}-{y} | {t} | {n} ({rel}) | {i}")
