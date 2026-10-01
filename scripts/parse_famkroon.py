#!/usr/bin/env python3
"""Parse the Smetser / Van Oostrum / Oosterom genealogy of famkroon.nl into data/famkroon.json.

Source: https://www.famkroon.nl/genealogie/stamboom/OOSTEROM.html (saved as raw/famkroon.html). The page is a
"genealogie" in the classic Dutch format: numbered sections (I, II, ..., VIII-g) with a head person, his or her
marriages ("Hij is getrouwd ... met X") and children ("1 : Name, geboren ..., volgt onder IX-a").
People who may be alive (marked {X} by the author, or born after 1925) are left out, with their descendants.
Run: python scripts/parse_famkroon.py
"""
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "..", "raw", "famkroon.html")
OUT = os.path.join(HERE, "..", "data", "famkroon.json")
CUTOFF = 1925

raw = open(RAW, encoding="utf-8", errors="replace").read()
txt = re.sub(r"(?s)<(script|style).*?</\1>", "", raw)
txt = re.sub(r"<br\s*/?>|</p>|</li>|</tr>|</h\d>", "\n", txt)
txt = html.unescape(re.sub(r"<[^>]+>", "", txt))
txt = re.sub(r"(?<=[.\w])(?=I\s+:\s+Stamvader)", "\n", txt)
lines = [re.sub(r"\s+", " ", l).strip() for l in txt.split("\n")]
lines = [l for l in lines if l]

HEAD = re.compile(r"^([IVXL]+(?:-[a-z]+)?)\s*:\s*(.*)$")
CHILD = re.compile(r"^(\d+)\s*:\s*(.*)$")
MARR = re.compile(r"^(Hij|Zij) (?:is|was) (?:in ondertrouw gegaan|ondertrouwd|getrouwd|gehuwd)(.*)$")
EXTRA = re.compile(r"^\((Hij|Zij) is (?:daarnaast|eerder|later|ook) (?:getrouwd|gehuwd|ondertrouwd)(.*)\)$")
KIDS = re.compile(r"^(Uit dit huwelijk|Zijn kind|Zijn kinderen|Zijn zoon|Zijn zonen|Zijn dochter|Zijn dochters|"
                  r"Haar kind|Haar kinderen|Haar zoon|Haar zonen|Haar dochter|Haar dochters|Kinderen uit)")

DATE = r"((?:op |in het jaar |in |rond |omstreeks |tussen |voor |na |ca\. )[^,()]+?)"


def year_of(s):
    m = re.findall(r"(1[0-9]{3})", s or "")
    return int(m[0]) if m else None


def clean_name(n):
    n = re.sub(r"\{[^}]*\}", "", n)
    n = re.sub(r"\s+", " ", n).strip(" ,")
    return n


