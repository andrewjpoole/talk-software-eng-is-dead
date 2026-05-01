# Legolas — History

## Core Context

- **Project:** A conference talk with VS Code demotime extension featuring SVG animations about the future of software engineering
- **Role:** Frontend Dev
- **Joined:** 2026-04-29T18:07:07.822Z

## Learnings

<!-- Append learnings below -->

### 2026-04-29T19:14:38.829+01:00 — Fill-reveal animation for Excalidraw SVGs
- Excalidraw exports shapes as `<g stroke="none">` → `<path fill="#1e1e1e">` pairs — no strokes anywhere
- Added `behavior: 'fill-reveal'` using CSS `clip-path: inset(0 X% 0 0)` to progressively reveal fill-only paths left-to-right
- Duration estimated from bounding box diagonal (`getBBox()`) proportional to animation speed
- Key file: `.demo/custom-components/animated-diagram-v2.js`
- New methods: `_canFillReveal()`, `_estimateFillDuration()`
- Existing stroke-based SVGs unaffected — fill-reveal only activates when `_canStroke()` returns false but element has visible fill

### 2026-04-30T11:10:00+01:00 — AI Timeline SVG labeling
- Hand-drawn SVG at `.demo/assets/ai-timeline.svg` exported from Concepts app, edited in Inkscape
- ViewBox: `-480 498 960 540` — coordinate system has negative x origin and y starts at 498
- Contains 14 `<circle r="1.5">` elements as dot markers + 11 tiny `<path>` elements that are pen-tap dot markers
- 4 serpentine rows: Row 1 (y~635-665, L→R), Row 2 (y~735-762, R→L), Row 3 (y~843-868, L→R), Row 4 (y~927-966, R→L)
- Total 25 markers mapped to 19 milestones; unused markers left unlabeled; some milestones grouped at same dot
- Andrew already labeled milestone 1 (Claude 3 Family) in Inkscape with a larger red circle (r=5.25) — skipped duplicate
- Font: `Silent People` (Andrew's talk font); Inkscape uses quoted form `'Silent People'`
- LANDMARK items use `fill="#C41E3A"` (red); normal items `fill="#333"` dates, `fill="#555"` names
- Reference timeline at `.demo/assets/ai-timeline-reference.svg` has the complete data model
- Key pattern: alternate text above/below dots within each row to avoid label overlap

### 2026-05-01T10:01:33+01:00 — Gartner Hype Cycle SVG slide
- Created `.demo/assets/gartner-hype-cycle.svg` matching hand-drawn style of `kubler-ross-change-curve.svg`
- Same viewBox (`-480 498 960 540`), same `Silent People` font, same stroke styles (`stroke-width:3.017`, round caps/joins)
- Reused identical Y-axis and X-axis path data from reference (same arrow groups with `sodipodi:nodetypes`)
- Y-axis label "Expectations" (rotated ~-90.7°), X-axis label "Time"
- Hype curve uses single continuous cubic bezier path with `stroke-dasharray:18.102` for animation compatibility
- Curve shape: low start → sharp peak (~y=595) → deep trough (~y=902) → gradual rise → plateau (~y=718)
- 5 stage labels use 24px font (slightly smaller than 32px title) with two-line `<tspan>` pairs for long names
- Each stage separated by `<!--Pause:UntilPlay-->` with cyan ellipse markers (`fill:#21e3ff`, rx=6.41, ry=5.80)
- Slide markdown (`.demo/slides/gartner-hype-cycle.md`) uses `animated-diagram.html` layout with `invert:true`, `speed:1200`
- Scene inserted in `.demo/act1.json` as `demo-gartner-1` after `demo-quebec-2`, before `demo-dark-1`
- No base64 images included — pure SVG elements only

## Session Completion

### 2026-04-30T11:18:00Z — Session finalized by Scribe
- Decisions on fill-reveal animation and timeline labeling archived in `.squad/decisions.md`
- 2 decision inbox files merged and deleted
- Orchestration and session logs written
- All work verified and committed
