#!/usr/bin/env python3
"""Build data/familie.json and data/stamboom.json for the Oosterom family site.

Every fact comes from a record on Open Archieven (Het Utrechts Archief, Streekarchief Midden-Holland) or, where marked,
from the MyHeritage tree "Sonja Oosterom + Florian Hillen". See onderzoek/plan-oosterom.md for the reasoning.
Living people are not named. Edit this script, never the JSON. Run: python scripts/build_data.py
"""
import json
import os
import re

OA = "https://www.openarchieven.nl/"
MH = "https://www.myheritage.nl/profile-OYYV6RLFE43U2DPKEJO6ILZTOTT5LPI-"
DTB = "hua:5329E09C-{}-4F89-E053-4701000AF4B8"  # church books Lopikerkapel (Het Utrechts Archief)

P = {}


def person(pid, name, sex, born=None, died=None, place=None, note="", recs=(), mh=None, occ=None):
    srcs = [{"label": lab, "url": OA + rid} for lab, rid in recs]
    if mh:
        srcs.append({"label": "MyHeritage-stamboom", "url": MH + mh})
    P[pid] = {"id": pid, "name": name, "sex": sex, "born": born, "died": died, "place": place, "note": note,
              "occupation": occ, "line": "oosterom", "sources": srcs}


# --- Generation 1: Huijbert van Oostrum (Lopikerkapel) ---
person("huijbert", "Huijbert van Oostrum", "m", "ca. 1717", "begraven 4-12-1792", "Lopikerkapel",
       note="Oudste zekere voorvader. Woonde onder Jaarsvelderkapel en noemde zich bij zijn eerste huwelijk Huijbert "
            "Janse Oostrum: zoon van een Jan. Trouwde op 3-3-1748 in Lopikerkapel met Ariaentje Boef uit Lopik; vier weken "
            "later werd hun dochter Geertruij gedoopt. Ariaentje werd in december 1749 begraven, een kindje in januari 1750. "
            "Op 1-6-1751 trouwde hij met Willempje Jaarsveld (begraven 27-12-1764). In 1771 stond hij, wonend in "
            "Jaarsveld, borg voor de pacht van Jan de With. Hij werd op 4-12-1792 in de kerk van Lopikerkapel begraven, "
            "in een huurgraf. Waarschijnlijk is hij de Huijbert die op 25-7-1717 in Lopikerkapel werd gedoopt als zoon "
            "van Jan Ariensz van Oostrum en Geertje Gerrits (van Beusekom), maar dat is nog niet bewezen (zie de bronnenpagina).",
       recs=[("Ondertrouw en huwelijk 1748", DTB.format("AFA3")), ("Doop dochter Geertruij 1748", DTB.format("AE26")),
             ("Ondertrouw en huwelijk 1751", DTB.format("AFA6")),
             ("Borgtocht 1771", "hua:609C5BC0-CC36-4642-E053-4701000A17FD"), ("Begrafenis 1792", DTB.format("B2A6"))])
person("ariaentje_boef", "Ariaentje Boef", "f", None, "begraven 15-12-1749", "Lopikerkapel",
       note="Eerste vrouw van Huijbert van Oostrum, uit Lopik. Getrouwd op 3-3-1748. Begraven in Lopikerkapel als "
            "'vrouw van Huijbert van Oostrum'; een kind van Huijbert werd op 3-1-1750 begraven.",
       recs=[("Huwelijk 1748", DTB.format("AFA3")), ("Begrafenis 1749", DTB.format("B190")),
             ("Begrafenis kind 1750", DTB.format("B18C"))])
person("geertruij_1748", "Geertruij van Oostrum", "f", "31-3-1748", None, "Lopikerkapel",
       note="Gedoopt in Lopikerkapel, dochter van Huijbert en Ariaentje Boef. Waarschijnlijk de Geertruij van Oostrum die "
            "in 1772 trouwde met Jan van der Graaf en in 1791 met Aelbert van Randwijk (niet bewezen).",
       recs=[("Doop 1748", DTB.format("AE26"))])
