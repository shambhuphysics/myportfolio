# CLAUDE.md

Guidance for Claude Code when working in this repository.

## Directory layout

```
index.html        root redirect → pages/index.html  (GitHub Pages entry point)

pages/            HTML source — edit these
  index.html      main portfolio (single-page, anchor-navigated)
  awards.html
  gallery.html
  machine_learning.html
  physics.html
  projects.html
  quantum.html
  useful_sites.html
  wellbeing.html

styles/           shared assets — edit these
  style.css
  script.js

images/           photos and section thumbnails
  profile.jpg, favicon.png
  awards/, gallery/, physics/, projects/, wellbeing/

cv/               gitignored — Shambhu_CV.pdf (linked as download from hero)
docs/             documentation notes (not site output)
```

## Development workflow

```bash
make serve      # python3 -m http.server → open http://localhost:8000/pages/
make deploy     # git add pages/ styles/ images/ → commit + push
make open       # open live site in browser
make status     # git status -s + last 5 commits
make clean      # remove .DS_Store / *~ / *.swp / *.pyc
```

**Live URL:** https://shambhubhandari.github.io
**GitHub Pages setting:** root of `main` branch (served via root `index.html` redirect)

## Runtime dependencies (all CDN, no npm)

- jQuery 3.5.1 — scroll events, sticky navbar, mobile menu
- Typed.js 2.0.11 — cycling hero text (`.typing`); strings in `styles/script.js`
- Three.js r121 + Vanta.js — animated fog on `#home`; config in inline `<script>` at bottom of `pages/index.html`
- Font Awesome 5.15.3 — icons
- Devicons v2.15.1 (CDN) — tech logos in the skills section

## Key CSS / JS patterns

- `[data-reveal]` + `.revealed` — IntersectionObserver scroll-reveal (set up in `styles/script.js`)
- `.stk-badge` / `.stack-cat-block` / `.stacks` — skills badge grid in `#skills`
- `.tl-item` — timeline cards in `#about` (Experience + Education)
- `.pub-grid` — 3→2→1-col responsive CSS Grid for publications
- Sticky navbar turns crimson at `scrollY > 20`
- `#scroll-progress` — fixed crimson bar tracking page scroll position
- Dark publications section (`background: #0f0f1a`) overrides `.title::after` background

## Content cheat-sheet

| What | File | Where |
|---|---|---|
| Hero cycling text | `styles/script.js` | `strings: [...]` in `new Typed(".typing", …)` |
| About bio | `pages/index.html` | `<p class="about-bio">` in `#about` |
| Experience / Education | `pages/index.html` | `.tl-item` blocks in `#about` |
| Skills badges | `pages/index.html` | `.stk-badge` spans in `#skills` |
| Publication links | `pages/index.html` | `<a class="pub-btn" href="…">` in `#publications` |
| Contact details | `pages/index.html` | `.icons` div in `#contact` |
| Vanta fog colours | `pages/index.html` | `highlightColor / midtoneColor / lowlightColor` in inline `<script>` at bottom |
| Sub-page content | `pages/*.html` | Each page has its own scoped `<style>` block |
