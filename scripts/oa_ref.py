"""Book, document number and scan GUID of Open Archieven records. Usage: python scripts/oa_ref.py hua:ID ..."""
import sys, re, subprocess
sys.stdout.reconfigure(encoding="utf-8")
for ident in sys.argv[1:]:
    a, i = ident.split(":", 1)
    t = subprocess.run(["curl", "-s", f"https://api.openarch.nl/1.0/records/show.json?archive={a}&identifier={i}&lang=nl"],
                       capture_output=True).stdout.decode("utf-8", "replace").replace(chr(92)+"/", "/")
    g = lambda k: (re.findall(r'a2a_' + k + r'":\{"a2a_' + k + r'":"([^"]+)', t) or [""])[0]
    print(ident, "|", g("Book"), "| akte", g("DocumentNumber"), "|", g("RegistryNumber"), "|", g("Uri"))
