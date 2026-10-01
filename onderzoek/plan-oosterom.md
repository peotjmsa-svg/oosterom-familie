# Research plan: the Oosterom (Van Oostrum) line back in time

Scope (user, 2026-10-01): only the direct Oosterom line and the women who married into it. Starting point: Willem
Oosterom (the user's grandfather, father of Sonja Oosterom), son of Arie Oosterom (1908–1988). Willem and his
siblings are private in MyHeritage and are not named on the site.

## The line so far

| Gen. | Man | Wife | Places | Source strength |
|------|-----|------|--------|-----------------|
| 0 | Willem Oosterom (private) | – | – | user |
| 1 | Arie Oosterom, b. 4-5-1908 Polsbroek, d. 1988 | Johanna Jacoba de Jong, 1917–1994 | Polsbroek, Bergambacht | birth record 1908 (parents Pieter × Willempje Lekkerkerker); death year and wife only MyHeritage |
| 2 | Pieter Oosterom, 17-5-1875 Polsbroek – 10-9-1959 Bergambacht, landbouwer/bouwman | Willempje Lekkerkerker, ca. 1877 (dau. of Arie Lekkerkerker × Steventje de With) | Polsbroek, Bergambacht from 1909 | marriage 25-10-1907 Polsbroek names both sets of parents; death 1959 |
| 3 | Teunis Oosterom, 17-5-1847 Zuid-Polsbroek – 25-5-1915 Polsbroek, landbouwer | Adriana Cornelia Lekkerkerker, 1850–1919 | Polsbroek; m. 9-12-1870 Benschop (MyHeritage, deed not seen) | death 1915 names parents Arie Oosterom × Elizabeth Kooijman |
| 4 | Arie Oosterom, 23-2-1801 Jaarsveld (bapt. 1-3-1801 Lopikerkapel) – 15-8-1881 Polsbroek | Elisabeth Kooiman, ca. 1811 – 23-1-1893 (dau. of Hendrik Kooiman × Adriana Hooglander) | m. 4-6-1830 Willige Langerak | marriage 1830 names Teunis Oosterom × Geertje Dekker; baptism 1801 same |
| 5 | Teunis Huijbertsz van Oostrum, bapt. 5-12-1762 Lopikerkapel – 27-8-1830 Jaarsveld | Geertje Dekker of Noordeloos, ca. 1767 – 24-8-1830 (dau. of Teunis Dekker × Maggeltje Kluit) | m. 2-12-1787 Lopikerkapel | death 1830 names Huibert Oosterom × Willemijntje Jaarsvelt; baptism 1762 same; "Huijbertsz" in 1788 |
| 6 | Huijbert van Oostrum ("Huijbert Janse" 1748) | 1) Ariaentje Boef († before 1751); 2) Willempje Jaarsveld of Jaarsveld, m. 1-6-1751 Lopikerkapel | Lopikerkapel | banns 1751 name Boef as previous wife |
| 7 | ? Jan Ariensz van Oostrum | ? | Lopikerkapel | **the wall: Huijbert's own baptism is not proven** |

All record ids are in `scripts/build_data.py` (Open Archieven: `hua:` = Het Utrechts Archief, `smh:` = Streekarchief
Midden-Holland). Church books of Lopikerkapel have ids `hua:5329E09C-XXXX-4F89-E053-4701000AF4B8`.

## The wall: who was Huijbert's father?

Jan Ariensz (Adriaense) van Oostrum, Lopikerkapel:
- m. 2-4-1693 Lopikerkapel Lijsbeth Huijberts (`hua:5329E09C-6F67-…`). Children: bapt. 28-1-1694 (AC50, not read),
  Huijbert 14-4-1695 (AC58, mother "Lijsberth"), 25-6-1699 (AC82), 1-5-1701 (AC96), 16-11-1704 (ACBE).
- m. 2) 22-7-1709 Lopikerkapel Geertie van Beusekom, widower of Lijsbeth Huijbertse (`6FAA`). Children: 8-6-1710 (ACE4),
  21-2-1712 (ACFC), 6-10-1715 (AD1F), Huijbert 25-7-1717 (AD25, mother "Geertie Gerritse"), 20-10-1718 (AD32),
  10-1-1721 (AD52), 27-6-1723 (AD5A).
