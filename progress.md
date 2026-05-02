# Progress

## Phase 1 — Planning
- [x] Create prd.md
- [x] Create progress.md

## Phase 2 — Navbar & Structure
- [x] Add `id="experience"` and `id="education"` to index.html
- [x] Remove sidebar (`<aside class="blog-sidebar">`) from index.html
- [x] Replace `.blog-layout` wrapper with `.home-hero` full-width container
- [x] Rewrite navbar HTML with dropdown structure (About ▾, Research ▾, Library ▾, Resources ▾, Contact)
- [x] Move Awards from Resources dropdown → About dropdown

## Phase 3 — Styling
- [x] Add dropdown CSS to style.css (hover-to-open, absolute panel, crimson top border)
- [x] Add sticky-state dropdown overrides (crimson background variant)
- [x] Add mobile accordion dropdown CSS inside `@media (max-width: 947px)`
- [x] Remove dead sidebar CSS rules (`.blog-sidebar`, `.sidebar-*`, `avatarFloat`)
- [x] Add `?v=20260502` cache-busting version string to CSS and JS `<link>`/`<script>` tags

## Phase 4 — JavaScript
- [x] Add mobile dropdown accordion toggle (`.has-dropdown > a` click handler)
- [x] Add outside-click close handler
- [x] Add non-dropdown link tap closes mobile menu overlay

## Phase 5 — awards.html Redesign
- [x] Sticky mini-navbar with back-to-home link
- [x] Hero header with title and crimson underline bar
- [x] Awards section: horizontal image+content card with tags and action buttons
- [x] Certifications section: 3-column pub-card grid with thumbnails and verify links
- [x] Peer Reviewing section: numbered list with publisher, since-date, Active badge

## Phase 6 — gallery.html Redesign
- [x] Sticky mini-navbar
- [x] Hero header
- [x] Search bar with live filter, auto-clear button, year-separator auto-hide
- [x] Chronological timeline (most recent → oldest): 7 events across 2018–2024
- [x] Per-event image grids with captions (single / pair / auto-fill layouts)
- [x] Lightbox with full-screen image, prev/next arrows, keyboard nav (← → Esc), counter
- [x] Responsive layout for mobile

## Phase 8 — Enhancements (post-launch)
- [x] Add 5 Coursera specialization certificates to awards.html (with images)
- [x] Replace Vanta FOG with Vanta NET (atomic network) hero background — pinned v0.5.24
- [x] Add interactive journey map (Leaflet.js, CartoDB dark tiles, 6 location pins + travel path)
- [x] Add visitor country detection (ipapi.co) + visit counter badge + localStorage history
- [x] Add university logos (UCL, KU, TU) to experience/education timeline cards
- [x] Add skill tag chips (.tl-tag) to all experience cards (PhD, KU, SGC)
- [x] Add Data Science self-learning entry to Education section
- [x] Create teaching.html: UCL (3 modules: GEOL0069/0046/0012) + NEB Nepal
- [x] Add Teaching to main navbar (after Research)
- [x] Migrate AI4EO resources to useful_sites.html

## Phase 7 — Deploy & QA
- [x] Deploy: navbar + sidebar removal (commit 59a1390)
- [x] Deploy: Chrome CSS cache-bust fix + prd.md/progress.md (commit 2761116)
- [x] Deploy: awards.html + gallery.html redesign + Awards moved to About nav (commit 65db2a3)
- [ ] Verify Chrome dropdown hover works correctly after hard-refresh
- [ ] Verify gallery search, lightbox, and timeline on mobile
- [ ] Verify awards.html cert images load and verify links work
