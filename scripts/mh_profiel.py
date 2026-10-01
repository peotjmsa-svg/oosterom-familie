"""Read MyHeritage profile pages in the user's debug Chrome (port 9223) and save the text.
Usage: python scripts/mh_profiel.py <id> [<id> ...]   (id = number like 1500229 in the tree OYYV6RLFE43U2DPKEJO6ILZTOTT5LPI)
Output: raw/mh/<id>.txt"""
import sys, time, os
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
SITE = "OYYV6RLFE43U2DPKEJO6ILZTOTT5LPI"
os.makedirs("raw/mh", exist_ok=True)
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    ctx = b.contexts[0]
    pg = ctx.new_page()
    for i in sys.argv[1:]:
        pg.goto(f"https://www.myheritage.nl/profile-{SITE}-{i}/x", wait_until="domcontentloaded")
        time.sleep(3)
        t = pg.inner_text("body")
        open(f"raw/mh/{i}.txt", "w", encoding="utf-8").write(pg.url + "\n" + t)
        print("=====", i, pg.url, len(t))
    pg.close()
