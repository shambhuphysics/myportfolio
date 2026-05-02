# PRD — Professional Portfolio Navbar Redesign

## Goals

- Replace dual-navigation (top navbar + left sidebar) with a single hierarchical navbar
- Consolidate all navigation into hover dropdown groups
- Remove sidebar so the home hero spans full width
- Remove redundant "Home" link from navbar
- Add deep-link anchors for Experience and Education sections

## Nav Structure

| Parent | Sub-items | Target |
|---|---|---|
| About | Experience | `#experience` |
| | Education | `#education` |
| | Skills | `#skills` |
| Research | Projects | `projects.html` |
| | Publications | `#publications` |
| Library | Machine Learning | `machine_learning.html` |
| | Physics & Chemistry | `physics.html` |
| | Quantum Computing | `quantum.html` |
| Resources | Useful Sites | `useful_sites.html` |
| | Gallery | `gallery.html` |
| | Wellbeing | `wellbeing.html` |
| | Awards | `awards.html` |
| Contact (plain) | — | `#contact` |

## UX Rules

- Hover to open on desktop (≥948px), click to open on mobile (<948px)
- Mobile: accordion-style, siblings collapse when one opens
- Click outside navbar closes all open dropdowns
- All sub-page links open in same tab
- Smooth scroll preserved for in-page anchors

## Out of Scope

- Dark/light mode toggle
- Search
- CMS integration
- Sub-page navbar changes (other `.html` files not touched)
