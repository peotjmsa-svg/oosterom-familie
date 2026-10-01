"""Contact sheet of consecutive proxy.archieven.nl scan pages, to find the right page of a register.
Usage: python scripts/scan_sheet.py OUTNAME GUID_HEX_START(12 chars) COUNT [suffix]"""
import sys, subprocess
from PIL import Image, ImageDraw
out, start, n = sys.argv[1], int(sys.argv[2], 16), int(sys.argv[3])
suf = sys.argv[4] if len(sys.argv) > 4 else "4642E0534701000A17FD"
ims = []
for k in range(n):
    g = f"{start + k:X}{suf}"
    p = f"raw/scans/_th{k}.jpg"
    subprocess.run(["curl", "-sL", "-A", "oosterom-familie research", "-o", p, f"https://proxy.archieven.nl/thumb/39/{g}"])
    try:
        im = Image.open(p).convert("RGB"); ImageDraw.Draw(im).text((5, 5), str(k), fill="red"); ims.append(im)
    except Exception:
        print(k, "fail")
w = max(i.width for i in ims); h = max(i.height for i in ims)
sheet = Image.new("RGB", (w * 6, h * ((len(ims) + 5) // 6)), "white")
for k, i in enumerate(ims):
    sheet.paste(i, ((k % 6) * w, (k // 6) * h))
sheet.save(f"raw/scans/{out}.jpg"); print(sheet.size)
