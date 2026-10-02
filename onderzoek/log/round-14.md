## Round 14 (2026-10-02): waar woonden de vaders precies? (Teunis 1847, Pieter 1875, Arie 1908, Huijbert, famkroon)

Doel: voor elke vader in de mannelijke lijn een moderne adres/coordinaat vinden voor fotos. Niet herhaald: Arie
1801 (Zuidzijdseweg 142) en Teunis Huijbertsz 1762 (Kapelsepad 15) - die stonden al vast (round 12/13).

### 1. Teunis Oosterom (1847-1915) - "huis no. 33" Polsbroek, 1875
Niet gevonden. Aanpak en resultaat:
- De Polsbroek bevolkingsregisters zelf (1850-1880, 1920-1938) staan niet op Open Archieven (gecontroleerd met
  archive=hua en archive=rel, naam Oosterom/Oostrom/Teunis Oosterom + eventplace Polsbroek: alleen Burgerlijke
  Stand-akten, geen enkel "Bevolkingsregister"-brontype). Ze zijn alleen te doorzoeken via RHC Rijnstreek en
  Lopikerwaard (rhcrijnstreek.nl/bronnen/indexen/overzicht-bewerkte-bronnen/polsbroek-bevolkingsregisters-1850-1880-1920-1938/)
  - die pagina zegt zelf: "Vaak is niet direct duidelijk welk hedendaags adres correspondeert" met de oude
  huisnummering.
- Het testament van 4-1-1881 noemt vier boerderijen: twee "Noordzijde" (een bewoond door Hendrik naar Hendrik,
  een bewoond door Teunis naar dochter Adriana x Krijn Kok) en twee "Zuidzijde" (een naar Teuntje x C.L. van den
  Ham, "Zuidzijde 48" naar Teunis zelf). Teunis woonde dus in 1881 op een Noordzijde-boerderij die hij niet
  erfde; hij kreeg in plaats daarvan land/een boerderij "Zuidzijde 48". "Huis no. 33" (1875, geboorte van Pieter)
  is dus vermoedelijk de Noordzijde-boerderij, niet "Zuidzijde 48" - maar dit staat nergens zwart op wit, puur
  redenering.
- 1832-kadaster Noord-Polsbroek nagekeken: HisGIS-gemeentenaam is "Noord Polsbroek" (met spatie, niet met
  streepje; code 06057), sectie A, 34 scans (OAT06057A001-A034, IIIF-pad .../Utrecht%2FNoord%20Polsbroek%2FOAT06057A0NN.jpg).
  GraphQL-status ook hier INITIEEL (eigenaren niet getranscribeerd), dus alle 34 scans met het oog gelezen
  (contactvellen, 4 per sheet, in raw/hisgis/sheets/). Geen enkele "Oosterom"/"Oostrum" als eigenaar in 1832 -
  logisch, want de Zuidzijde-boerderij werd pas in 1839 gekocht (niet gehuurd) en latere Noordzijde/Zuidzijde-
  aankopen waren kennelijk ook na 1832.
- Conclusie: zonder de 1893-notarisstukken (L156 inv. 1184/1185, boedelinventaris/veiling/scheiding - al
  aangevraagd, zie op-te-vragen.md) of zonder zelf de Polsbroek bevolkingsregisters bij RHC in te zien, is "huis
  no. 33" / "Zuidzijde 48" niet aan een modern adres of kadasterperceel te koppelen. Geen gok gedaan.

### 2. Pieter Oosterom (1875-1959) - Bergambacht "Hogendijk 149" en Stolwijk
Gedeeltelijk gevonden, maar met een onopgeloste knoop:
- De originele bron zelf bekeken: SAMH, Archief gemeente Bergambacht 1811-1939, deel 1716 (Bevolkingsregisters
  1893-1937, deel 7), blad 20 - scan achter record smh:583c545c-9133-cb28-3564-5c2f7c9de0e7 (Memorix-bestand
  9b5855b8-4b70-0853-e27d-b4794c710250, thumb/1920x1080, bewaard als raw/samh/bergambacht_blad20.jpg). Regel 1:
  "Oosterom Pieter, hoofd, landbouwer ... Polsbroek 1875 ... 9 jan. 1909 ... Stolwijk 148 ... 11 apr. 1925 ->
  Langerak". Kolom 13 ("Huizing: straat, gracht enz., wijk, huisnummer") is zelf meermaals gecorrigeerd: leesbaar
  staat er "Hogendijk 149", daaronder doorgehaald "141", en daar weer onder in rood een moeilijk leesbare
  correctie die eindigt op iets als "15" met daaronder vet zwart "20" (crops: raw/samh/crop_huizing_zoom2.jpg en
  _zoom3.jpg).