person("willempje_jaarsveld", "Willempje Jaarsveld", "f", None, "begraven 27-12-1764", "Jaarsveld",
       note="Kwam uit Jaarsveld. In de akten ook Willempie Jaersvelt en Willemijntje Jaarsvelt. Begraven in "
            "Lopikerkapel als 'Willemijntje Jaarsveld, vrouw van Huijbert Oostrum'.",
       recs=[("Huwelijk 1751", DTB.format("AFA6")), ("Begrafenis 1764", DTB.format("B222")), ("Overlijden zoon Teunis 1830", "hua:CD30A6D2-0FBA-4B6C-B213-C5C1D21D27E4")])
for pid, nm, sx, dt, code in [("gerrigje_1753", "Gerrigje van Oostrum", "f", "4-2-1753", "AE35"),
                              ("willem_1754", "Willem van Oostrum", "m", "25-8-1754", "AE3E"),
                              ("arie_1756", "Arie van Oostrum", "m", "31-10-1756", "AE49"),
                              ("dirkje_1759", "Dirkje van Oostrum", "f", "11-11-1759", "AE5C")]:
    person(pid, nm, sx, dt, None, "Lopikerkapel", note="Gedoopt in Lopikerkapel.", recs=[("Doop", DTB.format(code))])

# --- Generation 2: Teunis Huijbertsz ---
person("teunis_1762", "Teunis Huijbertsz van Oostrum", "m", "5-12-1762", "27-8-1830", "Lopikerkapel",
       note="Gedoopt in Lopikerkapel op 5-12-1762 als Theunes, zoon van Huijbert van Oostrum en Willempje Jaarsveld. "
            "Trouwde op 2-12-1787 in Lopikerkapel met Geertje Dekker uit Noordeloos. Ze kregen minstens tien kinderen. "
            "Overleden in Jaarsveld op 27-8-1830, 68 jaar oud, drie dagen na zijn vrouw. De overlijdensakte noemt zijn "
            "ouders Huibert Oosterom en Willemijntje Jaarsvelt.",
       recs=[("Doop 1762", DTB.format("AE73")), ("Ondertrouw en huwelijk 1787", DTB.format("B00F")),
             ("Overlijden 1830", "hua:CD30A6D2-0FBA-4B6C-B213-C5C1D21D27E4")])
person("geertje_dekker", "Geertje Dekker", "f", "ca. 1767", "24-8-1830", "Noordeloos",
       note="Uit Noordeloos (Alblasserwaard), dochter van Teunis Dekker en Maggeltje Kluit. Overleden in Jaarsveld, 63 jaar oud.",
       recs=[("Overlijden 1830", "hua:FC97F7DF-E530-4C5B-B550-B86061422243")])
for pid, nm, sx, dt, code, note in [
        ("willemijntje_1788", "Willemijntje van Oostrum", "f", "21-9-1788", "AEEC", ""),
        ("teunis_1789", "Teunis van Oostrum", "m", "27-12-1789", "AEF8",
         "Volgens MyHeritage overleden in 1826; in Jaarsveld overleed op 20-8-1826 een Teunis Teunisz Oosterom."),
        ("huijbert_1792", "Huijbert van Oostrum", "m", "11-11-1792", "AF10", ""),
        ("arie_1795", "Arie van Oostrum", "m", "6-9-1795", "AF1B", "Waarschijnlijk jong overleden: in 1799 en 1801 kregen zijn ouders weer een Arie."),
        ("gerrit_1797", "Gerrit Oostrum", "m", "17-12-1797", "AF2B", ""),
        ("arie_1799", "Arie Oostrum", "m", "6-1-1799", "AF33", "Waarschijnlijk jong overleden: in 1801 kregen zijn ouders weer een Arie."),
        ("willempje_1804", "Willempje Oostrum", "f", "1-1-1804", "AF55", ""),
        ("geertje_1807", "Geertje Oosterom", "f", "12-4-1807", "AF69", ""),
        ("teuntje_1808", "Teuntje Oostrum", "f", "18-12-1808", "AF74", "")]:
    person(pid, nm, sx, dt, None, "Lopikerkapel", note=("Gedoopt in Lopikerkapel. " + note).strip(), recs=[("Doop", DTB.format(code))])

