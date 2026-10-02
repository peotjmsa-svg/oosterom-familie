# Tricks and URL patterns (consolidated from all rounds)

Read once per project, not per round. Append here when a round finds a new one; do not duplicate in `log/`.

- `scripts/oa_plaats.py Oostrum Lopikerkapel -doop`: every record of a surname in one parish (API parameter
  `eventplace` works; `eventtype` returns 0).
- Open Archieven scans: `https://proxy.archieven.nl/download/39/<GUID>` for some burial books (full size, curl
  works). For others the Utrechts Archief viewer URL works in the debug Chrome; the thumbnail URLs on that page
  accept `&format=large` (1024 px) with curl.
- `scripts/scan_sheet.py` makes a contact sheet of consecutive proxy.archieven.nl pages (GUIDs are sequential within
  a register; the record's own GUID is often the cover/first page, so step forward to the act). `scan_get.py`
  downloads one page. `oa_ref.py` prints book, act number and scan GUID.
- HisGIS: GraphQL `https://oat.hisgis.nl/oat-ws/rest/graphql` (`oatScansByGemeente(gemeentenaam)` gives the scan
  codes); OAT images via IIIF `https://iiif.hisgis.nl/iiif/3/<Provincie>%2F<Gemeente>%2F<code>.jpg/full/2400,/0/default.jpg`;
  parcel geometry and tags (kad:gemeente/sectie/perceelnr, oat:soort) via Overpass
  `https://overpass.hisgis.nl/api/interpreter` (POST, header X-Requested-With). `scripts/kadaster1832.py` draws the
  parcels on the PDOK aerial photo. Minuutplan tiles `https://geoservices.hisgis.nl/tiles/minuutplans/{z}/{x}/{y}`
  have gaps at z≥17 for Jaarsveld A01. HisGIS GraphQL `personen` is empty for Jaarsveld (status INITIEEL): OAT scans
  must be read by eye, not queried.
- HUA register scans: `...NL-UtHUA_337-10_7_NNNN.jpg?format=large&miadt=39&miahd=<M>&mivast=39`, where miahd = miahd
  of page 1 + n − 1 (`scripts/hua_page.py`). Register 337-10 inv. 7 (1830) is ordered by municipality.
- BAG via PDOK WFS (`service.pdok.nl/lv/bag/wfs/v2_0`, typeName bag:pand / bag:verblijfsobject): build years and
  addresses near a point; PDOK locatieserver `reverse` for the nearest address.
- Street View: `scripts/streetview.py` (debug Chrome) saves stills to raw/streetview/. Google imagery itself: not
  published, only "© Google Street View (year)" stills with caption.
- RHC Rijnstreek (archief.rhcrijnstreek.nl): Imageserver `afbeelding.img?sessionid=<from the viewer>&QueryParams=<bestand_id>`
  returns the full-size scan. `scripts/rhc_scan.py` (`id` mode by bestand_id is reliable, `get` by list index;
  ~30 s per full scan — the server rate-limits and times out after ~70 downloads; go slowly, one scan per 30–60 s,
  ask the user before a bulk run). Faster untested route: viewer tile request
  `afbeelding.img?...&ACTION=maketile&t_width=..&t_height=..&t_offsetx=..&t_offsety=..&scalesize=..`.
- Delpher: `scripts/delpher.py` / `delpher_text.py` (KB SRU search and OCR text; page image via resolver
  `urn ...:pNNN:image`, ALTO via `...:pNNN:alto`).
- Notarial deed summaries (Open Archieven `rel:`): `scripts/oa_not.py` (deed summaries), `scripts/oa_arch.py` (one
  archive + period).
- Scan reading: `scripts/sheet.py DIR FROM TO` (4 pages per sheet, headings readable at 1000 px).
- MyHeritage: do not click the tree view (cards move, clicks miss). Use profile URLs
  `https://www.myheritage.nl/profile-OYYV6RLFE43U2DPKEJO6ILZTOTT5LPI-<id>/x`. Family members on a profile page are
  not `<a>` links, so their ids cannot be read from the page; ask the user for profile links.
- Use curl, not Python urllib (SSL error on this machine).
- HisGIS gemeentenaam for the north part of Polsbroek is "Noord Polsbroek" (with a space, code 06057), unlike
  "Zuid-Polsbroek" which uses a hyphen - try both spellings for a new gemeente before concluding scans do not exist.
- archiefman.nl (bouwvergunningen-indexen, e.g. Bergambacht bwt2063.htm) blocks WebFetch's default user-agent with
  a 403 but answers normally (200) to curl with a browser user-agent - a UA filter, not real bot protection.
- BAG bouwjaar/address lookup: PDOK locatieserver `free?q=<adres>` gives a point (no bouwjaar); for bouwjaar use
  PDOK BAG WFS `service.pdok.nl/lv/bag/wfs/v2_0`, typeName `bag:verblijfsobject`, a tight `bbox` (not a `CQL_FILTER`
  on `identificatie` — that param is ignored on this endpoint and returns unrelated features nationwide), then
  filter the returned rows for the right `openbare_ruimte` + `huisnummer`.
- RHC Rijnstreek en Lopikerwaard (archief.rhcrijnstreek.nl): the site's own name index IS free-text searchable, but
  only via normal interactive browsing (debug Chrome) - a scripted POST to `zoeken.php` gets HTTP 403 (CSRF/WAF).
  URL facet filters like `filters[Plaats][Polsbroek]=Polsbroek` work as a hard filter once on a results page.
- graftombe.nl hides deaths from the last decades behind a login ("Gegevens van recent overleden personen worden
  niet weergegeven op het openbare gedeelte") - do not log in, treat as a dead end for recent deaths.