def parse_person(text):
    """Turn 'Name ook genaamd X {c}, schipper, geboren te P op D, overleden ...' into a dict."""
    living = "{X}" in text
    parts = [p.strip() for p in re.split(r",(?![^()]*\))", text)]
    name_part = parts[0]
    alias = None
    m = re.search(r"\s+ook genaamd\s+(.*)$", name_part)
    if m:
        alias = clean_name(m.group(1))
        name_part = name_part[:m.start()]
    name = clean_name(re.sub(r"^Stamvader\s+", "", name_part))
    occ, born, born_place, died, died_place, bur, residence = [], None, None, None, None, None, None
    for p in parts[1:]:
        pl = p.lower()
        mm = re.match(r"(geboren|gedoopt)(?: te ([^,]+?))?\s+" + DATE + r"(?:\s*\(.*\))?$", p)
        if mm:
            if born is None or mm.group(1) == "geboren":
                born, born_place = mm.group(3).strip(), (mm.group(2) or born_place)
            continue
        mm = re.match(r"(?:overleden|begraven)(?: te ([^,]+?))?\s+" + DATE + r"(?:\s*\(.*\))?$", p)
        if mm:
            if pl.startswith("overleden") or died is None:
                died, died_place = mm.group(2).strip(), mm.group(1)
            continue
        if pl.startswith("geboren") or pl.startswith("gedoopt"):
            mm = re.match(r"(?:geboren|gedoopt) te (.+)$", p)
            if mm and not born_place:
                born_place = mm.group(1)
            continue
        if pl.startswith("overleden") or pl.startswith("begraven"):
            mm = re.match(r"(?:overleden|begraven) te (.+)$", p)
            if mm and not died_place:
                died_place = mm.group(1)
            continue
        if pl.startswith("wonende te"):
            residence = p[len("wonende te "):].split(" (")[0].rstrip(".")
            continue
        if re.match(r"^(zoon|dochter) van", pl) or "jaar oud" in pl or pl.startswith("volgt onder") or pl.startswith("hoogstens") \
                or pl.startswith("minstens") or pl.startswith("ongeveer") or re.match(r"^\d", pl):
            continue
        p = re.sub(r"\s*,?\s*wonende aldaar.*$|^wonende aldaar.*$", "", p).strip()
        if p.lower().startswith("gecremeerd"):
            continue
        if p and len(p) < 80 and p[:1].islower() and not re.match(r"^(van|de|den|der|ten|ter|op|in)", p) and "{" not in p:
            occ.append(p)
    parents = None
    m = re.search(r"(?:zoon|dochter) van (.+?)(?: \(([IVXL]+(?:-[a-z]+)?)\))?(?: en (.+?))?(?:\.|$)", text)
    if m:
        parents = {"father": clean_name(re.sub(r"\([^)]*\)", "", m.group(1))),
                   "mother": clean_name(re.sub(r"\([^)]*\)", "", m.group(3) or "")) or None}
    follows = None
    m = re.search(r"volgt onder ([IVXL]+(?:-[a-z]+)?)", text)
    if m:
        follows = m.group(1)
    sex = None
    if re.search(r"\b(zoon van|Hij )", text):
        sex = "m"
    if re.search(r"\b(dochter van|Zij )", text):
        sex = "f"
    by = year_of(born)
    if by and by > CUTOFF:
        living = True
    if born and re.match(r"na (19[2-9]\d|20\d\d)", born):
        living = True
    return {"name": name, "alias": alias, "occupation": ", ".join(o for o in occ if o) or None,
            "born": born, "born_place": born_place, "died": died, "died_place": died_place,
            "residence": residence, "parents_text": parents, "follows": follows, "living": living, "sex": sex,
            "text": text}


def parse_marriage(text):
    """'te Jaarsveld op 4 juni 1830, op 29-jarige leeftijd (1) met Elisabeth Kooiman ..., dochter van ...'."""
    m = re.search(r"\bmet (.+)$", text)
    spouse_txt = m.group(1) if m else ""
    place = re.search(r"\bte ([A-Z][^,]+?)(?: op| in| rond|,|$)", text[:m.start()] if m else text)
    date = re.search(r"(?:op|in het jaar|rond|in) ([0-9][^,]*?\d{4}|\d{4})", text[:m.start()] if m else text)
    spouse_txt = re.sub(r"\s*\((?:\d+|minstens|ongeveer|hoogstens)[^)]*\)", "", spouse_txt, count=1)
    return {"place": place.group(1).strip() if place else None, "date": date.group(1).strip() if date else None,
            "spouse": parse_person(spouse_txt) if spouse_txt else None, "text": text}


# ---- walk the sections ----
sections = {}
order = []
cur = None
for l in lines:
    h = HEAD.match(l)
    if h and (h.group(1) in ("I",) or "-" in h.group(1) or re.match(r"^[IVXL]+$", h.group(1))) and " : " in l.replace("  ", " "):
        code = h.group(1)
        cur = {"code": code, "head": parse_person(h.group(2)), "items": []}
        sections[code] = cur
        order.append(code)
        continue
    if cur is not None:
        cur["items"].append(l)

people = {}
families = []


def add_person(pid, d):
    d = dict(d)
    d["id"] = pid
    people[pid] = d
    return pid