- Jan named a son Huijbert in 1695 (after his first wife's father) and again in 1717. Usually a name was reused only
  after the first child died, so the 1717 Huijbert is the likelier ancestor. Not proven.
- MyHeritage puts "Arien Ariensz van Oostrum, ca. 1660" directly above Huijbert "Janszn" (b. 25-7-1717, d. 1792). That
  skips Jan. Arien is probably Jan's father. Candidate: Arien Eersten (Ernstensz) van Oostrum, m. 1649 (Utrecht /
  IJsselstein) and 26-5-1661 Lopikerkapel (`6ED1`), burial records Lopik 1723.

Next steps:
1. Find Huijbert's burial (MyHeritage: 1792) in the Lopik/Jaarsveld burial books, with age: decides 1695 vs 1717.
2. Burial of the 1695 Huijbert as a child (Lopik begraafboek, ca. 1695–1717).
3. Notarial records Lopik (Het Utrechts Archief, notarissen): estate of Jan Ariensz van Oostrum, guardianship of his
   children 1709 (remarriage of a widower with minor children needed a "boedelscheiding").
4. Marriage Huijbert × Ariaentje Boef (ca. 1740–1747): not found in Lopikerkapel; try Jaarsveld, Benschop, Polsbroek,
   IJsselstein, and the Boef family.

## MyHeritage tree (Sonja Oosterom + Florian Hillen)

Profiles (open with `python scripts/mh_profiel.py <id>` in the debug Chrome; the user is logged in, but not a member
of the site, so living/recent people are "Privé"):
- 1500004 Arie Oosterom 1908–1988, 1500008 Pieter 1875, 1500025 Teunis 1847–1915, 1500229 Arie 1801–1881.
- The user pasted the older ones (no ids): Arien Ariensz van Oostrum ca. 1660 (8 gen.), Huijbert Janszn van Oostrum
  25-7-1717 – 1792 (7 gen., listed as his own father: error in the tree), Teunis Huibertsz 5-12-1762 – ca. 1830 (6 gen.).
- The tree lists children of Teunis × Geertje Dekker as: Willemijntje 1789–1813, Teunis 1791–1826, Huibert 1792–1863,
  Gerrit 1797–1846, Magteltje 1800, Arie 1801–1881, Willempje 1803, Jacobus 1805–1886, Geertje 1808–1881,
  Teuntje 1809–1837. Baptism records differ: Willemijntje 21-9-1788, Teunis 27-12-1789, Arie 1795 and Arie 1799 (both
  missing in MyHeritage), Willempje 1-1-1804, Geertje 12-4-1807, Teuntje 18-12-1808. Magteltje and Jacobus: no
  baptism found yet (not on the site).
- Navigating the tree view by clicking is unreliable (cards move while the tree animates). Use the profile URLs:
  `https://www.myheritage.nl/profile-OYYV6RLFE43U2DPKEJO6ILZTOTT5LPI-<id>/x`. Family members on a profile page are not
  `<a>` links, so their ids cannot be read from the page; ask the user for profile links.

## Searched without result
- Open Archieven "Oosterom & Lekkerkerker 1870": the 1870 Benschop marriage of Teunis × Adriana Cornelia is not found.
- "Huibert Jansz van Oostrum": nothing (the records use "Huijbert Janse" or no patronymic).
- "Huijbert van Oostrum & Boef": only the 1748 baptism and the 1751 banns, no first marriage.

## Contradictions
- MyHeritage gives Arie (1801) a baptism at Jaarsvelderkapel; the record says Lopikerkapel.
- Teunis (b. 1789): MyHeritage says 1791–1826. The baptism is 27-12-1789; a Teunis Teunisz Oosterom died in Jaarsveld
  20-8-1826 (`hua:3DBB6D70-…`), probably him.

## Round 2 (2026-10-01): attack on the wall

New facts on Huijbert (all Lopikerkapel church books, Het Utrechts Archief L158):
- Banns 15-2-1748, married 3-3-1748: "Huybert Janse Oostrum wonende onder Jaerselderkapel en Arijaentie Boef wonende
  te Lopik" (`AFA3`, scan read: no "j.m." and no parents). Daughter Geertruij baptised 31-3-1748, four weeks later.
- Burials: "vrouw van Huijbert van Oostrum" 15-12-1749 (`B190`), "kind van Huijbert van Oostrum" 3-1-1750 (`B18C`),
  "Willemijntje Jaarsveld, vrouw van Huijbert Oostrum" 27-12-1764 (`B222`).
