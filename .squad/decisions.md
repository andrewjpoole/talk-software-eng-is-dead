# Squad Decisions

## Active Decisions

# Decision: Fill-reveal animation strategy for Excalidraw SVGs

**Date:** 2026-04-29T19:14:38.829+01:00
**Author:** Legolas (Frontend Dev)
**Status:** Implemented

## Context

Excalidraw SVGs use fill-only paths (`stroke="none"`) which bypass the existing stroke-dasharray animation. All elements appeared instantly with no visible animation.

## Decision

Added a `fill-reveal` behavior using CSS `clip-path: inset(0 X% 0 0)` to progressively reveal fill-only elements left-to-right. This was chosen over:
- **Fade-in**: Less visually dramatic, doesn't feel like "drawing"
- **Synthetic stroke**: Too complex, risk of visual artifacts with Excalidraw's dense path data

## Impact

- New behavior activates automatically for any SVG with fill-only paths
- Standard stroked SVGs continue to use stroke-dasharray animation unchanged
- Duration is proportional to element bounding box size, maintaining consistent animation pacing


---

# Decision: AI Timeline Label Strategy

**Author:** Legolas  
**Date:** 2026-04-30  
**Scope:** `.demo/assets/ai-timeline.svg`

## Context
Andrew's hand-drawn timeline SVG has 25 dot markers (14 circles + 11 tiny pen-tap paths) across 4 serpentine rows, but 19 milestones to label.

## Decision
- **Milestone 1 (Claude 3 Family)** already labeled by Andrew in Inkscape — left untouched, no duplicate added
- **Rows with excess markers** (Rows 2–3 have 6 markers for 3 milestones each): milestones placed at every-other dot for visual spacing; unused dots stay unlabeled
- **Rows with deficit** (Row 1 has 6 dots for 8 milestones): adjacent non-landmark milestones grouped at same dot (e.g., "Llama 3.1 + Cursor IDE Growth")
- **LANDMARK milestones** always get their own dedicated dot — never grouped with non-landmarks
- **Label positioning**: alternates above/below per dot within each row to avoid overlap
- **Font sizes**: 6 for dates, 5 for names — proportional to the 960×540 viewBox with r=1.5 dots

## Impact
Only additive `<text>` elements — no existing SVG elements modified.


## Governance

- All meaningful changes require team consensus
- Document architectural decisions here
- Keep history focused on work, decisions focused on direction
