"""Delpher newspaper search via the KB SRU endpoint. Usage: python scripts/delpher.py 'CQL query' [max]
Example: delpher.py 'Oosterom AND Polsbroek'   Prints date, paper, title and the article URL (urn)."""
import sys, subprocess, urllib.parse, re
sys.stdout.reconfigure(encoding="utf-8")
q = sys.argv[1]; n = sys.argv[2] if len(sys.argv) > 2 else "50"
u = ("https://jsru.kb.nl/sru/sru?version=1.2&operation=searchRetrieve&x-collection=DDD_artikel&recordSchema=ddd"
     f"&maximumRecords={n}&query=" + urllib.parse.quote(q))
t = subprocess.run(["curl", "-s", "-m", "60", u], capture_output=True).stdout.decode("utf-8", "replace")
print("hits:", (re.findall(r"<srw:numberOfRecords>(\d+)", t) or ["?"])[0])
for rec in re.findall(r"<srw:record>(.*?)</srw:record>", t, re.S):
    g = lambda k: (re.findall(rf"<{k}[^>]*>(.*?)</{k}>", rec, re.S) or [""])[0]
    print(g("dc:date"), "|", g("dc:publisher") or g("ddd:papertitle"), "|", g("dc:title")[:80], "|", g("ddd:metadataKey") or g("dc:identifier"))
