"""Street View still in the debug Chrome (port 9223): finds the nearest panorama and saves its 900x600 thumbnail.
Usage: python scripts/streetview.py OUT_PREFIX LAT LON HEADING [HEADING ...]
Google imagery: for the user's own reference; publishing needs attribution and a check of Google's terms."""
import sys, time, re
from playwright.sync_api import sync_playwright
out, lat, lon, heads = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223")
    pg = b.contexts[0].new_page(); pg.bring_to_front()
    pg.goto(f"https://www.google.com/maps/@?api=1&map_action=pano&viewpoint={lat},{lon}&heading={heads[0]}", wait_until="domcontentloaded")
    for _ in range(8):
        time.sleep(4)
        try: pg.screenshot(timeout=10000)
        except Exception: pass
        m = re.search(r"panoid%3D([\w-]+)", pg.url)
        if m: break
    if not m: sys.exit("no panorama found: " + pg.url)
    pid = m.group(1); at = re.search(r"@([\d.]+),([\d.]+)", pg.url)
    print("pano", pid, "at", at.group(1), at.group(2) if at else "")
    for h in heads:
        pg.goto(f"https://streetviewpixels-pa.googleapis.com/v1/thumbnail?cb_client=maps_sv.tactile&w=900&h=600&pitch=0&panoid={pid}&yaw={h}")
        time.sleep(2); pg.locator("img").first.screenshot(path=f"{out}_{h}.png"); print(f"{out}_{h}.png")
    pg.close()
