"""OCR text of Delpher articles. Usage: python scripts/delpher_text.py URN [URN ...] [--grep word]"""
import sys, subprocess, re, html
sys.stdout.reconfigure(encoding="utf-8")
args = sys.argv[1:]; g = None
if "--grep" in args: g = args[args.index("--grep") + 1]; args = args[:args.index("--grep")]
for urn in args:
    t = subprocess.run(["curl", "-s", "-L", "-m", "60", f"https://resolver.kb.nl/resolve?urn={urn}:ocr"], capture_output=True).stdout.decode("utf-8", "replace")
    t = html.unescape(re.sub(r"<[^>]+>", " ", t)); t = re.sub(r"\s+", " ", t)
    if g:
        for m in re.finditer(g, t, re.I): print(f"== {urn}: ...{t[max(0,m.start()-700):m.end()+900]}...")
    else: print(f"== {urn}\n{t[:4000]}")