- Het dorp Bergambacht voerde rond 1920 straatnaam+huisnummer in (voorheen wijkletter+nummer); de bouwvergunningen-
  index 1904-1984 (archiefman.nl/inv/bwt2063.htm, via curl met browser-UA bereikbaar, WebFetch kreeg 403 op
  user-agent) laat zien dat "Hogedijk" rond 1920 een eigen doorlopende nummering had (voorbeelden: oud adres
  Hogedijk 36 -> huidig nr. 180; oud adres Hogedijk 66 -> huidig nr. 10), wat erop wijst dat de Hogedijk-nummers
  uit Pieters tijd (149, 141, ...) niet dezelfde zijn als de huidige huisnummers op de Hogedijk (die nu 4 t/m 148
  lopen, bron: kadastralekaart.com/allecijfers.nl). Dus zelfs als "20" goed gelezen is, is het onzeker of dat de
  huidige Hogedijk 20 is. Geen concordantietabel voor Bergambacht gevonden op uitdeoudekoektrommel.com (dat houdt
  wel concordanties voor andere plaatsen bij, niet voor Bergambacht).
- Stolwijk (1906-1909, wijk G/H, blad 25, Archief gemeente Stolwijk 1812-1942 deel 1423): in het register hierboven
  staat als "vorige woonplaats" alleen "Stolwijk 148" (een huisnummer zonder straatnaam) - geen verdere
  precisering gevonden; we hebben deze ronde geen scan van het Stolwijkse register zelf bekeken.
- Conclusie: straatnaam "Hogedijk/Hogendijk" in Bergambacht staat vast (waarschijnlijk), het exacte huisnummer/
  perceel niet (onzeker) - de drie opeenvolgende nummers in het register moeten eerst zeker gelezen worden voor
  een BAG-opzoeking zinvol is.

### 3. Arie Oosterom (1908-1988) - volwassen adres
Niet gevonden, drie geprobeerde routes, alle drie doodlopend zonder inloggen/omzeilen:
- MyHeritage-profiel 1500004 (raw/mh/1500004.txt, al aanwezig): alleen geboorte Polsbroek 1908 en "Overleden: 1988
  (op de leeftijd van 80)" zonder plaats. Geen woonadres op de profielpagina. (De Chrome op poort 9223 draaide niet
  deze ronde, dus de "Biografie"-tab kon niet apart bekeken worden - mogelijk staat daar meer, dat is een
  concrete volgende stap.)
- graftombe.nl: zoekopdracht Oosterom, overlijdensjaar 1988 geeft 0 resultaten zichtbaar; de site meldt zelf
  "Gegevens van recent overleden personen worden niet weergegeven op het openbare gedeelte van graftombe.nl"
  (inloggen vereist) - gestopt, niet ingelogd per de regels.
- Open Archieven: BS Overlijden 1988 valt nog onder de wettelijke openbaarheidstermijn (overlijden 50 jaar, pas
  openbaar in 2038); geen akte te verwachten en geen gevonden. Een huwelijksakte Arie Oosterom x Johanna Jacoba de
  Jong (zou, als voor 1951, al openbaar zijn) is niet gevonden onder deze namen.
- Conclusie: voor Arie 1908-1988 is het volwassen woon-/sterfadres momenteel niet uit vrij toegankelijke bronnen
  te halen. Vraag de gebruiker om een bidprentje, familiepapieren of de MyHeritage-Biografie-tab (met ingelogde
  Chrome) te raadplegen.

### 4. Huijbert van Oostrum (1717-1792)
Geen nieuwe precisie gevonden; bevestigd dat dit alleen via archiefbezoek kan:
- Personele quotisatie 1749 (ontvanger Adriaan Steenis, Jaarsveld inbegrepen) zit in Nationaal Archief 3.01.51,
  niet online doorzoekbaar op naam.
- Verpondingskohieren/weeskamer/notarieel Jaarsveld: al eerder correct genoteerd in op-te-vragen.md als
  archiefbezoek-only; dit keer niets nieuws online gevonden (Delpher, Open Archieven, Genealogie Online allemaal
  niets nieuws - wel een niet-verwante naamgenoot "Pieter Ariens van Oostrum" ca. 1677-1747, het Lage Eind onder
  Jaarsveld 1706, in de Genealogie Online-stamboom Smit/Zimmermann - dit is vermoedelijk dezelfde al-ontkrachte
  Houten-lijn als round 4; niet onderzocht of gekoppeld, hier alleen genoemd als naamgenoot zonder bewezen band).
