## Round 13 (2026-10-02): photos rule, Polsbroek farms, notary records

User rule: no photos of houses/farms that did not belong to the Oosteroms (removed: Lopikerweg Oost 146 "1805",
Polsbroek Commons farm, Street View of Kapelsepad – the old farmhouse next to A149 stands on Jaarsveld A131
"huis en plaats", owner 1832 Gerrit Spruitenburg, so not Teunis's).

Found (Polsbroek):
- Utrechtsche Courant 28-1-1839 (and 1-3-1839, Opregte Haarlemsche Courant 28-2-1839): notary mr C.G. de Balbian van
  Doorn, Jutphaas, sells on 5-3-1839 "eene Hofstede met Woonhuis, Zomerhuis, Stalling, Braakhut, Hooiberg en ruim 28
  Bunders ... onder Zuid-Polsbroek, Sectie A. No. 570 tot en met 607 en 641 tot en met 655 ... bij den Huurder
  A. OOSTEROM te Zuid-Polsbroek"; information from A.C. Schaly, Nieuwenstein, Jutphaas. Delpher urn
  ddd:010807112:mpeg21:a0018 (page p004; image crop in assets/img/scans/advertentie1839.jpg).
- OAT 1832 Zuid-Polsbroek (HisGIS municipality name "Zuid-Polsbroek", OAT06058A020–A023): A570–582 owner "Graaff,
  Cornelia Maria de, Amsterdam" (De Graeff, lords of Zuid-Polsbroek); A580 "huis en erf". A580 = today Zuidzijdseweg
  142, Polsbroek (BAG pand bouwjaar 1888; thatched farmhouse). Notarial index: purchase deed 2-5-1839 (De Balbian van
  Doorn) referred to in 1880/1893 deeds.
- Notarial index RHC (Open Archieven `rel:`, full summaries in de index – use scripts/oa_not.py):
  * hypotheek 1-9-1880 (Y045 inv 2951 nr 7369): Arie Oosterom, zonder beroep te Polsbroek, borrows f 13.000 op een farm
    aan de Zuidzijde (refs 2-5-1839 en 23-12-1870 deeds).
  * testaments 4-1-1881 (Y045 inv 2954 nr 30 en 31): Arie en Elisabeth: vier farms in Polsbroek – Noordzijde (lived in
    by son Hendrik) → Hendrik; Noordzijde (lived in by son Teunis) → daughter Adriana × Krijn Kok; Zuidzijde → Teuntje ×
    C.L. van den Ham; "Zuidzijde 48" → son Teunis, bouwman. Executor Antonie van Kippersluis.
  * Elisabeth's testament 21-6-1880 (L156 inv 1159 nr 8051).
  * 1893 inventaris/veiling/scheiding (see round 12). Newspapers: Utrechtsch Prov. en Sted. Dagblad 6-9 en 26-9-1893
    (ad), Het nieuwe dagblad voor Utrecht 6-10-1893 (result): farm 8.4970 ha Noordzijde + 3.2435 ha Zuidzijde (used by
    Hendrik) bought by Krijn Kok for f 16.600; farm 15.8795 ha Zuidzijde (used by Krijn Kok) bought by P. de Pater, Vlist,
    for f 29.000.
  * 27-5-1879 (O063 inv 2036 nr 1015): Teunis Oostrom en Gerrit van der Heeden, landbouwers te Polsbroek, board members
    of de "Algemene Gereformeerde of Grote Armen van Polsbroek" (chairman burgemeester J.A. van Buma).
  * 1892 (Y045 inv 2975 nr 1927, 1983): estate of Marrigje Heijcoop van Os, widow of Pieter Lekkerkerker (Adriana
    Cornelia's parents); heirs incl. Teunis Oostrom, bouwman te Polsbroek; their farm (Benedeneind, Benschop) sold for
    f 38.000 to Scheltus Schouten.
- Not ours (side lines, noted): Maria van der Werken wid. Willem van Oosterom (Zwaantje, Lopik, 1892); Jan Oosterom
  d. 1894 Jaarsveld; Teunis Oosterom kastelein Het Zwaantje (d. 1898); Jacobus Oosterom d. 1886 Jaarsveld.

Name question – notary records Lopik (RHC L156):
- Inv. 1112 (protocol van notary Bijlandt, ca. 1645–1664, 158 scans) heeft een alfabetisch register (scans 145–157,
  by first name of de first party). Read A, C, G, H/J, M: geen Smetser, geen Van Oostrum, geen Arien/Adriaen Adriaensz
  of Cornelisz. (Alleen first parties zijn indexed.)
- Inv. 1111 (1609–1645?, 289 scans): geen register; being downloaded for page-by-page reading (raw/rhc/all1111).
  2026-10-02: resumed download timed out again at scan 19 (same RHC rate-limit as below). Scans 0000–0018 present.
  User said stop for now; resume later with longer --sleep (e.g. 60s) or try the tile route.
- Woerden notarial index (rel) 1585–1700: Van Oostrums there are other families (jhr Jan van Oostrum 1585, Jacob Jansz
  Oostrum Montfoort/Woerden, Thomas Eerstensz family 1697 Montfoort). Geen Smetser van Jaarsveld; Smetsers in Woerden
  zijn de Jan Jansz family.
- Delpher: 'Smetser AND (Jaarsveld OR Lopik OR Oostrum)' 0 hits.

Tools added: scripts/oa_not.py (deed summaries), scripts/oa_arch.py (one archive + period), scripts/delpher.py en
delpher_text.py (KB SRU search en OCR text; page image via resolver urn ...:pNNN:image, ALTO via ...:pNNN:alto),
scripts/rhc_scan.py (RHC scans; `id` mode by bestand_id is reliable, `get` by list index; ~30 s per full scan).
- Inv. 1111 is "Register van testamenten" van de Lopik notary, 1609–1646 (title page scan 1), 289 scans, geen index;
  each testament starts with a heading ("Testament van ..."). Scans 0–14 downloaded (raw/rhc/all1111): testament of
  heer Johan vander Berch, domdeken Utrecht (1609). After ~70 full-size downloads in total the RHC image server started
  timing out (2026-10-02 ~12:45), so bulk downloading was stopped. Faster route found: the viewer's tile request
  `afbeelding.img?...&ACTION=maketile&t_width=..&t_height=..&t_offsetx=..&t_offsety=..&scalesize=..` (not yet tested
  voor a whole page at reduced scale). Ask the user before resuming (bulk download), go slowly (one scan per 30 s).
- Sheets for reading: scripts/sheet.py DIR FROM TO (4 pages per sheet, headings readable at 1000 px).
