"""Download pages of a Het Utrechts Archief scanned register at 'large' size.
The viewer's thumbnail URL works with format=large; miahd increases by 1 per page.
Usage: python scripts/hua_page.py BASE_URL_WITHOUT_NNNN MIAHD_OF_PAGE_1 OUTDIR n1 [n2 ...]
BASE example: https://img.hetutrechtsarchief.nl/mi-39/hua/archiefbank/_Projecten2020/DTR06_2020_337-10_20190101_001/7/NL-UtHUA_337-10_7_"""
import sys, subprocess, os
base, m1, out = sys.argv[1], int(sys.argv[2]), sys.argv[3]
os.makedirs(out, exist_ok=True)
for n in map(int, sys.argv[4:]):
    f = os.path.join(out, f"p{n:04d}.jpg")
    if not os.path.exists(f) or os.path.getsize(f) < 10000:
        subprocess.run(["curl", "-s", "-o", f, f"{base}{n:04d}.jpg?format=large&miadt=39&miahd={m1 + n - 1}&mivast=39&rdt=20230905"])
    print(f, os.path.getsize(f))