# --- Generation 3: Arie Oosterom (1801-1881) ---
person("arie_1801", "Arie Oosterom", "m", "23-2-1801", "15-8-1881", "Jaarsveld",
       note="Geboren in Jaarsveld, gedoopt op 1-3-1801 in Lopikerkapel als Arie Oostrum, zoon van Teunis en Geertje "
            "Dekker. Hij was het derde kind met de naam Arie: twee broertjes met die naam waren waarschijnlijk jong gestorven. Trouwde "
            "op 4-6-1830 in Willige Langerak met Elisabeth Kooiman (19). Woonde daarna in Polsbroek, waar hij op 80-jarige "
            "leeftijd overleed.",
       recs=[("Doop 1801", DTB.format("AF44")), ("Huwelijk 1830", "hua:4E6732AB-5866-4D96-A40F-79FC7E4836C3"),
             ("Overlijden 1881", "hua:E1044046-EFE4-4952-ADA6-895FDCFC08AE")], mh="1500229")
person("elisabeth_kooiman", "Elisabeth Kooiman", "f", "ca. 1811", "23-1-1893", "Willige Langerak",
       note="Uit Willige Langerak, dochter van Hendrik Kooiman en Adriana Hooglander. Overleden in Polsbroek, 81 jaar oud.",
       recs=[("Huwelijk 1830", "hua:4E6732AB-5866-4D96-A40F-79FC7E4836C3"),
             ("Overlijden 1893", "hua:1C99270F-1324-48CA-9E5F-89E493821A0D")])
person("geertje_1830", "Geertje Oosterom", "f", "24-10-1830", "23-3-1846", "Willige Langerak",
       note="Overleden op 15-jarige leeftijd.", recs=[("Overlijden 1846", "hua:82DAEA90-EB56-4618-9551-F680FCD294BD")])
person("hendrik_1833", "Hendrik Oosterom", "m", "17-9-1833", "1909", "Polsbroek", note="Gegevens uit MyHeritage (profiel van vader Arie).", mh="1500229")
person("adriana_1838", "Adriana Oosterom", "f", "2-2-1838", "1927", "Polsbroek", note="Gegevens uit MyHeritage (profiel van vader Arie).", mh="1500229")
person("teuntje_1839", "Teuntje Oosterom", "f", "22-8-1839", "1907", "Polsbroek",
       recs=[("Geboorte 1839", "hua:A93DAB36-0363-4A91-88A2-13462CA28132")])
person("elizabeth_1845", "Elizabeth Oosterom", "f", "19-3-1845", "13-5-1878", "Polsbroek",
       note="Getrouwd met Joris van der Heiden. Overleden op 30-jarige leeftijd.",
       recs=[("Geboorte 1845", "hua:6F1F1648-2DBA-4159-8F79-84DD662C3257"),
             ("Overlijden 1878", "hua:B659707E-2252-437C-825C-F82E68C715CC")])

# --- Generation 4: Teunis Oosterom (1847-1915) ---
person("teunis_1847", "Teunis Oosterom", "m", "17-5-1847", "25-5-1915", "Polsbroek", occ="landbouwer (bouwman)",
       note="Geboren in Zuid-Polsbroek. Trouwde op 9-12-1870 in Benschop met Adriana Cornelia Lekkerkerker (datum "
            "uit MyHeritage; de akte is nog niet gezien). Boer in Polsbroek, waar hij in 1915 op 68-jarige leeftijd "
            "overleed. De overlijdensakte noemt zijn ouders Arie Oosterom en Elizabeth Kooijman.",
       recs=[("Overlijden 1915", "hua:A8F3AC7D-FF87-44EF-9636-6A154584BAF3")], mh="1500025")
person("adriana_cornelia_lekkerkerker", "Adriana Cornelia Lekkerkerker", "f", "1850", "1919", "Benschop",
       note="Dochter van Pieter Lekkerkerker en Marrigje van Os Heijkoop (volgens MyHeritage).",
       recs=[("Geboorte zoon Pieter 1875", "hua:E68DD65A-AD25-449A-AF77-D76755DE8B4D")])
for pid, nm, sx, dt, rid in [("teuntje_1874", "Teuntje Oosterom", "f", "30-4-1874", "hua:431E99D9-CE55-4AF7-BC38-C4BC6C025989"),
                             ("adriana_cornelia_1876", "Adriana Cornelia Oosterom", "f", "4-10-1876", "hua:1A17912C-3813-4EF5-B2EF-80DAE0743688"),
                             ("geertje_1878", "Geertje Oosterom", "f", "24-2-1878", "hua:9727F280-DB86-4D38-BEE4-605821687AD0"),
                             ("arie_1880", "Arie Oosterom", "m", "28-10-1880", "hua:062F51D9-80DF-4845-B5A1-B22CDD37A42D"),
                             ("cornelis_johannes_1882", "Cornelis Johannes Oosterom", "m", "24-12-1882", "hua:478E9659-78FE-4FAE-BC0B-E874C516BF0A"),
                             ("johanna_1888", "Johanna Oosterom", "f", "8-3-1888", "hua:311182E2-77E3-4E86-A602-532BC6A119CD")]:
    person(pid, nm, sx, dt, None, "Polsbroek", recs=[("Geboorte", rid)])
