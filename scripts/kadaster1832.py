"""Draw 1832 cadastral parcels (HisGIS) on a present-day aerial photo (PDOK Luchtfoto, CC BY 4.0) or on the
HisGIS 1832 map. Usage:
  python scripts/kadaster1832.py OUT.jpg GEMEENTE SECTIE "nr,nr,nr" [--zoom 18] [--pad 60] [--base lf|osm|mp] [--house nr]
Parcel numbers like 125bis are allowed. --house marks the parcel with the house in red, the rest in yellow.
Geometry: overpass.hisgis.nl (kad:gemeente / kad:sectie / kad:perceelnr), as used by the hisgis.nl viewer."""
import sys, io, math, json, subprocess, argparse
from PIL import Image, ImageDraw, ImageFont
ap = argparse.ArgumentParser()
ap.add_argument("out"); ap.add_argument("gemeente"); ap.add_argument("sectie"); ap.add_argument("nrs")
ap.add_argument("--zoom", type=int, default=18); ap.add_argument("--pad", type=int, default=80)
ap.add_argument("--base", default="lf"); ap.add_argument("--house", default="")
ap.add_argument("--label", action="store_true")
a = ap.parse_args()
UA = "oosterom-familie research"
nrs = [n.strip() for n in a.nrs.split(",") if n.strip()]
base_nrs = sorted({''.join(c for c in n if c.isdigit()) for n in nrs})
q = f'[out:json][timeout:60];wr["kad:gemeente"="{a.gemeente}"]["kad:sectie"="{a.sectie}"]["kad:perceelnr"~"^({"|".join(base_nrs)})$"];out geom tags;'
d = json.loads(subprocess.run(["curl", "-s", "-X", "POST", "-A", UA, "-H", "X-Requested-With: XMLHttpRequest",
                               "--data-urlencode", "data=" + q, "https://overpass.hisgis.nl/api/interpreter"], capture_output=True).stdout)
polys = []
for e in d["elements"]:
    t = e.get("tags", {}); key = t.get("kad:perceelnr", "") + t.get("kad:perceelnrtvg", "")
    if key not in nrs: continue
    rings = []
    if e["type"] == "way": rings = [e["geometry"]]
    else: rings = [m["geometry"] for m in e.get("members", []) if m.get("role") == "outer" and "geometry" in m]
    for r in rings: polys.append((key, [(p["lat"], p["lon"]) for p in r], t.get("oat:soort", "")))
if not polys: sys.exit("no parcels found")
def px(lat, lon, z):
    n = 2 ** z * 256
    return (lon + 180) / 360 * n, (1 - math.log(math.tan(math.radians(lat)) + 1 / math.cos(math.radians(lat))) / math.pi) / 2 * n
z = a.zoom
pts = [px(la, lo, z) for _, r, _ in polys for la, lo in r]
x0, y0 = min(p[0] for p in pts) - a.pad, min(p[1] for p in pts) - a.pad
x1, y1 = max(p[0] for p in pts) + a.pad, max(p[1] for p in pts) + a.pad
tx0, ty0, tx1, ty1 = int(x0 // 256), int(y0 // 256), int(x1 // 256), int(y1 // 256)
img = Image.new("RGB", ((tx1 - tx0 + 1) * 256, (ty1 - ty0 + 1) * 256), "white")
for tx in range(tx0, tx1 + 1):
    for ty in range(ty0, ty1 + 1):
        u = {"lf": f"https://service.pdok.nl/hwh/luchtfotorgb/wmts/v1_0/Actueel_orthoHR/EPSG:3857/{z}/{tx}/{ty}.jpeg",
             "osm": f"https://geoservices.hisgis.nl/wmts/osm1832/{z}/{tx}/{ty}.png",
             "mp": f"https://geoservices.hisgis.nl/tiles/minuutplans/{z}/{tx}/{ty}"}[a.base]
        b = subprocess.run(["curl", "-s", "-A", UA, u], capture_output=True).stdout
        try:
            t = Image.open(io.BytesIO(b)).convert("RGBA"); img.paste(t, ((tx - tx0) * 256, (ty - ty0) * 256), t)
        except Exception: pass
ov = Image.new("RGBA", img.size, (0, 0, 0, 0)); dr = ImageDraw.Draw(ov)
for key, r, soort in polys:
    xy = [(px(la, lo, z)[0] - tx0 * 256, px(la, lo, z)[1] - ty0 * 256) for la, lo in r]
    house = key == a.house
    dr.polygon(xy, fill=(200, 40, 30, 90) if house else (255, 210, 0, 55), outline=(200, 40, 30, 255) if house else (255, 220, 0, 255), width=3)
    if a.label:
        cx = sum(p[0] for p in xy) / len(xy); cy = sum(p[1] for p in xy) / len(xy)
        dr.text((cx, cy), key, fill=(0, 0, 0, 255))
img = Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB")
img = img.crop((int(x0 - tx0 * 256), int(y0 - ty0 * 256), int(x1 - tx0 * 256), int(y1 - ty0 * 256)))
img.save(a.out, quality=88)
print(a.out, img.size, len(polys), "parcels:", ", ".join(sorted({k for k, _, _ in polys})))
