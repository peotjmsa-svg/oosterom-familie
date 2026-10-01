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
person("teunis_1762", "Teunis Huijbertsz van Oostrum", "m", "5-12-1762", "27-8-1830", "Lopikerkapel", occ="schipper",
       note="Gedoopt in Lopikerkapel op 5-12-1762 als Theunes, zoon van Huijbert van Oostrum en Willempje Jaarsveld. "
            "Trouwde op 2-12-1787 in Lopikerkapel met Geertje Dekker uit Noordeloos. Ze kregen veertien kinderen; vier "
            "zoons heetten Arie, en alleen de laatste (1801) bleef leven. Teunis was schipper en woonde in Jaarsveld, "
            "aan de Lek (huwelijksakte van zijn zoon Arie, 1830). Hij overleed in Jaarsveld op 27-8-1830, 68 jaar oud, "
            "drie dagen na zijn vrouw. De overlijdensakte noemt zijn ouders Huibert Oosterom en Willemijntje Jaarsvelt.",
       recs=[("Doop 1762", DTB.format("AE73")), ("Ondertrouw en huwelijk 1787", DTB.format("B00F")),
             ("Overlijden 1830", "hua:CD30A6D2-0FBA-4B6C-B213-C5C1D21D27E4")])
person("geertje_dekker", "Geertje Dekker", "f", "ca. 1767", "24-8-1830", "Noordeloos",
       note="Uit Noordeloos (Alblasserwaard), dochter van Teunis Dekker en Maggeltje Kluit. Overleden in Jaarsveld, 63 jaar oud.",
       recs=[("Overlijden 1830", "hua:FC97F7DF-E530-4C5B-B550-B86061422243")])
for pid, nm, sx, dt, code, note in [
        ("willemijntje_1788", "Willemijntje van Oostrum", "f", "21-9-1788", "AEEC",
         "Kreeg in 1803, 15 jaar oud, een zoon Arie; in het doopboek staat geen vader (AF4C)."),
        ("teunis_1789", "Teunis van Oostrum", "m", "27-12-1789", "AEF8",
         "Trouwde in 1815 in Jaarsveld met Geertrui Streef. Overleden in Jaarsveld op 20-8-1826, 36 jaar oud."),
        ("magteltje_1791", "Magteltje van Oostrum", "f", "4-12-1791", "AF06",
         "Waarschijnlijk jong overleden: in 1800 kregen haar ouders weer een Magteltje."),
        ("huijbert_1792", "Huijbert van Oostrum", "m", "11-11-1792", "AF10", "Trouwde in 1819 in Jaarsveld met Zwaantje 't Lam."),
        ("arie_1795", "Arie van Oostrum", "m", "6-9-1795", "AF1B", "Waarschijnlijk het 'kind van T. Oostrum' dat op 3-2-1796 werd begraven."),
        ("arie_1796", "Arie Oosterom", "m", "2-10-1796", "AF1F", "Waarschijnlijk het 'kind van T. Oostrum' dat op 23-10-1796 werd begraven."),
        ("gerrit_1797", "Gerrit Oostrum", "m", "17-12-1797", "AF2B", "Trouwde in 1821 in Jaarsveld met Lysbeth Jaarsveld."),
        ("arie_1799", "Arie Oostrum", "m", "6-1-1799", "AF33", "Waarschijnlijk het 'kind van T. Oostrum' dat op 4-7-1800 werd begraven."),
        ("magteltje_1800", "Magteltje Oostrum", "f", "23-2-1800", "AF40", "Trouwde in 1824 in Jaarsveld met Gijsbert Oskam, dagloner."),
        ("willempje_1804", "Willempje Oostrum", "f", "1-1-1804", "AF55", ""),
        ("geertje_1807", "Geertje Oosterom", "f", "12-4-1807", "AF69", ""),
        ("teuntje_1808", "Teuntje Oostrum", "f", "18-12-1808", "AF74", "Trouwde in 1833 in Jaarsveld met Ernst Oskam.")]:
    person(pid, nm, sx, dt, None, "Lopikerkapel", note=("Gedoopt in Lopikerkapel. " + note).strip(), recs=[("Doop", DTB.format(code))])