person("arie_1879", "Arie Oosterom", "m", "1879", "2-10-1879", "Polsbroek", note="Als baby overleden.",
       recs=[("Overlijden 1879", "hua:86C4B84D-AC07-402C-9714-87C525AECBE0")])

# --- Generation 5: Pieter Oosterom (1875-1959) ---
person("pieter_1875", "Pieter Oosterom", "m", "17-5-1875", "10-9-1959", "Polsbroek", occ="landbouwer (bouwman)",
       note="Geboren in Polsbroek. Trouwde daar op 25-10-1907 (32 jaar) met Willempje Lekkerkerker (30). Na de geboorte "
            "van zoon Arie in 1908 verhuisde het gezin naar Bergambacht, aan de overkant van de Lek in Zuid-Holland, "
            "waar Pieter boer was. Hij overleed daar op 84-jarige leeftijd.",
       recs=[("Geboorte 1875", "hua:E68DD65A-AD25-449A-AF77-D76755DE8B4D"),
             ("Huwelijk 1907", "hua:6CF6874D-62DA-415E-8D90-C7F48CB94E2F"),
             ("Overlijden 1959", "smh:308d74b4-2b47-afa9-72cb-420fced74522")], mh="1500008")
person("willempje_lekkerkerker", "Willempje Lekkerkerker", "f", "ca. 1877", None, "Polsbroek",
       note="Dochter van Arie Lekkerkerker en Steventje de With. Zij overleefde haar man (1959).",
       recs=[("Huwelijk 1907", "hua:6CF6874D-62DA-415E-8D90-C7F48CB94E2F")])
for pid, nm, sx, dt, died, rid, note in [
        ("adriana_cornelia_1909", "Adriana Cornelia Oosterom", "f", "8-5-1909", "2-9-1909", "smh:9121e8b4-b0a0-d937-ed59-1ab76fcc19d5", "Als baby overleden."),
        ("adriana_cornelia_1910", "Adriana Cornelia Oosterom", "f", "24-8-1910", None, "smh:13a46ae7-3cbf-4a19-37a8-743211523b0c", ""),
        ("steventje_1913", "Steventje Oosterom", "f", "4-2-1913", None, "smh:ae973130-869f-8a09-8b45-616c5505d34c", ""),
        ("teuntje_elizabeth_1915", "Teuntje Elizabeth Oosterom", "f", "4-5-1915", None, "smh:fc61ba19-e389-be87-698f-10566246532c", ""),
        ("teunis_1917", "Teunis Oosterom", "m", "7-7-1917", "9-9-1917", "smh:7725f8ac-8f9f-0119-fda7-d082d828f539", "Als baby overleden."),
        ("willempje_gijsbertha_1920", "Willempje Gijsbertha Oosterom", "f", "29-7-1920", None, "smh:a121e60a-8964-22cd-6fcf-45440fd15fb7", ""),
        ("wijntje_hendrika_1923", "Wijntje Hendrika Oosterom", "f", "22-4-1923", None, "smh:7af7d238-4ef4-beb4-a0de-f9f8c4b890e8", "")]:
    person(pid, nm, sx, dt, died, "Bergambacht", note=note, recs=[("Geboorte", rid)])

# --- Generation 6: Arie Oosterom (1908-1988) ---
person("arie_1908", "Arie Oosterom", "m", "4-5-1908", "1988", "Polsbroek",
       note="Geboren in Polsbroek, groeide op in Bergambacht. Getrouwd met Johanna Jacoba de Jong. Ze kregen vijf "
            "kinderen. Sterfjaar uit MyHeritage.",
       recs=[("Geboorte 1908", "hua:F79DE64A-C1CC-CEE3-E043-4701000AEA30")], mh="1500004")