- 20-12-1771 notary J. Boomhoff Jansz (Utrecht): Huybert van Oostrum, living in Jaarsveld, guarantor for Jan de With
  renting from Magdalena Colombier (`hua:609C5BC0-CC36-4642-E053-4701000A17FD`).
- Burial 4-12-1792 (`B2A6`, scan read, register folio 197): "in de kerk in een huurgraf 't lyk van Huibert Oostrum,
  komt voor de kerk met 2 uur luyden, kleed, onder Jaarsv. Capel", fee f 4-13. **No age.** Second register (`70EE`,
  folio 7) only "J.4 Dec. H. Oosterom".

Evidence that Huijbert = the 1717 son of Jan Ariensz × Geertje Gerrits (van Beusekom), still circumstantial:
- Jan Ariensz reused names only after a child died: Arien 1694 → Arie 1712 (buried 25-10-1735 as "Arien, zoon van
  Jan Ariensz", `B11C`); Grietie 1704 → Grietie 1710; Huijbert 1695 → Huijbert 1717. So the 1695 Huijbert probably
  died young. Other children of Jan: twins Jan and Hendrik 1696, Hendrik 1697, twins Jan and Willem 1699, Aeltie 1701,
  Dirkie 1715, Jacobus 1718, Theunis 1721 (buried 15-3-1736 as son of Jan Arienz, `B118`), Aefje 1723.
  Checked (`AC56`, `AC5E`, `AC63`, `AC7D`): all 1696–1699 children have mother Lijsbeth Huijberts, so the reuse
  pattern holds four more times (Jan 1696 → 1699, Hendrik 1696 → 1697).
- Huijbert's children are named Geertruij (his mother Geertje?), Gerrigje (Gerrit, her father?), Willem, Arie (Jan's
  father Arien?), Dirkje (Jan's daughter Dirkie 1715) and Teunis (Jan's son Theunis 1721). Fits the 1717 family.
- Jan Ariensz van Oostrum was buried in Lopikerkapel on 8-2-1753 (`B1AB`, "Jan Arienze Oostrum").
- Other Jans van Oostrum around: Jan Ersten (buried Lopik 19-8-1748, `D093`), Jan Aertse (partner buried 1767),
  Jan Janse (wife Aaltjen van Rooijen buried Lopik 1727). So "Huijbert Janse" alone does not prove the link.

Dead ends this round:
- Woerden burial 1-8-1707 "Huybert Oostrum" (`hua:5329E09D-AD71-…`, scan read): an adult-style entry (3-guilder class),
  not "kind van". Woerden had its own Oostrum family (Claas, Aart, Gijsbert). Not ours.
- Nijmegen 1714/1716 "Huybert van Oostrum" × Christina Mol: different man (dead by 1716).
- 1704 notary J. Both: "Jan Ariensz Oostrum woont Lageweyde" (near Woerden). Unclear if ours.
- Notarial index Utrecht 1705–1712 and 1748–1756 under "Oostrum": no estate of Jan Ariensz or Lijsbeth Huijberts.
  The village courts of Lopik/Jaarsveld (weeskamer, boedels) are not indexed online.

Jan Ariensz's own father (for later): his first son is Arien (1694), so his father was an Arien. Candidates:
Arien Eersten (Ernstensz) van Oostrum, corn merchant in Utrecht (notary 1668), m. 1) 1649 Trijntgen van Suijlen
(IJsselstein/Utrecht), 2) 26-5-1661 Lopikerkapel Grietjen Klaes Blom (`6ED1`). Jan named a daughter Grietie (1704),
which would fit Grietjen Blom. Other children of an Arien in Lopik: Eerst Ariensz (m. 1690 Marrigjen Donker), Thomas
Ariensz (m. 1692 Lijsbet Donker), Aefie Ariense (m. 1698 Hendrick Fooijert). Arien Ersten's wife buried Lopik
22-12-1723 (`A4C3`). All unproven.

Tricks that worked:
- `scripts/oa_plaats.py Oostrum Lopikerkapel -doop`: every record of a surname in one parish (API parameter
  `eventplace` works; `eventtype` returns 0).
- Scans: Open Archieven gives `https://proxy.archieven.nl/download/39/<GUID>` for some burial books (full size, curl
  works). For others the Utrechts Archief viewer URL works in the debug Chrome; the thumbnail URLs on that page accept
  `&format=large` (1024 px) with curl.