person("jacobus_1805", "Jacobus Oosterom", "m", "ca. 1805", None, "Jaarsveld",
       note="Zijn doop is niet gevonden. Trouwde op 27-8-1834 in Lopik (29 jaar) met Margaretha Verbaan; de akte noemt "
            "Teunis Oosterom en Geertje Dekker als ouders. MyHeritage geeft hem als sterfjaar 1886, maar dat hoort bij "
            "een andere Jacobus (zoon van Johannes).",
       recs=[("Huwelijk 1834", "hua:4C9F89C3-D4B8-476E-B774-34203D56D669")])

# --- Generation 3: Arie Oosterom (1801-1881) ---
person("arie_1801", "Arie Oosterom", "m", "23-2-1801", "15-8-1881", "Jaarsveld", occ="schipper, later bouwman",
       note="Geboren in Jaarsveld, gedoopt op 1-3-1801 in Lopikerkapel als Arie Oostrum, zoon van Teunis en Geertje "
            "Dekker. Hij was de vierde zoon met de naam Arie; de drie eerdere waren waarschijnlijk als baby gestorven. Bij "
            "zijn huwelijk op 4-6-1830 in Willige Langerak met Elisabeth Kooiman (19) was hij, net als zijn vader, "
            "schipper in Jaarsveld. Getuige was onder anderen zijn broer Cornelis Oosterom (24), bouwman. Daarna ging hij "
            "boeren: in 1835 is hij bouwman in Zuid-Polsbroek, en zijn vrouw heet landbouwster. Hij overleed op "
            "80-jarige leeftijd in huis nummer 57 in Polsbroek.",
       recs=[("Doop 1801", DTB.format("AF44")), ("Huwelijk 1830", "hua:4E6732AB-5866-4D96-A40F-79FC7E4836C3"),
             ("Geboorte zoon Teunis 1835", "hua:E4F7BA2B-ADE9-4399-A299-95F0D6C3D701"),
             ("Overlijden 1881", "hua:E1044046-EFE4-4952-ADA6-895FDCFC08AE")], mh="1500229")
person("elisabeth_kooiman", "Elisabeth Kooiman", "f", "ca. 1811", "23-1-1893", "Willige Langerak", occ="landbouwster",
       note="Uit Willige Langerak, dochter van Hendrik Kooiman, bouwman, en Adriana Hooglander (overleden vóór 1830). "
            "Overleden in Polsbroek, 81 jaar oud.",
       recs=[("Huwelijk 1830", "hua:4E6732AB-5866-4D96-A40F-79FC7E4836C3"),
             ("Overlijden 1893", "hua:1C99270F-1324-48CA-9E5F-89E493821A0D")])
person("geertje_1830", "Geertje Oosterom", "f", "24-10-1830", "23-3-1846", "Willige Langerak",
       note="Overleden op 15-jarige leeftijd.", recs=[("Geboorte 1830", "hua:E07C91EB-DC1C-49EB-A6AD-361BB4386DF7"),
                                                     ("Overlijden 1846", "hua:82DAEA90-EB56-4618-9551-F680FCD294BD")])
person("nn_1832", "Levenloos kind", "m", "1832", "27-6-1832", "Polsbroek",
       recs=[("Overlijden 1832", "hua:0FCB577E-53DA-4F57-865F-0956006E4C2B")])
person("hendrik_1833", "Hendrik Oosterom", "m", "17-9-1833", "1909", "Polsbroek",
       note="Sterfjaar uit MyHeritage.", recs=[("Geboorte 1833", "hua:32633A0E-90E0-424B-934E-592C57EAC027")])
person("teunis_1835", "Teunis Oosterom", "m", "12-3-1835", "3-1-1836", "Polsbroek", note="Als baby overleden.",
       recs=[("Geboorte 1835", "hua:E4F7BA2B-ADE9-4399-A299-95F0D6C3D701"),
             ("Overlijden 1836", "hua:CF24087B-386F-42AA-8DA8-19224CFE5A40")])
person("adriana_1838", "Adriana Oosterom", "f", "2-2-1838", "1927", "Polsbroek",
       note="Sterfjaar uit MyHeritage.", recs=[("Geboorte 1838", "hua:F47CE863-728C-4C22-9F7F-FB84B6D42E11")])
