"""Search all of Het Utrechts Archief for a term in the debug Chrome and open one result category.
Usage: python scripts/hua_click.py TERM "Category text" OUT.txt"""
import sys, time, urllib.parse
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
term, cat, out = sys.argv[1], sys.argv[2], sys.argv[3]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg = b.contexts[0].new_page()
    pg.goto("https://hetutrechtsarchief.nl/onderzoek/resultaten/archieven?mivast=39&mizig=0&miadt=39&milang=nl&mizk_alle="
            + urllib.parse.quote(term), wait_until="domcontentloaded"); time.sleep(5)
    pg.get_by_text(cat, exact=True).first.click(); time.sleep(6)
    t = pg.inner_text("body")
    open(out, "w", encoding="utf-8").write(pg.url + "\n" + t)
    i = t.find("resultaten")
    print(pg.url); print(t[max(0, i - 200):i + 6000])
    pg.close()