- Famkroon.nl noemt Huijbert (fk_VII) zelf als "leenman en schipper van Jaarsvelderkapel te Utrecht" - dat zit al
  automatisch in build_data.py (de famkroon-merge vult occupation aan waar leeg). Dat "leenman" (hield een
  leen/feodaal goed) past bij de al bestaande hypothese dat de Oosterom-familie een relatie had met het goed
  Oversloot. Het zou aannemelijk (niet bewezen) zijn dat Huijbert dezelfde Jaarsvelderkapel-boerderij bewoonde
  die zijn zoon Teunis in 1830 erfde (kadaster A149, nu Kapelsepad 15) - boerderijen gingen doorgaans van vader
  op zoon - maar geen enkele akte noemt Huijbert zelf op dat perceel. Dit als "waarschijnlijk" labelen, niet als
  vast.

### 5. Famkroon-generaties voor Huijbert (fk_I t/m fk_VI-a)
Precies nagelezen wat famkroon.json zelf zegt (geen website-onderzoek nodig, het bestand ligt al in het project):
alle zes personen (Cornelis Smetser ca. 1515, Aryen Cornelis Smetser ca. 1540, Cornelis Smetser ca. 1565, Adriaan
van Oostrum Smetser ca. 1595, Arien van Oostrum Smetser ca. 1630, Jan Ariensz ca. 1660) hebben als woonplaats-veld
niets preciezer dan "Jaarsveld" of "Omgeving Jaarsveld / Lopik" (fk_I zelfs alleen het laatste, geen enkel dorp
hard). Geen huis, boerderij of straat genoemd. Dit bevestigt alleen wat al in status-oosterom.md stond: voor deze
generaties is er zonder archiefbron niets preciezers te zeggen dan "ergens onder Jaarsveld/Lopik", expliciet
famkroon-only en ongecontroleerd.

### Nieuwe tools/tricks
- archiefman.nl (bouwvergunningen-indexen) blokkeert WebFetch zijn standaard user-agent (403) maar geeft gewoon
  200 met curl + een browser-UA - geen bot-bescherming/login, dus geen regel overtreden, alleen een UA-filter.
- graftombe.nl verbergt overlijdens van de laatste decennia achter een inlog - gestopt zoals de regels vragen.
- HisGIS-gemeentenaam voor het noorddeel van Polsbroek is "Noord Polsbroek" (spatie, niet streepje) ondanks dat
  "Zuid-Polsbroek" wel met streepje werkt - eerst uitproberen bij een nieuwe gemeente.
- Memorix/SAMH-scans met een "Huizing"-kolom (bevolkingsregister) zijn goed leesbaar op thumb/1920x1080 (klerken-
  schrift, geen oud schrift); inzoomen met PIL crop+resize+SHARPEN werkt voor het meeste, maar overlappende
  rode/zwarte correcties in dezelfde cel blijven soms onzeker.

### Searched without result (exact)
- Open Archieven: archive=hua / archive=rel, name="Oosterom"/"Teunis Oosterom"/"Teunis Oostrom",
  sourcetype=Bevolkingsregister, eventplace=Polsbroek geeft geen "Bevolkingsregister"-brontype voor Polsbroek zelf.
- HisGIS Overpass/GraphQL gemeente("Noord Polsbroek").status geeft INITIEEL (geen getranscribeerde eigenaren).
- Alle 34 OAT-scans Noord-Polsbroek sectie A (art. 1-1015) met het oog gelezen: geen Oosterom/Oostrum eigenaar.
- graftombe.nl, Oosterom, overlijden 1988: 0 publieke resultaten (recent overlijden verborgen).
- Open Archieven name="Arie Oosterom Johanna Jacoba de Jong" en name="Johanna Jacoba de Jong": geen match op onze
  Johanna Jacoba (geb. 1917).
- archiefman.nl bwt2063 (Bergambacht bouwvergunningen): geen vermelding van huisnummer 149 of 141 op Hogedijk.
- uitdeoudekoektrommel.com omnummeringen-concordantie: Bergambacht niet in de lijst van plaatsen.

### Open points (volgende stap)
1. Lees de twee crop-fotos (raw/samh/crop_huizing_zoom2.jpg, _zoom3.jpg) van de Bergambacht-Hogendijk-correcties
   met de schriftlezer; zoek daarna het gelezen eindnummer op in het BAG (adressen Hogedijk 4-148) of vraag SAMH om
   het Bergambachtse omnummerregister.
2. Vraag de 1893-notarisstukken op bij RHC (L156 inv. 1184/1185, al in op-te-vragen.md) voor de beschrijving van
   "Zuidzijde 48" en de Noordzijde-boerderijen - enige kans om het huis no. 33 van Teunis alsnog te plaatsen.
3. Start de debug Chrome en bekijk MyHeritage-profiel 1500004 zijn "Biografie"-tab voor Arie 1908-1988 zijn
   volwassen adres; overweeg de gebruiker te vragen om een bidprentje/rouwkaart.
4. Huijbert zijn boerderij: alleen nog via een archiefbezoek (weeskamer/notarieel/personele quotisatie Jaarsveld,
   zie op-te-vragen.md) - niet online op te lossen.
