# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development

No build step. Open `index.html` directly in a browser, or serve locally:

```bash
python3 -m http.server 8000   # then open http://localhost:8000
```

Deploy by pushing to the `main` branch of `https://github.com/shambhuphysics/myportfolio` — GitHub Pages serves the root automatically. Live URL: `https://shambhuphysics.github.io/myportfolio/`

## Architecture

Single-page static site (`index.html` + `style.css` + `script.js`). All five sections live in one HTML file; navigation anchors scroll to them.

**Section order:** `#home` → `#about` → `#skills` → `#publications` → `#contact`

**Runtime dependencies (all CDN, no npm):**
- jQuery 3.5.1 — DOM helpers and scroll events in `script.js`
- Typed.js 2.0.11 — cycling text in `.typing` (hero) and `.typing-2` (about); strings live in `script.js`
- Three.js r121 + Vanta.js — animated fog background on `#home`; config is in the inline `<script>` at the bottom of `index.html`
- Font Awesome 5.15.3 — all icons, including skill-card icons (`<i class="fab/fas ...">`)

**Key CSS patterns:**
- `.skill-card` uses CSS `perspective`/`rotateY` for 3D flip on hover; front uses `card-front`, back uses `card-back`
- `.pub-grid` is a CSS Grid (3-col → 2-col → 1-col responsive) defined entirely in `style.css`
- Sticky navbar turns crimson at `scrollY > 20` (jQuery in `script.js`)
- Dark publications section (`background: #0f0f1a`) requires overriding `.title::after { background }` — already done in the custom block at the bottom of `style.css`

**Asset locations:**
- `images/profile.jpg` — profile photo (source: Blogger backup)
- `images/favicon.png` — site favicon
- `logo/` — unused SVG/PNG logos from the original template (can be deleted)
- `cv/Shambhu_CV.pdf` — excluded from git via `.gitignore`; linked as a download in the hero

## Content updates

- **Typed.js strings** — edit the `strings: [...]` arrays in `script.js` (two instances: `.typing` and `.typing-2`)
- **Publication "Read Paper" links** — each `<a href="#" class="pub-btn">` in `index.html` under `#publications`; replace `#` with the DOI URL
- **About bio** — the `let text = "..."` string inside the inline `<script>` block in the about section of `index.html`
- **Contact details / social links** — the `.icons` div inside `#contact`
- **Vanta fog colours** — the `highlightColor`, `midtoneColor`, `lowlightColor`, `baseColor` hex values in the inline `<script>` at the bottom of `index.html`
