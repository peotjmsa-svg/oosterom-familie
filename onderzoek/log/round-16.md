## Round 16 (2026-10-02): Teunis "huis no. 33" Polsbroek and Huijbert quotisatie Jaarsveld

Goal: push the two open leads from round 14/15 further online (no archive visit). Both questions resolved further
than before; one major new primary-source find for Teunis, one correction/precision for the quotisatie lead, and
one unresolved contradiction flagged.

### 1. Teunis Oosterom (1847-1915), huis no. 33 Polsbroek, 1875

RHC Rijnstreek index portal archief.rhcrijnstreek.nl is a real, usable, free-text searchable name
index for the Polsbroek bevolkingsregister. Round 14 only read the static descriptive page and concluded
it could only be searched in person; that undersold it.
Automated POST search (scripted, no session) is
blocked with HTTP 403 (classic CSRF/WAF behaviour on zoeken.php, treated as bot protection, not bypassed).
But normal interactive browsing via the project debug Chrome (same tool already used for MyHeritage/Street View
elsewhere in this project) works with no login and no block.
Using that, the following was found (PROVEN, primary source, not reasoning):

- L052 (Archief Gemeente Polsbroek), inv. 1132 "Bevolkingsregister Zuid-Polsbroek, 1850-1860", folio 10: both
  Arie Oosterom (b. 1801 te Lopikerkapel, bouwman) and his son Teunis Oosterom (b. 1847 te Zuid-Polsbroek,
  ongehuwd) are registered at the same address: "10, 33". (archief.rhcrijnstreek.nl/detail.php?id=12647209
  and id=12647224.) This is the first primary-source confirmation that house number 33 is specifically tied
  to Arie and Teunis own household, in Zuid-Polsbroek (not Noord-Polsbroek), already in the 1850s, well
  before Pieter 1875 birth, and the same number later cited as Pieter birth-house. PROBABLE (not proven) that
  it is the same physical farm continuously through 1875: the number recurs, but the household is also later
  recorded under different numbers in later register volumes (Arie "Nummer 57, 69 n.k." in L052 inv. 1134,
  1880-1900, id=67204595; Teunis himself "Nummer 59, 61" in L052 inv. 1135, 1900-1920, id=67207613), so the house
  was renumbered more than once and a sale or exchange of farms in between (per round 14 testament find) cannot
  be excluded.
Teunis exact 1875-era household entry (as adult head, with wife Adriana Cornelia Lekkerkerker and son Pieter)
was not pinned down this round. The index has his later entries (1900-1920 register, folio 64) and his
father 1850s entry, but the in-between "Bevolkingsregister Polsbroek, 1860-1880" (inv. 1133) entry specifically
under Teunis-as-head (not his brother Hendrik folio 215, which was checked and is a different household,
Hendrik having returned from Streefkerk in 1871) was not found in the time available. Open lead, see below.

Burgerlijke Stand geboorteakte index (L052a, Archief Ambtenaar van de Burgerlijke Stand van Polsbroek,
inv. 3, aktenummer 17): Pieter Oosterom, geb. 17-05-1875 te Polsbroek, vader Teunis Oosterom, moeder Adriana
Cornelia Lekkerkerker (id=10144930). Index only, no house number field, no scan link found on the detail page
(confirmed index-text-only, same as the bevolkingsregister entries; RHC online portal never showed an image
for any record checked this round, only transcribed fields).
CONTRADICTION found, not smoothed over: the RHC bevolkingsregister record for Teunis Oosterom (b. 17-05-1847
te Polsbroek, L052 inv. 1135 "Bevolkingsregister Polsbroek, 1900-1920", folio 64, id=67207613) states
"Overlijden: 25-05-1905 te Polsbroek". The project accepted line (status-oosterom.md) has Teunis Oosterom
1847-1915. These are 10 years apart. Both the birth date (17-5-1847) and the household link (his son Pieter
entry, id=67209098, explicitly says "Overgenomen van folionummer 64 van dit deel" = copied from Teunis own
folio) confirm this is our Teunis, not a namesake. This round did not try to resolve which date is right; that
needs the main session judgement (and ideally the actual BS overlijdensakte, 1905 or 1915, Polsbroek, which was
not searched this round). Flag for the main session; do not silently keep 1915 or switch to 1905 without
checking the overlijdensakte.
1b. The 1893 Lopik notary deeds (L156 inv. 1184/1185), double-checked, still NOT online. Confirmed via two
independent checks:
- Open Archieven (rel:5c7dd0c9-48df-8e35-9221-6f28c2e55a4c = boedelinventaris 17-3-1893, L156 inv. 1184 nr. 1408;
  rel:a27eb3d3-9d7e-9355-9979-e7b9e9959eb7 = boedelscheiding 13-12-1893, L156 inv. 1185 nr. 1525): the raw API
  record (records/show.json) has no media/scan field at all, only the A2A text abstract; the public record page
  (openarchieven.nl/rel:.../nl) shows no scan link either.
- RHC own "Lopik: notariele akten 1876-1906" page
  (rhcrijnstreek.nl/bronnen/indexen/overzicht-bewerkte-bronnen/lopik-notariele-akten-1876-1906/) confirms
  inv. 1184/1185 = "1893 januari-juli" / "1893 augustus-december" exist as an index entry, but RHC own
  "Notariele akten" informatieblad (.../informatieblad-type-bron/notariele-akten/) only states scans are linked
  for the pre-1811 notarial archives; nothing on the site claims scans exist for 1893. Round 12 "NOT online
  for these years" stands, confirmed independently today, not just repeated.