person("teuntje_1839", "Teuntje Oosterom", "f", "22-8-1839", "1907", "Polsbroek",
       note="Sterfjaar uit MyHeritage.", recs=[("Geboorte 1839", "hua:A93DAB36-0363-4A91-88A2-13462CA28132")])
person("elizabeth_1845", "Elizabeth Oosterom", "f", "19-3-1845", "13-5-1878", "Polsbroek",
       note="Getrouwd met Joris van der Heiden, landbouwer. Overleden op 33-jarige leeftijd (de akte zegt 30).",
       recs=[("Geboorte 1845", "hua:6F1F1648-2DBA-4159-8F79-84DD662C3257"),
             ("Overlijden 1878", "hua:B659707E-2252-437C-825C-F82E68C715CC")])

# --- Generation 4: Teunis Oosterom (1847-1915) ---
person("teunis_1847", "Teunis Oosterom", "m", "16-5-1847", "25-5-1915", "Polsbroek", occ="landbouwer",
       note="Geboren in Zuid-Polsbroek (de geboorteakte zegt 16 mei, MyHeritage 17 mei). Trouwde in 1870 met Adriana "
            "Cornelia Lekkerkerker uit Benschop (de huwelijksakte is nog niet gevonden). Landbouwer in Polsbroek, in 1875 "
            "in huis nummer 33. Het echtpaar kreeg tussen 1871 en 1895 negentien kinderen; acht van hen stierven als baby. "
            "In de akten wordt de naam vaak Oostrom gespeld. Overleden in Polsbroek, 68 jaar oud. De overlijdensakte noemt "
            "zijn ouders Arie Oosterom en Elizabeth Kooijman.",
       recs=[("Geboorte 1847", "hua:E1BDC780-9C50-4772-9FE5-40D6D4B24307"),
             ("Geboorte zoon Pieter 1875", "hua:E68DD65A-AD25-449A-AF77-D76755DE8B4D"),
             ("Overlijden 1915", "hua:A8F3AC7D-FF87-44EF-9636-6A154584BAF3")], mh="1500025")
person("adriana_cornelia_lekkerkerker", "Adriana Cornelia Lekkerkerker", "f", "6-11-1850", "20-3-1919", "Benschop",
       note="Geboren in Benschop, dochter van Pieter Lekkerkerker en Marrigje Heijkoop van Os. Moeder van negentien "
            "kinderen. Overleden in Polsbroek, 68 jaar oud.",
       recs=[("Geboorte 1850", "hua:EE15904E-175E-49B7-A758-C3AB82372FE5"),
             ("Overlijden 1919", "hua:818C77A3-9184-409B-A719-2C5108CDD310")])
