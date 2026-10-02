"""Contact sheets of scans for reading: python scripts/sheet.py DIR FROM TO [PER=4] [W=1000] -> DIR/sheets/NNNN.jpg"""
import sys, os
from PIL import Image
d, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
per = int(sys.argv[4]) if len(sys.argv) > 4 else 4; w = int(sys.argv[5]) if len(sys.argv) > 5 else 1000
os.makedirs(os.path.join(d, "sheets"), exist_ok=True)
files = [os.path.join(d, f"s{i:04d}.jpg") for i in range(a, b + 1) if os.path.exists(os.path.join(d, f"s{i:04d}.jpg"))]
for k in range(0, len(files), per):
    ims = []
    for f in files[k:k + per]:
        im = Image.open(f).convert("L"); W, H = im.size
        im = im.crop((int(W * .1), int(H * .05), int(W * .92), int(H * .95)))
        ims.append(im.resize((w, int(im.size[1] * w / im.size[0]))))
    h = max(i.size[1] for i in ims); cols = 2
    s = Image.new("L", (w * cols, h * ((len(ims) + 1) // 2)), 255)
    for i, im in enumerate(ims): s.paste(im, ((i % cols) * w, (i // cols) * h))
    out = os.path.join(d, "sheets", os.path.basename(files[k])); s.save(out, quality=80); print(out, [os.path.basename(f) for f in files[k:k+per]])
