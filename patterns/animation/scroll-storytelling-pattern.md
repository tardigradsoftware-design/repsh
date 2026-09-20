---
title: Scroll Storytelling Pattern
category: animation
confidence: medium
updated: 2026-09-20
tags: [animation, scroll, gsap]
---

# Scroll Storytelling

GSAP ScrollTrigger-class: pinned sections + scrubbed timelines; progress-mapped transforms; text reveals staged.

## Rules
- One narrative per page; steps must be readable WITHOUT animation (content-first fallback)
- Mobile: unpin or simplify (pinning + touch = jank factory); test on mid-tier Android
- Reduced-motion: swap to static compositions
- Performance: transform/opacity only; will-change on animated nodes; measure long frames
