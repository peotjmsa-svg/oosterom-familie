## Round 7 (2026-10-01): Smetsers in the tree, male line only, Plekken page

- User decision: famkroon's Jan Ariensz = son of Arien Smetser is accepted ("ook genaamd Smetser, Brug(ge) en Jan
  Ariens Schipper"); add the Smetsers. Note: famkroon marks Arien (V-a) and Jan (VI-a) with {Q} = "tijdelijke
  zoekcode" (their own code list, Codes en data page); generations I–IV have no source code; Gerrigje Smetser (II)
  is {?K.} = "geen bewijs, kind van deze ouders". Code letters: a/b/c = birth/marriage/death from Genlias,
  n notarial, i other internet, capitals = cards/documents in hand.
- scripts/parse_famkroon.py parses the genealogy into data/famkroon.json (1374 persons; 400 possibly living left out:
  born after 1925 or marked {X}). build_data.py merges it under our checked data (MAP our id -> famkroon id for
  Huijbert, Teunis 1762, Arie 1801, their wives and matching children), root = fk_I Cornelis Smetser.
- User: tree only male line (no children of daughters) and blood relatives must carry the Oosterom/Oostrum/Smetser
  name. Result: 744 persons (455 blood relatives + 289 partners), 313 families.
- Plekken page (plekken.html): Jaarsveld/Oversloot (1392 mention; Huis te Jaarsveld destroyed by the French 1673),
  kerk Lopikerkapel (chapel 1327, rebuilt ca. 1450, reformed 1605, independent 1620, pulpit 1646, bell by Gerhart
  Schimmel 1682, restored 1828–1832 by contractor Roeloff Benschop – probably Roelof Benschop 1794–1858, son of
  Dirkje van Oostrum × Aalbert Roelofs Benschop), de Lek, Montfoort (Annetje 1622 x 1649 burgemeester Hendrick Jacobs
  Speyert), Willige Langerak, Zuid-Polsbroek (De Graeff heerlijkheid), Bergambacht, Portengen/Ter Aa (Arie 1756 branch).
- famkroon errors noticed: Willemijntje van Oosterom b. 1810 "overleden 1954, 143 jaar oud"; Arie 1801's children
  miss Teunis 1847 (ours).
- Other famkroon pages (Kroon, Boele, Lam, Griffioen …) are in-law families of the Kroon author; not needed.