Next steps:
1. Village court archives of Jaarsveld and Lopik (Het Utrechts Archief): boedel/voogdij after Ariaentje Boef's death
   (1749/1750, minor child Geertruij) and after Jan Ariensz's death (1753). See `op-te-vragen.md`.
2. Lidmaten (church members) register of Lopikerkapel/Jaarsveld: may list "Huijbert Jansz van Oostrum" with origin.
3. 1870 Benschop marriage deed of Teunis × Adriana Cornelia Lekkerkerker.

## Round 3 (2026-10-01): tree complete, professions, origins

Tree filled (64 persons): all baptisms of Teunis × Geertje Dekker (14 children incl. Arie 1795, Arie 1796, Magteltje
1791 and 1800, Jacobus ca. 1805 from his 1834 marriage), Arie × Elisabeth Kooiman (8 incl. stillborn 1832, Teunis
1835–1836), Teunis × Adriana Cornelia Lekkerkerker (19 children 1871–1895, 8 died as babies; spelled "Oostrom").
Marriages of the 1762-family children read: Teunis 1815 × Geertrui Streef (d. 1826), Huibert 1819 × Zwaantje 't Lam,
Gerrit 1821 × Lysbeth Jaarsveld, Magteltje 1824 × Gijsbert Oskam, Teuntje 1833 × Ernst Oskam, Jacobus 1834 × Margaretha
Verbaan. Willemijntje (1788) had a son Arie in 1803 with no father named (`AF4C`); a Johannes Oosterom bapt. 1807 has
parents Thomas Oosterom × Willemijntje Oosterom (`AF6A`), maybe her later husband (not checked).

Professions, read from scans:
- 1830 marriage Willige Langerak (act 1, scan `proxy.archieven.nl/download/39/609C5C737C244642E0534701000A17FD`):
  Arie Oosterom, **schipper**, 29, born and living Jaarsveld; father Teunis Oosterom **schipper**; Geertje Dekker
  zonder beroep. Bride's father Hendrik Kooiman bouwman (could not write); mother Adriana Hooglander deceased.
  Witnesses: Gijsbert Oskam dagloner 31 (brother-in-law), **Cornelis Oosterom bouwman 24, Jaarsveld, brother of the
  groom** (no baptism found; maybe = Jacobus?), Jacob Schep bouwman 40, Jan Kooiman bouwman 21.
- 1835 birth Zuid-Polsbroek act 2 (scan `…609C5C6BCFAC…`): Arie Oosterom 33 **bouwman**; Elizabeth Kooijman 23
  **landbouwster**; Arie signs.
- 1875 birth Polsbroek act 17 (scan `…609C5C6C4E6B…`): Teunis Oosterom 28 **landbouwer**, house wijk ? nr 33;
  witness Joris van der Heiden landbouwer 38; Teunis signs "T. Oosterom".
- 1881 death Polsbroek act 18 (scan `…609C5C747758…`): Arie Oosterom, 80, zonder beroep, born Lopik, died house
  nr 57; informants did not know his parents.
- Pieter: landbouwer / bouwman (Bergambacht birth records 1909–1923, index).

Origins (probable, notes only, not in the tree):
- Name: from Oostrum (Osterhem), a former hamlet near Houten (Wikipedia "Van Oostrum").
- Arien Eersten (Aersten) van Oostrum m. 26-5-1661 Lopikerkapel Grietjen Klaes Blom (`6ED1`, also `7547` Lopik).
  Children found: Aerst Ariensz bapt. 27-3-1664 Lopik (`7320`, father "Arien Aersten"), Marrichje Eersten bapt.
  4-10-1674 Lopikerkapel (`AB87`). Lopik/Lopikerkapel baptisms 1655–1690 are indexed, but children are often listed
  by patronymic only and the mother as N.N.; Jan (ca. 1661–1663) not found.
- Genealogie Online "Stamboom Ammerlaan" (no sources): Arien × Grietje Blom children Jan 1661, Jacob 1664, Maayken
  1667, Eerst 1670, Thomas 1671, Claasje 1672, Marrichgen 1674, Pieter ±1676; Arien son of Eerst (Ernst) Adriaensz
  van Oostrum (±1600–±1640, Lopikerkapel/Lopikerveld) × Theuntgen Gijsbertsdr; Eerst son of Adriaan Jansz van Oostrum
  (±1576–±1630, Bunnik) × Annichje Cornelisdr; he son of Jan Adriaansz (±1545–±1586) × Marrichgen Ernstendr Schaik.
  URLs: genealogieonline.nl/en/stamboom-ammerlaan/I378.php, I389.php, I391.php. Unsourced; conflicts: the records
  give Aerst 1664 (not Eerst 1670).
