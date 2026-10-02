## Round 17 (2026-10-02): death-date check, revised Bergambacht reading

- **Teunis Oosterom 1847–1915, death-date contradiction resolved**: round 16 flagged RHC's bevolkingsregister
  (L052 inv. 1135, folio 64) giving "Overlijden 25-05-1905", against the site's 1915. Checked the actual civil
  death record (`hua:A8F3AC7D-FF87-44EF-9636-6A154584BAF3` via `oa_kind.py`): "25-05-1915 Overlijden Polsbroek |
  Overledene: Teunis Oosterom (68); Partner: Adriana Cornelia Lekkerkerker; Vader: Arie Oosterom; Moeder: Elizabeth
  Kooijman". Same day and month, year off by exactly 10 — a transcription slip in RHC's own index (or in the
  original register annotation), not a second person: the civil death act is the authoritative primary source and
  names the same parents/partner. **1915 stays correct**, no change needed to the tree. Worth a one-line note to
  RHC if we ever contact them, otherwise no action.
- **Pieter Oosterom 1875–1959, Bergambacht house number — revised reading**: a schriftlezer pass on
  `raw/samh/bergambacht_blad20.jpg` + crops corrects round 14/15's guess. The cell (col. 13, row 1) reads, oldest to
  newest: black "Hogendijk 149" (1909) struck in red → a red correction "…N° 9…" (illegible) struck through in
  black → final black "**62**" (the earlier "141" read in round 14 was mistranscribed: it's actually "/4/" in the
  *profession* column, not a house-number step at all). Verdict: "Hogendijk" proven, "149" proven, final "62"
  waarschijnlijk (not proven — a faint red stroke under it is unexplained). **Do not geocode "Hogendijk 62" against
  today's BAG** — Bergambacht's Hogedijk was renumbered after this register (round 14 example: old 66 → now 10), so
  a right reading of the old number still doesn't give today's address without the gemeente's omnummeringsregister.
  Suggested site crop + caption in the schriftlezer's report (scratchpad, not yet copied into assets/).
- **New primary-source address data point** (round 16, RHC archief.rhcrijnstreek.nl index, interactive browse via
  debug Chrome — scripted POST search is blocked by the site's own CSRF/WAF, respected as bot protection):
  Arie Oosterom (1801) and son Teunis (1847) both registered at **"10, 33"**, bevolkingsregister Zuid-Polsbroek
  1850-1860 (L052 inv. 1132 folio 10, ids 12647209/12647224) — ties "huis no. 33" (already known from Pieter's 1875
  birth akte) to this household as early as the 1850s. Probable (not proven) it's the same farm through 1875: the
  household later appears under different numbers (57,69 then 59,61) in later volumes — can't rule out a renumbering
  vs. an actual move. Teunis's own adult household folio (inv. 1133, 1860-1880) would settle it — not yet located.
  1893 Lopik notary deeds (L156 inv. 1184/1185) reconfirmed not online.
- **Huijbert van Oostrum 1717–1792**: quotisatie lead now precise — Nationaal Archief 3.01.51, inv. 11 ("Onder
  Schoonhoven", 1745-1748) names Jaarsveld and Zuidpolsbroek explicitly, but the finding aid itself states no item
  in this archive has been digitised; reading-room only (added to `op-te-vragen.md`). HUA toegang 205 (pacht/leen
  items ca. 1700-1800) still needs a manual (non-scripted) browse — site's Inventaris UI resisted automation.

Next steps unchanged from round 16's list (death-date item now closed): Teunis's inv. 1133 folio, NA 3.01.51 inv. 11
visit, manual HUA 205 pass, and the still-pending Street View/BAG work is done (round 15).
