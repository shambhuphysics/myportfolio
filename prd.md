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