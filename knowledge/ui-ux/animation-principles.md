---
title: Animation Principles (UI)
category: ui-ux
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [animation, motion, frontend]
---

# Animation Principles

## When animation helps
- Causality: element A moved → show where it went (list reorder, route change)
- Continuity: shared-element transitions keep context
- Feedback: hover/press within 150-200ms
- Orientation: entrance reveals structure (stagger ≤5 items, 30-60ms offsets)

## When it harms
- Loops without information (pulsing orbs)
- Entrance replays on every navigation
- Animation masking slowness (spinner theatre) — fix the slowness
- Anything that breaks with `prefers-reduced-motion`

## Budget
- Interactions 150-200ms ease-out; entrances 300-500ms; page transitions ≤400ms.
- One choreographed moment per view max.
- Mobile: fewer + shorter; test on mid-tier Android, not your laptop.

## Implementation notes
- Physics (spring) for gesture-driven; easing curves for state changes.
- Animate transform/opacity only (compositor-friendly); measure long frames after adding.
- Libraries: `motion` (React, physics+gestures), GSAP ScrollTrigger (scroll storytelling), Lottie for complex illustrated loops. Verify current versions in `repositories/frontend/`.
