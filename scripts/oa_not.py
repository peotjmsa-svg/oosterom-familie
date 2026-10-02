"""Summarise notarial (or any) Open Archieven records: date, deed type, notary, archive ref, all persons.
Usage: python scripts/oa_not.py rel:ID [rel:ID ...]"""
import sys, json, subprocess
sys.stdout.reconfigure(encoding="utf-8")
def L(x): return x if isinstance(x, list) else ([x] if x else [])
def v(d, k): return (d or {}).get(k, {}).get(k, "") if isinstance((d or {}).get(k), dict) else ""
for ident in sys.argv[1:]:
    a, i = ident.split(":", 1)
    d = (lambda j: j[0] if isinstance(j, list) else j)(json.loads(subprocess.run(["curl", "-s", f"https://api.openarch.nl/1.0/records/show.json?archive={a}&identifier={i}&lang=nl"], capture_output=True).stdout))
    names = []
    for p in L(d.get("a2a_Person")):
        n = p.get("a2a_PersonName", {})
        names.append(" ".join(x for x in (v(n, "a2a_PersonNameFirstName"), v(n, "a2a_PersonNamePrefixLastName"), v(n, "a2a_PersonNameLastName")) if x))
    ev = d.get("a2a_Event", {}); dt = ev.get("a2a_EventDate", {})
    s = d.get("a2a_Source", {}); ref = s.get("a2a_SourceReference", {})
    rem = [r.get("a2a_Value", {}).get("a2a_Value", "") for r in L(s.get("a2a_SourceRemark")) + L(ev.get("a2a_EventRemark"))]
    print(f"== {ident} {v(dt,'a2a_Day')}-{v(dt,'a2a_Month')}-{v(dt,'a2a_Year')} | {v(ref,'a2a_Archive')} inv {v(ref,'a2a_RegistryNumber')} nr {v(ref,'a2a_DocumentNumber')} | {' / '.join(x for x in rem if x)[:3000]}")
    print("   ", "; ".join(names))
