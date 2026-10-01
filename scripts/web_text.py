"""Open a URL in the user's debug Chrome (port 9223) and print the page text. Usage: python scripts/web_text.py URL [OUT.txt]"""
import sys, time
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    ctx = b.contexts[0]
    pg = ctx.new_page()
    pg.goto(sys.argv[1], wait_until="domcontentloaded"); time.sleep(5)
    t = pg.inner_text("body")
    if len(sys.argv) > 2:
        open(sys.argv[2], "w", encoding="utf-8").write(pg.url + "\n" + t)
    print(t[:8000])
    pg.close()
