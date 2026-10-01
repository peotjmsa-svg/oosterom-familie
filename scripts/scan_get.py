"""Download Open Archieven scan(s) and save a reduced copy for reading. Usage: python scripts/scan_get.py NAME URL [maxpx]"""
import sys, subprocess
from PIL import Image
name, url = sys.argv[1], sys.argv[2]
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 1800
p = f"raw/scans/{name}.jpg"
subprocess.run(["curl", "-sL", "-A", "oosterom-familie research", "-o", p, url])
im = Image.open(p); print(name, im.size)
im.thumbnail((mx, mx)); im.save(f"raw/scans/{name}_s.jpg", quality=88)
