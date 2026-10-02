"""RHC Rijnstreek en Lopikerwaard scans via the debug Chrome (port 9223).
Usage: python scripts/rhc_scan.py list SCANS_URL            -> prints index:bestand_id:filename for every scan
       python scripts/rhc_scan.py get SCANS_URL OUTDIR i [i ...] [--w 2400]  -> saves scans (by list index) as jpg
       python scripts/rhc_scan.py id SCANS_URL OUTDIR bestand_id [...]   -> saves scans by bestand_id (reliable)
SCANS_URL = a detail.php?form-action=scans&... URL of one inventory number (from the archive's 'Scans' tab)."""
import sys, re, time, os, io
from playwright.sync_api import sync_playwright
from PIL import Image
args = sys.argv[1:]; mode, url = args[0], args[1]
w = 2400
if "--w" in args: w = int(args[args.index("--w") + 1]); args = args[:args.index("--w")]
with sync_playwright() as p:
    b = p.chromium.connect_over_cdp("http://127.0.0.1:9223"); ctx = b.contexts[0]; pg = ctx.new_page()
    sess = []
    pg.on("request", lambda r: sess.append(r.url) if "sessionid=" in r.url else None)
    pg.goto(url, wait_until="networkidle"); time.sleep(2)
    opts = pg.eval_on_selector_all("select.scans-select option", "e=>e.map(o=>[o.value,o.textContent])")
    ids = pg.evaluate("""() => { const m=[...document.querySelectorAll('a,option,[data-bestand]')].map(e=>e.outerHTML).join(' ');
                                 return m.match(/bestand_id=[0-9]+/g) || [] }""")
    sid = re.search(r"sessionid=(\w+)", sess[0]).group(1)
    first = int(re.search(r"QueryParams=(\d+)", sess[0]).group(1))
    if mode == "list":
        for v, t in opts: print(v, t)
        print("first bestand_id", first, "session", sid)
    elif mode == "id":
        out = args[2]; os.makedirs(out, exist_ok=True)
        for bid in args[3:]:
            r = ctx.request.get(f"https://archief.rhcrijnstreek.nl/Imageserver/afbeelding.img?sessionid={sid}&QueryParams={bid}",
                                headers={"Referer": "https://archief.rhcrijnstreek.nl/"})
            im = Image.open(io.BytesIO(r.body())).convert("L")
            im = im.resize((w, int(im.size[1] * w / im.size[0])), Image.LANCZOS)
            f = os.path.join(out, f"b{bid}.jpg"); im.save(f, quality=85); print(f)
    else:
        out = args[2]; os.makedirs(out, exist_ok=True)
        for i in map(int, args[3:]):
            n0 = len(sess)
            pg.select_option("select.scans-select", str(i))
            for _ in range(20):
                time.sleep(0.5)
                if len(sess) > n0: break
            time.sleep(1)
            q = [u for u in sess[n0:] if "QueryParams=" in u][-1] if len(sess) > n0 else sess[-1]
            bid = re.search(r"QueryParams=(\d+)", q).group(1)
            r = ctx.request.get(f"https://archief.rhcrijnstreek.nl/Imageserver/afbeelding.img?sessionid={sid}&QueryParams={bid}",
                                headers={"Referer": "https://archief.rhcrijnstreek.nl/"})
            im = Image.open(io.BytesIO(r.body())).convert("L")
            im = im.resize((w, int(im.size[1] * w / im.size[0])), Image.LANCZOS)
            f = os.path.join(out, f"s{i:04d}.jpg"); im.save(f, quality=85); print(f, bid)
    pg.close()
