# PRD — Personal Portfolio Site

## Goals

- Replace dual-navigation (top navbar + left sidebar) with a single hierarchical navbar
- Consolidate all navigation into hover dropdown groups
- Remove sidebar so the home hero spans full width
- Remove redundant "Home" link from navbar
- Add deep-link anchors for Experience and Education sections
- Redesign awards.html to match the publications section aesthetic
- Redesign gallery.html as a chronological timeline with search and lightbox
- Move Awards link into the About dropdown

## Nav Structure (current)

| Parent | Sub-items | Target |
|---|---|---|
| About | Experience | `#experience` |
| | Education | `#education` |
| | Skills | `#skills` |
| | Awards | `awards.html` |
| Research | Projects | `projects.html` |
| | Publications | `#publications` |
| Library | Machine Learning | `machine_learning.html` |
| | Physics & Chemistry | `physics.html` |
| | Quantum Computing | `quantum.html` |
| Resources | Useful Sites | `useful_sites.html` |
| | Gallery | `gallery.html` |
| | Wellbeing | `wellbeing.html` |
| Contact (plain) | — | `#contact` |

## UX Rules

- Hover to open on desktop (≥948px), click to open on mobile (<948px)
- Mobile: accordion-style, siblings collapse when one opens
- Click outside navbar closes all open dropdowns
- All sub-page links open in same tab
- Smooth scroll preserved for in-page anchors
- CSS/JS links carry `?v=YYYYMMDD` version strings to bust browser cache on deploy

## awards.html Design

- Three sections: Awards · Certifications · Peer Reviewing
- Awards: horizontal card (image left, content right) with tags, description, action buttons
- Certifications: 3-column card grid matching `pub-grid` style; image thumbnail, issuer, title, verify link
- Peer Reviewing: numbered list with publisher, since-date, Active badge; slide-right hover

## gallery.html Design

- Search bar at top — live keyword filter on title + `data-tags`; year separators auto-hide when empty
- Timeline layout (most recent top → oldest bottom) with vertical crimson line and glowing dot per event
- Events: May 2024 TYC/Imperial · Apr 2024 UCL · Apr 2023 AWE/Oxford · Feb 2023 Royal Institution · 2022 Khalifa UAE · 2020–22 TU/KU Nepal · 2018–19 SIESTA India
- Responsive image grid per event with captions below each photo
- Lightbox: full-screen overlay, prev/next nav (arrows + keyboard), counter, ESC to close

## Out of Scope

- Dark/light mode toggle
- CMS or backend integration
- Changes to machine_learning.html, physics.html, quantum.html, wellbeing.html, useful_sites.html, projects.html

## Teaching Section

### Nav change
Add **Teaching** as top-level item after Research:
`About | Research | Teaching | Library | Resources | Contact`

### New page: `pages/teaching.html` — 2 sections (awards.html dark style) ✅

#### 1. UCL (2022–Present) — 3 module cards with links
- GEOL0069 AI for Earth Observations — Tags: Python, Deep Learning, Remote Sensing, Geospatial, Raster, AWS, Azure
- GEOL0046 Deep Earth & Planetary Modelling — Tags: VASP, FORTRAN, Python, Shell, HPC, Phase Transitions, High-Pressure Physics
- GEOL0012 Global Geophysics — Tags: Solid State Physics, Thermodynamics, Statistical Mechanics

#### 2. National Examination Board — Nepal (2019–2021) — merged card
- Taught Mathematics and Physics (undergraduate + intermediate levels)
- Tags: Mathematics, Physics, Teaching, Mentoring

#### AI4EO resources migrated → `useful_sites.html` (new section at bottom) ✅

### Files changed ✅
| `pages/teaching.html` | created |
| `pages/index.html` | Teaching added to navbar after Research |
| `pages/useful_sites.html` | AI4EO section added |

## Publications — Live Citations + Journal Quartiles

### Problem
Current pub cards have static text, no citation counts, no journal quality indicator.

### Data source
- **Snapshot** (2026-05-02): 18 papers, 189 total citations, h-index 10 (Google Scholar)
- **Live counts**: Semantic Scholar public API (free, no key) — `api.semanticscholar.org/graph/v1/paper/search?query=TITLE&fields=citationCount`
- **Journal quartiles**: hardcoded from Scimago SJR (static, updated manually)

### Implementation

#### 1. Rebuild pub cards with new fields
Each `.pub-card` gets:
- **Citation badge** `<span class="pub-cites">` — shows count, refreshed by JS
- **Quartile badge** `<span class="pub-q q1">Q1</span>` — colour-coded (Q1=green, Q2=blue, Q3=grey)
- **Year chip** already present (keep)
- Scholar link on citation badge (opens paper on Scholar)

#### 2. Full publication list (18 papers from Scholar snapshot)