KIDS_1847 = [
    ("elizabeth_1871", "Elizabeth Oostrom", "f", "7-6-1871", None, "hua:C9162314-81CC-423C-A342-905C1B8D124C",
     "Trouwde in 1896 met Arie Oosterom (zoon van Hendrik Oosterom en Deliaantje Rietveld)."),
    ("merrigje_1872", "Merrigje Heijkoop Oostrom", "f", "16-5-1872", "12-8-1872", "hua:7E237296-4B9E-436B-BF98-63B37CFFF0A9", "Als baby overleden."),
    ("merrigje_1873", "Merrigje Heijkoop Oostrom", "f", "12-5-1873", None, "hua:5467032F-DC70-4481-8EAA-9239C210DF71",
     "Trouwde in 1899 met Teunis de Bruin."),
    ("teuntje_1874", "Teuntje Oosterom", "f", "30-4-1874", None, "hua:431E99D9-CE55-4AF7-BC38-C4BC6C025989",
     "Trouwde in 1899 met Arie Molenaar."),
    ("adriana_cornelia_1876", "Adriana Cornelia Oosterom", "f", "4-10-1876", "17-6-1910", "hua:1A17912C-3813-4EF5-B2EF-80DAE0743688",
     "Overleden op 33-jarige leeftijd."),
    ("geertje_1878", "Geertje Oosterom", "f", "24-2-1878", None, "hua:9727F280-DB86-4D38-BEE4-605821687AD0",
     "Trouwde in 1905 met Dirk Rijneveld."),
    ("arie_1879", "Arie Oostrom", "m", "11-5-1879", "2-10-1879", "hua:85A6765F-5690-489B-8415-1CFA2952E226", "Als baby overleden."),
    ("arie_1880", "Arie Oosterom", "m", "28-10-1880", None, "hua:062F51D9-80DF-4845-B5A1-B22CDD37A42D",
     "Trouwde in 1906 met Elizabeth van Dijk."),
    ("cornelis_johannes_1882a", "Cornelis Johannes Oostrom", "m", "27-1-1882", "7-2-1882", "hua:2534F079-13E2-4B3E-A92F-58D71AB0D289", "Als baby overleden."),
    ("cornelis_johannes_1882", "Cornelis Johannes Oosterom", "m", "24-12-1882", None, "hua:478E9659-78FE-4FAE-BC0B-E874C516BF0A",
     "Trouwde in 1913 in Breukelen met Geertruida Agatha Looij."),
    ("teunis_1884", "Teunis Oostrom", "m", "4-5-1884", "12-7-1884", "hua:997AF8E8-5DF8-4ECC-80CC-E9E39D7D1CF4", "Als baby overleden."),
    ("johanna_1885", "Johanna Oostrom", "f", "19-7-1885", "31-8-1885", "hua:642DD921-3489-4C95-9E67-05D3AB543897", "Als baby overleden."),
    ("teunis_1886", "Teunis Oostrom", "m", "16-10-1886", "21-1-1887", "hua:D26962D6-68AB-405E-8066-CDC936335358", "Als baby overleden."),
    ("johanna_1888", "Johanna Oosterom", "f", "8-3-1888", None, "hua:311182E2-77E3-4E86-A602-532BC6A119CD",
     "Trouwde in 1910 met Bastiaan Zwijnenburg."),
    ("adriana_1889", "Adriana Oostrom", "f", "30-6-1889", None, "hua:81B3D5C0-E1B2-4AB6-9AE4-D32844BBCC16",
     "Trouwde in 1916 met Floris Hogendoorn."),
    ("wijntje_1890", "Wijntje Oostrom", "f", "17-11-1890", "5-11-1915", "hua:A8991BDE-2A46-4DF0-AF0B-B8F1E3D9434B",
     "Overleden op 24-jarige leeftijd."),
    ("hendrika_1892", "Hendrika Oostrom", "f", "24-4-1892", None, "hua:7576DDD8-A9D4-45BE-B978-D5C72F490CAA",
     "Trouwde in 1918 met Adriaan Rozendaal."),
    ("teunis_1895", "Teunis Oostrom", "m", "8-2-1895", "21-4-1895", "hua:7F6D6187-4408-4D04-BCE9-6AC470B24B34", "Als baby overleden."),
]
for pid, nm, sx, dt, died, rid, note in KIDS_1847:
    person(pid, nm, sx, dt, died, "Polsbroek", note=note, recs=[("Geboorte", rid)])

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
                            children=["willemijntje_1788", "teunis_1789", "magteltje_1791", "huijbert_1792", "arie_1795",
                                      "arie_1796", "gerrit_1797", "arie_1799", "magteltje_1800", "arie_1801",
                                      "willempje_1804", "jacobus_1805", "geertje_1807", "teuntje_1808"]),
    "c_arie_kooiman": dict(h="arie_1801", w="elisabeth_kooiman", marr="4-6-1830, Willige Langerak",
                           children=["geertje_1830", "nn_1832", "hendrik_1833", "teunis_1835", "adriana_1838",
                                     "teuntje_1839", "elizabeth_1845", "teunis_1847"]),
    "c_teunis_lekkerkerker": dict(h="teunis_1847", w="adriana_cornelia_lekkerkerker", marr="1870, Benschop",
                                  children=sorted([k[0] for k in KIDS_1847] + ["pieter_1875"],
                                                  key=lambda k: (int(P[k]["born"].split("-")[2]), int(P[k]["born"].split("-")[1]),
                                                                 int(P[k]["born"].split("-")[0])))),
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
