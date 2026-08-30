# CLIENT_BRIEF.md — Lucky Alien Papillon Kennel

## Project
One-page informational website introducing a papillon (Continental Toy Spaniel) kennel,
the breeders, and the puppies available, for a worldwide audience.

## Languages
- Ukrainian — build now (only language in this pass)
- Russian, English, Romanian — to be added later (out of scope for now)

## Site structure (as of the August 2026 full overhaul)
1. Navigation (8 pills: Головна · Про нас · Плідники · Цуценята · Новини · Відгуки · Порода · Контакти)
2. Hero
3. Credentials strip
4. About the kennel ("Про нас")
5. Breeding dogs ("Плідники") + "Ми рекомендуємо" closing gallery + one-line Basenji mention
6. Show news ("Новини") — dated achievement timeline
7. Puppies mega-section ("Цуценята") — 5 in-page sub-sections with jump pills:
   Про цуценят · Зараз доступні · Відео · Догляд · Ціни
8. How to reserve a puppy ("Як забронювати цуценя") — Заявка / Завдаток / Договір, 3 steps
9. Reviews ("Відгуки")
10. Before you arrive ("Перед тим як забрати цуценя")
11. FAQ ("Питання")
12. About the Papillon breed ("Про породу папійон")
13. Contact ("Контакти")
14. Footer — real logo, certificate photo, updated address

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

## August 2026 overhaul — new facts discovered in `Кінологія 2/`
- **The kennel breeds both Basenji and Papillon** (real logo, 3 of 4 show-news graphics, and the
  Instagram handle `basenjlucky` are all Basenji). **Client decision: keep the site Papillon-only**
  for the main product content (Breeding dogs, Puppies, Breed info), with a single sentence in the
  Breeding section noting a dedicated Basenji section is coming.
  **Update:** the client later explicitly asked for the Новини (Show news) section to become a
  photo blog using the real graphics in `Кінологія 2/Новини шоу/` — 3 of those 4 real photos are
  Basenji achievements, so the News blog now legitimately shows Basenji content (clearly tagged
  "Басенджі" vs "Папійон" on each card), while Breeding/Puppies/Breed sections remain Papillon-only.
  This is a deliberate, narrower exception (real news reporting, not a full Basenji product line) —
  don't expand Basenji content further without asking.
- Real kennel logo now in use everywhere (nav, footer, favicon): `assets/img/logo-dark(-icon).png`
  (dark line art, transparent bg, for light surfaces) and `logo-light(-icon).png` (pale gold line
  art, transparent bg, for dark surfaces) — processed from
  `Кінологія 2/Логотипи + примітки /`. The old "LA" monogram is fully retired.
- Real city from the UKU/FCI certificate: **Кривий Ріг, Україна**. Owner's full legal name:
  **Надія Іовчева**. Kennel registration number **427/16**. Certificate photo lives in the footer
  (`assets/img/certificate.jpg`), per the source folder's own instruction ("place at the end of
  the site in good quality").
- 3 real puppy videos now embedded in the Puppies → "Відео" sub-section
  (`assets/video/puppy-1/2/3.mp4`, poster frames auto-extracted via ffmpeg). These are the
  kennel's own Instagram-style promo reels (Lucky Alien branding baked into the video itself),
  not raw candid footage — that's expected/normal, matches how the kennel already presents itself.
- `Кінологія 2/Випускники/` supplied real photography: 2 candid puppy photos now used in the
  Breeding section's "Ми рекомендуємо" gallery (`graduate-1.jpg`, `graduate-2.jpg`), and 2 real
  owner+dog photos powering the Reviews section avatars (`review-1.jpg`, `review-2.jpg`).

## Placeholder content added this pass — flag for client review
These sections have no real source material yet; written now with safe, non-fabricated content
per the client's own instruction ("if info missing, write it yourself, we'll amend"). Client should
review and replace:
- **Ціни (Price list)**: kept the existing real €1500–2500 range, added an illustrative "what's
  included" list — client should confirm the list items are accurate.
- **Завдаток (Deposit)** and **Договір (Contract)** in the "Як забронювати цуценя" section: no real
  deposit amount/terms or contract sample exists yet. Copy explicitly says these are agreed
  individually / a contract sample will be added — **do not invent a specific deposit amount or a
  fabricated contract photo**.
- **Відгуки (Reviews)**: the 2 testimonial quotes are illustrative, paired with real owner photos
  but attributed generically ("Власниця цуценяти Lucky Alien") rather than invented names — client
  should swap in real review text when available.
- **Догляд за цуценям (Puppy care)** and **Перед тим як забрати цуценя (Before you arrive)**: general,
  safe, non-kennel-specific advice — fine to keep as-is or let the client personalize further.
- **Питання (FAQ)**: 5 reasonable, generic Q&A pairs — client may want to add kennel-specific ones.
- **Про породу папійон (About the breed)**: public breed-standard facts (size, weight, lifespan,
  coat, history) — not kennel-specific claims, safe to keep as reference content.
