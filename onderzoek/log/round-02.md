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