| # | Title (short) | Journal | Q | Cites | Year |
|---|---|---|---|---|---|
| 1 | Structural deformation…CrS2,CrSe2,CrSSe | Physica E | Q2 | 29 | 2023 |
| 2 | Penta-SiCN: A highly auxetic monolayer | ACS Appl. Electron. Mater. | Q1 | 23 | 2022 |
| 3 | Strain dependent…penta-BCN | Carbon Trends | Q2 | 21 | 2022 |
| 4 | Large Negative Poisson's Ratio…penta-B2C | ACS Omega | Q2 | 20 | 2022 |
| 5 | Structural, electronic, magnetic…Cr2X3 | Eur. Phys. J. B | Q2 | 19 | 2021 |
| 6 | First-principles DFT…MoSSe | Comput. Mater. Sci. | Q1 | 18 | 2023 |
| 7 | Enhanced optoelectronic…fluorinated | Appl. Surf. Sci. | Q1 | 13 | 2022 |
| 8 | Strain induced…2D silicene | J. Nepal Phys. Soc. | — | 11 | 2021 |
| 9 | New 2D p-SiPN: Wide Bandgap | Nanomaterials | Q2 | 10 | 2022 |
| 10 | Enhanced mechanical…optical | Appl. Surf. Sci. | Q1 | 10 | 2022 |
| 11 | Signature of low dimensional quasi-F center | Materials Horizons | Q1 | 8 | 2024 |
| 12 | Optoelectronic…fluorinated hexagonal | Chem. Phys. Lett. | Q2 | 3 | 2021 |
| 13 | Strain driven negative Poisson's ratio | Carbon Trends | Q2 | 3 | 2021 |
| 14 | New 2D penta-SiPN | J. Phys.: Conf. Ser. | Q3 | 1 | 2024 |
| 15 | Dielectric barrier discharge plasma | Chem. Eng. J. | Q1 | — | 2026 |
| 16 | Ab initio phase diagrams binary alloys | J. Chem. Phys. | Q1 | — | 2025 |
| 17 | Highly Tunable Negative Poisson's Ratio | Asia Pac. Phys. Conf. | — | — | 2022 |
| 18 | Study of strain-induced…(preprint) | ChemRxiv | — | — | 2021 |

#### 3. Live citation refresh (JS)
On page load, for the top 6 visible cards:
```js
fetch(`https://api.semanticscholar.org/graph/v1/paper/search?query=TITLE&fields=citationCount`)
  .then(r=>r.json()).then(d=>{ /* update .pub-cites span */ })
```
Fallback: show snapshot count if API fails or times out (>3s).

#### 4. CSS additions
```css
.pub-cites { background:rgba(220,20,60,0.12); color:crimson; border:1px solid rgba(220,20,60,0.3); padding:2px 8px; border-radius:12px; font-size:11px; font-weight:700; }
.pub-q     { padding:2px 8px; border-radius:12px; font-size:10px; font-weight:800; margin-right:4px; }
.pub-q.q1  { background:#e8f5e9; color:#2e7d32; }
.pub-q.q2  { background:#e3f2fd; color:#1565c0; }
.pub-q.q3  { background:#f5f5f5; color:#757575; }
```

### Files
| `pages/index.html` | Rebuild all pub-card HTML (18 papers) + add live-fetch JS snippet |
| `styles/style.css` | Add `.pub-cites`, `.pub-q` badge styles |

## Remove Blogger Post Preview Sections from Landing Page

### Problem
After the Publications section, `index.html` contains 7 legacy "blogger-section" blocks
(Research, Awards & Certs, Gallery, Wellbeing, Machine Learning, Quantum Computing,
Physics & Chemistry) — each a card with raw `&amp;nbsp;`-polluted text and a "Read Full Post"
button. These are redundant: the navbar already links to each sub-page directly.

### Fix
Delete all 7 `<section class="blogger-section …">` blocks from `index.html`.
These are lines ~522–630 (from `id="projects"` blogger block through `id="physics"` blogger block).
No CSS or JS changes needed — `.blogger-section` and `.card-grid` rules can stay (they'll be
inert) or be pruned from `style.css` in a separate cleanup pass.

### Result
Page flow after removal:
`Home → About → Skills → Publications → Contact → Journey Map → Footer`

### File
| `pages/index.html` | Delete 7 blogger-section blocks |

## Real time website visitor counter

- Use a real time website visitor counter
- Use map for location display

## Change landing page background
- Use something dynamic for eg. atoms movement, particles movement, etc.
- Should be light and not distractive
- Should be responsive and work on mobile devices
- Should be optimized for performance
- Should be interactive and engaging
- Should be visually appealing
- Should be easy to implement
- Should fill the entire screen
- Should not be distractive

## Search bar
 - search must find any keyword in the website