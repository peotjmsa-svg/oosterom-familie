"""Open Archieven search limited to one archive and a period. Usage: python scripts/oa_arch.py ARCHIVE "Naam" VAN-TOT [-doop]
Example: oa_arch.py rel Oostrum 1580-1700   (rel = RHC Rijnstreek en Lopikerwaard, hua = Het Utrechts Archief)."""
import sys, json, subprocess, urllib.parse
sys.stdout.reconfigure(encoding="utf-8")
arch, name, per = sys.argv[1], sys.argv[2], sys.argv[3]
nodoop = "-doop" in sys.argv
seen = set()
for start in range(0, 3000, 100):
    u = "https://api.openarch.nl/1.0/records/search.json?" + urllib.parse.urlencode(
        {"name": f"{name} {per}", "archive": arch, "lang": "nl", "number_show": 100, "start": start, "sort": 1})
    d = json.loads(subprocess.run(["curl", "-s", "-A", "oosterom-familie research", u], capture_output=True).stdout.decode("utf-8", "replace"))
    docs = d["response"].get("docs", [])
    for r in docs:
        if nodoop and r.get("eventtype") == "Doop": continue
        k = (r["identifier"], r.get("personname"))
        if k in seen: continue
        seen.add(k); e = r.get("eventdate") or {}
        print(f"{e.get('year','')}-{e.get('month','')}-{e.get('day','')} | {r.get('eventtype')} | {r.get('personname')} | {r.get('relationtype')} | {','.join(r.get('eventplace') or [])} | {arch}:{r['identifier']}")
    if len(docs) < 100: break
