## Round 15 (2026-10-02): BAG check + Street View stills for the two confirmed father addresses

Checked bouwjaar via PDOK BAG WFS (`bag:verblijfsobject`, bbox query) for both addresses round 12/13 identified:
- **Zuidzijdseweg 142, Polsbroek** (Arie Oosterom 1801-1881, farm bought 1839): confirmed bouwjaar 1888 — current
  house postdates Arie's death (1881) by 7 years, so it is a rebuild on his farm, not the building he lived in
  himself. Still the right parcel/address, kept.
- **Kapelsepad 15, Lopikerkapel** (Teunis Huijbertsz van Oostrum 1762-1830, farm "N° 7" Jaarsvelderkapel): confirmed
  bouwjaar **2023** — a brand-new house, as round 13 already said ("new houses 2020-2023 stand on A149"). The old
  thatched farmhouse visible from the road (Kapelsepad 16/18/19, bouwjaar 1550) is the neighbour's, on parcel A131,
  NOT Teunis's — matches round 13's removal of that photo. Heading 0 of the Street View still (see below) shows the
  actual new house at nr. 15; heading 270 shows the neighbour's old farm and should not be used/published.

Street View stills taken (debug Chrome, `scripts/streetview.py`, headings 0/90/180/270), saved to
`raw/streetview/`:
- `arie_1801_zuidzijdseweg142_*.png` (51.98632512, 4.87776516) — heading 270 best shows the small farmhouse across
  the canal matching the "thatched farmhouse" BAG description.
- `teunis_1762_kapelsepad15_*.png` (51.98811009, 5.03675617) — heading 0 shows the new (2023) house at nr. 15;
  do not use heading 270 (shows neighbour's old farm, not ours).

Pieter Oosterom 1875 (Bergambacht "Hogedijk", house-number reading disputed between round 14's crops): tried
geocoding "Hogedijk 20 Bergambacht" (one candidate reading) at PDOK locatieserver — no such house number exists
today, only street-level hits. Confirms round 14's own "onzeker" verdict; not pursued further without an in-person
archive reading. No Street View taken for Pieter/Arie 1908/Huijbert 1717/the famkroon-only generations — no address
precise enough to point a camera at.

Tricks: PDOK BAG WFS `bag:verblijfsobject` CQL_FILTER by identificatie doesn't work on this endpoint (returns
unrelated features); use a tight `bbox` instead and filter the returned rows for the right `openbare_ruimte` +
`huisnummer`.
