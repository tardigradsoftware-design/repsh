---
title: What Makes UI Look Professional
category: ui-ux
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [ui, design, frontend]
---

# What Makes UI Look Professional

Principles extracted from high-craft product experiences (Linear, Stripe, Vercel, Apple-class) — as transferable rules, not pixels. Re-verify the reference sites before quoting their current look (sites change; principles persist).

## 1. Type does the heavy lifting
- One real type scale (12/14/16/20/24/32/48+); weight contrast (400/500/600) over size chaos.
- Line-height tightens as size grows (1.6 → 1.1). Measure for prose ~65-75ch.
- Display face for identity + workhorse UI face; that's it.

## 2. Color discipline
- Neutral ramp (10 steps) + ONE accent used on <10% of surface = instant credibility.
- Semantic colors only for semantics. Dark mode is re-designed (contrast re-checked), never inverted.
- Borders/structure from neutrals; shadows reserved for elevation moments (modals, popovers).

## 3. Spacing rhythm
- One scale (4/8/12/16/24/32/48/64/96). Consistent paddings INSIDE same component class.
- Density varies by content: data-dense tables tighter, marketing airier — deliberately.

## 4. Structure through restraint
- Fewer containers; group with space and alignment before drawing boxes.
- Alignment consistency beats decoration. Radii consistent (1-2 values).

## 5. Motion with meaning
- 150-200ms ease-out for interactions; 300-500ms entrances; nothing loops without cause.
- Motion communicates causality (what just changed, where something came from).

## 6. Honest details
- Real numbers, real names, real screenshots. Empty states that guide. Loading = skeletons after ~300ms, not spinners.
- Every interactive element: hover/focus-visible/active/disabled states exist.

## 7. The professionalism test
Screenshot any screen: can you point to the type hierarchy, one clear accent, aligned rhythm, and zero decoration-without-purpose? If yes, it reads professional.

**Anti-signals:** gradient-on-gradient, glass everywhere, icon soup, fake metrics, three fonts, rounded-3xl-on-everything. See `avoiding-ai-slop-ui.md`.