for code in order:
    sec = sections[code]
    head_id = "fk_" + code
    if head_id not in people:
        add_person(head_id, sec["head"])
    else:
        people[head_id].update({k: v for k, v in sec["head"].items() if v})
    fam = None
    child_ctx = None  # id of the last child (for child marriages)
    in_kids = False
    items = sec["items"]
    for idx, l in enumerate(items):
        if l.startswith("Famkroon") or l.startswith("Gegenereerd"):
            continue
        c = CHILD.match(l)
        if c and in_kids:
            n = c.group(1)
            cd = parse_person(c.group(2))
            if cd["follows"]:
                cid = "fk_" + cd["follows"]
                if cid not in people:
                    add_person(cid, cd)
            else:
                cid = add_person(f"fk_{code}_{fam['n'] if fam else 0}_{n}", cd)
            if fam is None:
                fam = {"id": f"fkf_{code}_0", "n": 0, "husb": head_id if sec["head"]["sex"] != "f" else None,
                       "wife": head_id if sec["head"]["sex"] == "f" else None, "chil": [], "marr_date": None,
                       "marr_place": None}
                families.append(fam)
            fam["chil"].append(cid)
            child_ctx = cid
            continue
        mm = MARR.match(l) or EXTRA.match(l)
        if mm:
            who, rest = mm.group(1), mm.group(2)
            md = parse_marriage(rest)
            nxt = next((x for x in items[idx + 1:] if not EXTRA.match(x)), "")
            heads_marriage = bool(KIDS.match(nxt)) and re.search(r"\((?:[2-9])\) met", rest) is not None
            if child_ctx and in_kids and not EXTRA.match(l) and not heads_marriage:
                # marriage of the last child (no own section)
                sp = md["spouse"]
                if sp and sp["name"]:
                    sid = add_person(child_ctx + "_sp" + str(sum(1 for f in families if child_ctx in (f["husb"], f["wife"])) + 1), sp)
                    ch = people[child_ctx]
                    if ch.get("sex") is None:
                        ch["sex"] = "m" if who == "Hij" else "f"
                    hus, wif = (child_ctx, sid) if who == "Hij" else (sid, child_ctx)
                    people[sid]["sex"] = "f" if who == "Hij" else "m"
                    families.append({"id": "fkf_" + sid, "n": 0, "husb": hus, "wife": wif, "chil": [],
                                     "marr_date": md["date"], "marr_place": md["place"]})
                continue
            if EXTRA.match(l):
                continue  # earlier/later marriage of a spouse: keep as text only
            sp = md["spouse"]
            k = sum(1 for f in families if f["id"].startswith(f"fkf_{code}_")) + 1
            sid = None
            if sp and sp["name"] and not sp["name"].lower().startswith("een onbekende"):
                sid = add_person(f"fk_{code}_sp{k}", sp)
                people[sid]["sex"] = "f" if who == "Hij" else "m"
            people[head_id]["sex"] = "m" if who == "Hij" else "f"
            fam = {"id": f"fkf_{code}_{k}", "n": k, "husb": head_id if who == "Hij" else sid,
                   "wife": sid if who == "Hij" else head_id, "chil": [], "marr_date": md["date"],
                   "marr_place": md["place"]}
            families.append(fam)
            in_kids = False
            child_ctx = None
            continue
        if KIDS.match(l):
            in_kids = True
            if l.startswith(("Zijn ", "Haar ")) and (fam is None or fam["chil"] or "onbekende" in l):
                k = sum(1 for f in families if f["id"].startswith(f"fkf_{code}_")) + 1
                fam = {"id": f"fkf_{code}_{k}", "n": k, "husb": head_id if l.startswith("Zijn") else None,
                       "wife": head_id if l.startswith("Haar") else None, "chil": [], "marr_date": None,
                       "marr_place": None}
                families.append(fam)
            child_ctx = None
            continue

# drop living people and everything below them
living = {pid for pid, p in people.items() if p.get("living")}
changed = True
while changed:
    changed = False
    for f in families:
        if (f["husb"] in living or f["wife"] in living) and any(c not in living for c in f["chil"]):
            for c in f["chil"]:
                if c not in living:
                    living.add(c)
                    changed = True
for pid in living:
    people.pop(pid, None)
fams = []
for f in families:
    f["chil"] = [c for c in f["chil"] if c in people]
    if f["husb"] not in people:
        f["husb"] = None
    if f["wife"] not in people:
        f["wife"] = None
    if f["husb"] or f["wife"]:
        fams.append(f)
for p in people.values():
    p.pop("text", None)
json.dump({"source": "https://www.famkroon.nl/genealogie/stamboom/OOSTEROM.html", "people": people,
           "families": fams}, open(OUT, "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
print(len(people), "personen,", len(fams), "gezinnen,", len(living), "levend/weggelaten ->", os.path.normpath(OUT))
