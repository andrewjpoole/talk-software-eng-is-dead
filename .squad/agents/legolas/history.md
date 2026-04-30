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

## Session Completion

### 2026-04-30T11:18:00Z — Session finalized by Scribe
- Decisions on fill-reveal animation and timeline labeling archived in `.squad/decisions.md`
- 2 decision inbox files merged and deleted
- Orchestration and session logs written
- All work verified and committed
