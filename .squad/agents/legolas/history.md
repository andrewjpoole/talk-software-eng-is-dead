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