- Also checked: zoekakten.nl, Alle Overheid: no notary-deed content for Lopik/Cambier van Nooten found via web
  search (these sites mainly aggregate BS/population records, not notarial deeds).
### 2. Huijbert van Oostrum (1717-1792), quotisatie 1749 and HUA toegang 205

2a. Nationaal Archief 3.01.51 (Adriaan Steenis, ontvanger personele quotisatie): Jaarsveld IS in scope, but
NOT digitised; needs an in-person visit, now precisely pinpointed. The full inventory (fetched as PDF,
nationaalarchief.nl/onderzoeken/archief/3.01.51/download/pdf) was read completely (the website own React page
only lazy-loads part of the list, which caused an initial false negative; the PDF is complete). Inventarisnummer
11 ("Onder Schoonhoven", 1745-1748) explicitly lists "Zuidpolsbroek" and "Jaarsveld" by name among the
villages in that portfolio, alongside Cabauw, Bergambacht, Stolwijk, Lekkerkerk etc. So round 14 "Jaarsveld
inbegrepen" claim is correct, and is now sourced to a specific inv. nr. (11), not just the archive as a whole.
Digitisation: the finding aid itself states under "Beperkingen aan het gebruik": fully public, and under
"Beschikbaarheid van kopieen": Inventarisnummers van dit archief zijn niet in kopievorm beschikbaar. That is,
NA own catalogue says explicitly there are no copies/scans for any inventory number in this archive; it can be
reserved online for a reading-room visit (openbaar, reserveren via account) but not viewed remotely. Clear,
sourced NO for online availability, not speculation.

2b. HUA toegang 205 Huis Jaarsveld: inconclusive this round, not fully resolved online. The archive page
confirms 1283 described items, 381 digitised (about 30 percent), so partial digitisation does exist in
principle. A within-archive name search for Oostrum/Huijbert/pacht could not be driven through the site
search widget in the time available (the Inventaris tab and in-archive search box are both behind a heavy
single-page-app UI that resisted scripted interaction; clicks were intercepted by overlay elements, and
GET-parameter search URLs were silently ignored; this is UI friction, not bot-protection, so it was not pushed
further this round rather than declared blocked). A generic site-wide search for pacht Oostrum returned 111
Personen and 28 Transcripties hits, un-scoped to archive 205, not useful without further filtering. Not
resolved; needs either a slower manual pass through the Inventaris tree (via the debug Chrome) or an in-person
visit; this round could not confirm or rule out a digitised pacht/lease entry naming Huijbert.
### Searched without result (exact)
- archief.rhcrijnstreek.nl/zoeken.php scripted POST with the page own unique-token and form fields: HTTP 403
  (anti-forgery/WAF); not pursued further (rule: do not bypass bot protection); interactive browser search works
  fine instead (see above).
- RHC search "Oosterom" +Polsbroek +bevolkingsregister (quotes/plus operators): not treated as AND/required by
  this search engine; results are an OR/ranked match, not a filter; the facet filter UI
  (filters[Plaats][Polsbroek]=Polsbroek as a URL param) does work as a hard filter and was used instead.
- HUA hetutrechtsarchief.nl/onderzoek/resultaten/archieven?...&mizk_alle=... as a bare GET parameter: ignored
  (no results change); the visible trefwoord input field is hidden behind a collapsed search bar and resisted
  scripted fill().
- Web search for zoekakten.nl / Alle Overheid + "Cambier van Nooten" 1893: no notarial-deed content indexed there.
- NA site own rendered archief page (nationaalarchief.nl/onderzoeken/archief/3.01.51), scrolling/lazy-load:
  only loads items 1-7 of 1-16 in the browser DOM even after repeated scroll; use the PDF download instead for a
  complete inventory list.

### Open leads (next concrete step)
1. Teunis death date contradiction (1905 vs 1915): search Open Archieven / HUA for a Teunis Oosterom
   overlijdensakte Polsbroek in both 1905 and 1915 to see which (if either) matches; also re-check whatever
   source originally produced 1915 in the tree.
2. Teunis own 1860-1880 household folio (L052 inv. 1133) was not found; searching the RHC Polsbroek
   bevolkingsregister index (archief.rhcrijnstreek.nl, filter Plaats=Polsbroek, groep Persoon) page-by-page
   for Teunis Oosterom plus wife Adriana Cornelia Lekkerkerker in inv. 1133 specifically (not inv. 1132 or 1135)
   would pin the exact 1875-era house number and confirm or deny it was still 33 or already renumbered, and would
   be the direct, unambiguous proof-grade record for huis no. 33 in 1875 itself.
3. Request NA 3.01.51 inv. 11 ("Onder Schoonhoven", quotisatie 1745-1748, covers Zuidpolsbroek/Jaarsveld) for a
   reading-room visit; confirmed not available as a copy/scan; add to op-te-vragen.md.
4. HUA toegang 205: a manual (not scripted) browse of the Inventaris tree via the debug Chrome, scoped to
   pacht/leen items ca. 1700-1800, is still untried this round; 30 percent of the archive is digitised so this is
   worth a dedicated pass rather than more scripted search attempts.
