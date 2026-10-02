"""Open Archieven records of a name filtered by source type. Usage: python scripts/oa_bron.py Naam "Bronsoort" [plaats]
Example: oa_bron.py Oosterom "Memories van successie"  (sourcetype as shown in the API, e.g. Bevolkingsregister)."""
import sys, json, subprocess, urllib.parse
sys.stdout.reconfigure(encoding="utf-8")
name, st = sys.argv[1], sys.argv[2]
place = sys.argv[3] if len(sys.argv) > 3 else None
seen = set()
for start in range(0, 3000, 100):
    p = {"name": name, "lang": "nl", "number_show": 100, "start": start}
    if place: p["eventplace"] = place
    out = subprocess.run(["curl", "-s", "-A", "oosterom-familie research", "https://api.openarch.nl/1.0/records/search.json?" + urllib.parse.urlencode(p)], capture_output=True).stdout.decode("utf-8", "replace")
    try: d = json.loads(out)
    except Exception: print("ERR", out[:200]); break
    docs = d["response"].get("docs", [])
    for r in docs:
        if r.get("archive_code") == "rel" or r.get("sourcetype") != st: continue
        k = (r.get("identifier"), r.get("personname"))
        if k in seen: continue
        seen.add(k)
        e = r.get("eventdate") or {}
        print(f"{e.get('day','')}-{e.get('month','')}-{e.get('year','')} | {r.get('personname')} ({r.get('relationtype')}) | {','.join(r.get('eventplace') or [])} | {r['archive_code']}:{r['identifier']}")
    if len(docs) < 100: break
