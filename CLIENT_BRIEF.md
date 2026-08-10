# CLIENT_BRIEF.md — Lucky Alien Papillon Kennel

## Project
One-page informational website introducing a papillon (Continental Toy Spaniel) kennel,
the breeders, and the puppies available, for a worldwide audience.

## Languages
- Ukrainian — build now (only language in this pass)
- Russian, English, Romanian — to be added later (out of scope for now)

## Site structure (final — do not add/remove sections)
1. Navigation
2. Hero
3. About the kennel ("Про нас")
4. Breeding dogs ("Плідники")
5. Puppies ("Цуценята")
6. Contact ("Контакти")

## Reference design
`desktop.png` — an English kennel site ("Lalabay"), light theme with a dark hero/footer/contact
block, gold (~#c9a869) script accent font + geometric sans, pill-outline buttons, thin gold wave
dividers, a giant faint watermark word behind the intro strip, black contact card floating on
white page. Match layout, spacing, typography and color treatment; do not add sections that
aren't in reference (e.g. no "News/Blog" section, since it's not in the requested structure);
adapt reference's two "Our dogs / puppies" mini-card pattern into our single "Breeding dogs" +
"Puppies" sections.

## Brand facts (sourced from real marketing photos in `Кінологія/`, not the text brief)
- Kennel name: **Lucky Alien** (Lucky Alien Kennel, FCI / Ukrainian Kennel Union)
- Base: Ukraine and Romania — worldwide shipping is a selling point, no single city emphasized
- Phones: +380 50 321 0192 (Ukraine, Viber/WhatsApp), +40 765 312 193 (Romania)
- Instagram: instagram.com/basenjlucky
- Facebook: facebook.com/nadiya.iovcheva
- Email: **placeholder** `info@luckyalien-kennel.com` — client to replace with real address later
- Kennel founded/officially registered: 2017 (per text brief — breeder's personal dream started
  in the 1980s, first papillon came from a German import line)

## About text source
Ukrainian text must be adapted (not machine-translated verbatim, edited to read well) from
`Питомник папийонов бриф.docx.txt` section 3 ("Про розплідник") and slogan (section 4):
"ПАПІЙОН ПРИНОСИТЬ ЩАСТЯ В ДІМ". Covers: childhood dream → first papillon from a German import →
philosophy (health-first genetic testing incl. PRA/NAD, show success/champion titles, active
agility life) → dogs live in the house as family, not in kennels/cages.

## Breeding dogs content
Real, verifiable dog on kennel marketing material: **Zvezdny Alliance Fantastic Style** —
Interchampion; Junior Champion Romania; Champion + Grand Champion Bulgaria, Romania, Moldova;
Best of Best in Breed Moldova. Health panel: DM-2 N/N, Factor VII N/N-FVII, NAD N/N,
PAP_PRA-pending, vWD-1 N/N. Present as the kennel's spotlight breeding female; do not fabricate
a matching resident male — no verified "our own stud" exists in source material.

## Puppies content (per client decision — show both)
1. **Lucky Alien Roblox** — papillon boy, DOB 12.10.2025, FCI pedigree, EU pet passport,
   microchipped, vaccinated, wormed, from fully health-tested parents, currently looking for
   his forever home.
2. **New litter, DOB 12.10.2025 — 4 males** — freshly announced litter (sire: Fashion Rid Keeper
   of My Soul; dam: Zvezdny Alliance Fantastic Style).
Price: **€1500–€2500** range, shown per client decision.

## Photography
Source folder `Кінологія/` has 9 real candid JPGs (usable as authentic site photography) and
4 pre-designed marketing flyer graphics (contain their own English text/branding — use only as
factual source, not as page imagery, to avoid mixing English flyer text into the Ukrainian page)
plus 3 video files (not required for this pass — static hero photo only, matches reference).

## Contact form
No backend. Build the form UI to match the reference visually; no submit handler wired up yet
(client will add a backend/service later).

## Open decisions already made with client
- Location line: "Ukraine · Romania" worldwide shipping emphasis, no single city
- Puppies section: show both Roblox + new litter
- Pricing: show €1500–€2500 range
- Email: placeholder, to be swapped later
- Form: static UI only, no submit logic