person("johanna_de_jong", "Johanna Jacoba de Jong", "f", "1917", "1994", None, note="Gegevens uit MyHeritage.")
person("kinderen_1908", "Vijf kinderen", "m", None, None, None,
       note="Drie zoons en twee dochters. Zij en hun nakomelingen worden op deze site niet bij naam genoemd.")

C = {
    "c_huijbert_boef": dict(h="huijbert", w="ariaentje_boef", marr="3-3-1748, Lopikerkapel", children=["geertruij_1748"]),
    "c_huijbert_jaarsveld": dict(h="huijbert", w="willempje_jaarsveld", marr="1-6-1751, Lopikerkapel",
                                 children=["gerrigje_1753", "willem_1754", "arie_1756", "dirkje_1759", "teunis_1762"]),
    "c_teunis_dekker": dict(h="teunis_1762", w="geertje_dekker", marr="2-12-1787, Lopikerkapel",
                            children=["willemijntje_1788", "teunis_1789", "huijbert_1792", "arie_1795", "gerrit_1797",
                                      "arie_1799", "arie_1801", "willempje_1804", "geertje_1807", "teuntje_1808"]),
    "c_arie_kooiman": dict(h="arie_1801", w="elisabeth_kooiman", marr="4-6-1830, Willige Langerak",
                           children=["geertje_1830", "hendrik_1833", "adriana_1838", "teuntje_1839", "elizabeth_1845",
                                     "teunis_1847"]),
    "c_teunis_lekkerkerker": dict(h="teunis_1847", w="adriana_cornelia_lekkerkerker", marr="9-12-1870, Benschop",
                                  children=["teuntje_1874", "pieter_1875", "adriana_cornelia_1876", "geertje_1878",
                                            "arie_1879", "arie_1880", "cornelis_johannes_1882", "johanna_1888"]),
    "c_pieter_lekkerkerker": dict(h="pieter_1875", w="willempje_lekkerkerker", marr="25-10-1907, Polsbroek",
                                  children=["arie_1908", "adriana_cornelia_1909", "adriana_cornelia_1910", "steventje_1913",
                                            "teuntje_elizabeth_1915", "teunis_1917", "willempje_gijsbertha_1920",
                                            "wijntje_hendrika_1923"]),
    "c_arie_dejong": dict(h="arie_1908", w="johanna_de_jong", marr=None, children=["kinderen_1908"]),
}
for cid, c in C.items():
    c["id"] = cid


def year(v):
    m = re.findall(r"(\d{4})", str(v or ""))
    return int(m[-1]) if m else None


def fmt_date(v):
    m = re.match(r"^(\d+)-(\d+)-(\d+)$", str(v or ""))
    if not m:
        return v
    maand = ["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]
    return f"{int(m[1])} {maand[int(m[2]) - 1]} {m[3]}"


here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "..", "data", "familie.json"), "w", encoding="utf-8", newline="\n") as fh:
    json.dump({"people": P, "couples": C}, fh, ensure_ascii=False, indent=1)

# Descendant tree in the format of js/stamboom.js (same as the Hillen and Kagol sites)
tree_people = {}
for pid, pp in P.items():
    kids = []
    for f in C.values():
        if pid in (f["h"], f["w"]):
            kids += [k for k in f["children"] if k not in kids]
    facts = []
    if pp["born"]:
        facts.append("geboren " + str(fmt_date(pp["born"])))
    if pp["died"]:
        facts.append("overleden " + str(fmt_date(pp["died"])))
    tree_people[pid] = {
        "id": pid, "name": pp["name"], "sex": "M" if pp["sex"] == "m" else "F",
        "birth_year": year(pp["born"]), "death_year": year(pp["died"]),
        "occupation": pp["occupation"], "place": pp["place"],
        "note": (" · ".join(facts) + (". " if facts and pp["note"] else "") + pp["note"]) or None,
        "sources": pp["sources"], "children": kids,
    }
tree_fams = {fid: {"id": fid, "husb": f["h"], "wife": f["w"], "chil": f["children"],
                   "marr_date": f["marr"], "marr_place": None} for fid, f in C.items()}
with open(os.path.join(here, "..", "data", "stamboom.json"), "w", encoding="utf-8", newline="\n") as fh:
    json.dump({"root_id": "huijbert", "people": tree_people, "families": tree_fams,
               "stats": {"individuals": len(tree_people), "families": len(tree_fams)}}, fh, ensure_ascii=False, indent=1)
print(len(P), "personen,", len(C), "gezinnen")
