---
title: Design System Consistency
category: ui-ux
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [design-systems, frontend]
---

# Design System Consistency

## Minimal viable system (any project)
- **Tokens:** color ramp + accent, type scale, space scale, radius set, shadow set, motion durations/easings.
- **Primitives:** button, input, select, dialog, popover, toast, table, tabs — built once (shadcn/Radix pattern), themed via tokens.
- **Rules:** one way to do each thing. Two buttons that look 90% same = merge them.

## Consistency mechanisms
- Tokens in CSS variables / Tailwind theme; lint against arbitrary values.
- Composition over configuration: variants ≤3 per component.
- owned-components (shadcn model): code in your repo, upgrades are diffs you control.

## Drift controls
- New component → check existing inventory first (duplication is the #1 failure).
- Review screens side-by-side at 3 viewports; rhythm breaks show up visually.
- Record decisions in a living `design.md` (one page, not a book).
