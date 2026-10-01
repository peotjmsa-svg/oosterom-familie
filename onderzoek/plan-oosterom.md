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
