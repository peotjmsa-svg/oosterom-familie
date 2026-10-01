"""Print scan URLs (download + viewer) of Open Archieven records. Usage: python scripts/oa_scan.py hua:ID ..."""
import sys, re, subprocess
sys.stdout.reconfigure(encoding="utf-8")
for ident in sys.argv[1:]:
    a, i = ident.split(":", 1)
    t = subprocess.run(["curl", "-s", f"https://api.openarch.nl/1.0/records/show.json?archive={a}&identifier={i}&lang=nl"],
                       capture_output=True).stdout.decode("utf-8", "replace").replace("\/", "/")
    print(ident, re.findall(r'a2a_Uri"?:\{"a2a_Uri":"([^"]+)', t), re.findall(r'a2a_UriViewer":\{"a2a_UriViewer":"([^"]+)', t))
