"""Open a page in the user's debug Chrome (port 9223), wait, save a screenshot and the image URLs on the page.
Usage: python scripts/hua_scan.py OUT.png URL"""
import sys, time
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
out, url = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    ctx = b.contexts[0]
    pg = next((x for x in ctx.pages if "hetutrechtsarchief" in x.url), None) or ctx.new_page()
    pg.goto(url, wait_until="domcontentloaded"); time.sleep(6)
    pg.screenshot(path=out)
    for s in pg.eval_on_selector_all("img", "e=>e.map(i=>i.src)"):
        if "image" in s or ".jpg" in s:
            print(s)
    print(pg.url)