- A different, wealthier Utrecht branch: Ernst (Eerst) Jansz van Oostrum (notarial 1617–1651, dead by 1645 per one
  deed), sons Adriaen/Arien Eersten (corn merchant Utrecht, m. 1644 and 1649), Jan Eerstensz (m. 1653), Cornelis,
  Thomas Eersten. Not proven to be the same Arien as the 1661 Lopikerkapel groom.

Site: index.html rewritten (schippers → boeren; origin section; photos of Lek 1745, Jaarsveld (Almeloveen),
Polsbroek (Schoemaker), Willige Langerak church 1840, Bergambacht church, old farm Polsbroek; scan excerpts 1748,
1792, 1830, 1835, 1875 in assets/img/scans/).

Tricks: `scripts/scan_sheet.py` makes a contact sheet of consecutive proxy.archieven.nl pages (GUIDs are sequential
within a register; the record's own GUID is often the cover/first page, so step forward to the act). `scan_get.py`
downloads one page. `oa_ref.py` prints book, act number and scan GUID.

Next steps:
1. Lopik/Lopikerkapel baptism scans 1661–1663 (Jan Ariensz) page by page in the HUA viewer.
2. Benschop 1870 marriage (not indexed): browse the Benschop 1870 marriage register scans.
3. Bergambacht: where Pieter's farm stood (bevolkingsregister Bergambacht 1900–1940, Streekarchief Midden-Holland).
4. Jaarsveld schippers: any notarial or "veer" records about Teunis van Oostrum as skipper.

## JohnOoms.nl "Geslacht Van Oostrum" (checked 2026-10-01)

URL: https://johnooms.nl/genealogieen/van-oostrum/ (text saved in raw/johnooms.txt). Secondary source, partly
sourced via Genealogie Online. It follows the Houten/'t Goy family (hofstede Oostrum, knapen, Wickenburgh) from
Hendrik van Oistrum (ca. 1275) through Van Schayck descendants to:
- 8. Adriaan Jansz van Oostrum (1505–1576, Houten) × Lijsbeth Stevensdr van Schayck (1540)
- 9. Jan Adriaansz (1545–1586) × Marrichgen Eerstens Jacobsdr van Schaijck (1575)
- 10. Adriaan Jansz (1576–1630, Bunnik) × Annichjen Cornelisdr (1595)
- 11. Ernst Gerrit Adriaansz (ca. 1610 Lopikerkapel – 1639) × Theuntgen Ghijsbertsdr, m. 25-5-1630 Jaarsveld
- 12. **Arie Ernsts van Oostrum** (ca. 1635 – ca. 1706 Lopikerkapel) × Grietje Claasdr Blom (b. 1640 Lopik, dau. of
  Claas Bastiaans Blom and Adriaantje Thomasdr Pellen), m. 26-5-1661 Lopik. **"In 1699 was hij burgemeester van
  Jaarsveld."** Children: Maaike, Ernst (bapt. 20-1-1670 Meerkerk, m. 1690 Marrigje Jans Doncker), Claasje, Thomas,
  Marrigje, Pieter (m. 1699 Jaarsveld, d. 1747), Aaltje, Adriaan, Jacob, **Jan Ariens van Oostrum** (not followed
  further on the site).
- Site continues with Ernst's and Pieter's lines (Van der Velden, Graafland, Stigter), not with Jan.

Assessment: same family as ours one generation above Jan Ariensz. Jan Ariens is listed as a child of Arie Ernsts ×
Grietje Blom, which supports our probable link. Our own line (Jan → Huijbert → Teunis …) is not on the site.
Checked on Open Archieven: Jaarsveld marriages of the siblings exist (Aaltjen Ariendr 1680, Jacob Arienz 1691, Maagje
Adriaens 1693, Claasje 1698, Pieter Arijenz 1699), and Lopik ones (Eerst 1690, Thomas 1692, Jan 1693). Ooms's
"Ernst bapt. 1670 Meerkerk" conflicts with the Lopik baptism of Aerst Ariensz 27-3-1664 (maybe two sons).
The 1630 Jaarsveld marriage of Ernst × Theuntgen is not on Open Archieven; generations 1–10 are older secondary work.
Leads: "burgemeester van Jaarsveld 1699" (Jaarsveld court/village archive), Genealogie Blom II on the same site.

## Round 4 (2026-10-01): testing the link to Arien Ernsten (JohnOoms.nl)

Positive evidence for Huijbert ← Jan Ariensz:
- Baptism 28-1-1694 (Lopikerkapel book 197, scan `609C5C950F24…`, read): "Jaarsvelderkapel 4. Den 28 januari 1694
  een kind gedoopt van Jan Ariense van Oostrum, **schipper**, ende Lysabeth Hijberts sijn vrouw, een soon zynde, de
  naem van 't kind is Arien."
- Baptism 25-7-1717 (scan `609C5C950F2F…`, read): "Jaarsvelderkapel 224. Den 25 juli een kind gedoopt van Jan Ariense
  van Oostrum en Geertie Gerritse syn vrouw, een soon, de name van 't kind is Huibert." No witnesses in this register.
- Marriage 2-4-1693 (scan `609C5C950EF0…`, read): "Den 2 april 1693 hebben gehad haer drie geboden Jan Adriaense van
  Oostrum met Lysbet Huijberts, en zijn alhier getrout." No origin given.
- Elimination: all Huijbert/Huybert/Hubert + Oostrum/Oosterom/Oostrom baptisms 1680–1735 on Open Archieven: Woerden
  1687 (son of Boudewijn; buried 1707), Lopikerkapel 1695 and 1717 (both sons of Jan Ariensz), Amsterdam family. So
  "Huybert Janse Oostrum wonende onder Jaarsvelderkapel" (1748) can only be a son of Jan Ariensz.
- Jan's children re-use names: Arien 1694/1712, Jan 1696/1699, Hendrik 1696/1697, Aeltie 1701/1702, Grietie
  1704/1710, Huijbert 1695/1717. Jan Ariensz was a skipper, like Teunis (1762) and Arie (1801).
- All Jan Ariensz/Ariense/Adriaense van Oostrum records found are this one man (Lopikerkapel 1693–1723); a "Jan
  Ariensz Oostrum woont Lageweyde" (near Woerden) in a 1704 deed of notary J. Both is unclear.

Disproof of Jan Ariensz ← Arien Ernsten van Oostrum × Grietje Claesdr Blom (JohnOoms.nl, Ammerlaan):
- vanoostrum.info (Person 226, sourced) summarises Weeskamer Jaarsveld inv. 272/473, 1-11-1706: inventory by Grietge
  Claesse Blom, widow of Arijen Ernsten van Oostrum, buurmeester of Jaarsveld; no testament; **"Zij hebben 6 kinderen
  in leven en meerderjarig: Tomas, Maechie, Ernst, Claesje, Marrchje en Pieter Arijense van Oostrum."** Settlement
  10-11-1706 with the same six. Our Jan was alive (children 1704, 1710) and is not named. So he was not their son
  (unless the summary is wrong: check the original weeskamer act).
- Same site: Arien Ernsten lived 1667 in Meerkerk, 1673 confession, lived "bij 't Klapheck op Peter Hoppens oven",
  schepen of Jaarsveld 1695–1705, regent of the Vijfhoeven 1698; buried 1706 Jaarsveld. Ernst bapt. 20-1-1670
  Meerkerk; Thomas b. 1665 Jaarsveld. Inventory: 49 cheeses, cows, butter, f 687 cash, leased farm of 20 morgen from
  Mr. Gerrart Emans. A nice story for a side line, but not ours.
- Lopik baptisms 1660–1663 read page by page (book 36 scans `686699F87B1F…`, `…7B20…`, `…7B21…`): no son of Arien
  Aertsen/Eersten except Aert (Eerst) 27-3-1664.
- Jaarsveld 1691 groom "Jacob Arienz van Oostrum" (index) is "Jacob van Oostrum, woont Ameijde" × Aagje Pijl, also not
  an heir in 1706. Aaltjen van Oostrum × Harmen Verweij (Jaarsveld 1680) also not an heir.

New candidate for Jan's parents:
- Notary F. van Ewyck de Jonge (Utrecht, U034a4 inv. 817 nr 71), 30-1-1682: testament of Hendrickje Cornelis,
  "woont de Vaert", heirs her children with the late **Arien Hendrickss van Oostrum**: Cornelis, Maeyghje, **Jan**,
  Hendrick and Cornelia Arissen van Oostrum (`hua:609C5BC6-732E-4642-E053-4701000A17FD`; scan is a PDF, bitonal,
  hard to read). "de Vaert" also occurs in the Jaarsvelderkapel baptism book 1693–1694 ("woonende ontrent de vaert op
  de Steenoven"). Jan named two sons Hendrik. Not proven; no son Cornelis or daughter Hendrickje/Cornelia among Jan's
  children, which is a point against.

Next steps:
1. Original weeskamer Jaarsveld 272/473 (1706) at Het Utrechts Archief: confirm the six heirs.
2. Read the 1682 testament properly (request a better scan or view at the archive).
3. Search Arien Hendricksz van Oostrum × Hendrickje Cornelis: marriage (ca. 1660–1675) and children's baptisms
   (Jaarsveld church books before 1690 are not indexed online; Lopik/Lopikerkapel indexed but sparse).
4. Burial of Jan Ariensz 1753 and of Geertje van Beusekom; any Jaarsveld court records (ORA) naming Huijbert Jansz.

## Round 5 (2026-10-01): how is Jan Ariensz related to the Van Oostrum families?

- vanoostrum.info (mail@vanoostrum.info; Aldfaer trees, sourced from DTB, ORA Jaarsveld, weeskamer) has a separate
  tree "Stamboom van Huybert van Oostrum" (index title "van Oostrum alias Smetser", raw/vo/Huybert.html). Root is our
  Huybert (bapt. 25-7-1717 Lopikerkapel, buried 4-12-1792; x1 1748 Adriaentgen Boef, x2 1751 Willempgen van Jaersvelt,
  b. 30-8-1727 Lopikerkapel). Children there: **Jan van Oostrum 1751–1812** (not on our site yet; probably the Jan who
  m. 1776 Joosje Kortleven and whose child was buried 1786 as "kind van Jan Huijbertz") and Arie 1756–1841 (Ruwiel,
  x 1787 Engeltje Kool). They do NOT give Huybert's parents: that researcher hit the same wall.
- 1709 banns (scan read): "Jan Ariense van Oostrum weduwenaer van Lysbeth Huijbertse en Geertie Gerritse van
  Beusekom beyde woonende alhier" (Lopikerkapel). A Hendrik Gerritse van Beusekom j.m. married there in Oct 1709.
- Candidate ruled out: Adriaen (Arien) Henricksz van Oostrum × Henrickjen Cornelis, Vreeswijk (m. 1632). Children
  bapt. Vreeswijk: Teunis 1635, Cornelis 1637, Maeijchjen 1640, **Jan 1643**, Henrick 1646, Cornelisjen 1654. This is
  the family of the 1682 will. That Jan (b. 1643) cannot be ours (our Jan had children until 1723).
- Candidate open: Arien Teunissen van Oostrum × Lijsbet Henricx van Es, m. 21-1-1671 Utrecht
  (`hua:1117A373-DDE3-…`). Fits names (Jan's sons Theunis 1721 and Hendrik 1696/1697) and age (Jan b. ~1671–72,
  m. 1693). No children's baptisms found on Open Archieven (Utrecht city or villages). Arien Teunissen could be a
  grandson of Adriaen Henricksz (his son Teunis b. 1635) – speculative.
- Jaarsveld baptisms before ~1700 are not on Open Archieven. Book 131 (Jaarsveld NH dopen) is a later family register
  (18th c., alphabetical; O on pp. 59–60: Oosterom Willem × Beligje den Uijl, children 1779–1786). No help for 1665–72.
- Conclusion so far: our line is NOT the line on JohnOoms.nl (Arien Ernsten). A common ancestor further back (Houten
  / Lopikerwaard Van Oostrums, 16th–17th c.) is likely but unproven.

Next steps:
1. Email mail@vanoostrum.info: share Jan Ariensz (schipper, 1694) and ask whether ORA/weeskamer Jaarsveld or Lopik
   mention Jan Ariensz van Oostrum or his father.
2. Arien Teunissen van Oostrum: Utrecht notarial index and Lopik/Jaarsveld court records; burial; children.
3. ORA Jaarsveld / Lopik (Het Utrechts Archief): transports of land or boats by Jan Ariensz van Oostrum, schipper.
