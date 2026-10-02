"""Open a page in the user's debug Chrome (port 9223), wait, print the image URLs on the page and save a screenshot.
Usage: python scripts/hua_scan.py OUT.png URL"""
import sys, time
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
out, url = sys.argv[1], sys.argv[2]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    ctx = b.contexts[0]
    pg = next((x for x in ctx.pages if "hetutrechtsarchief" in x.url), None) or ctx.new_page()
    pg.bring_to_front()
    pg.goto(url, wait_until="domcontentloaded"); time.sleep(6)
    for s in pg.eval_on_selector_all("img", "e=>e.map(i=>i.src)"):
        if "image" in s or ".jpg" in s or "download" in s:
            print(s)
    print(pg.url)
    try: pg.screenshot(path=out, timeout=15000)
    except Exception as e: print("no screenshot:", e)
