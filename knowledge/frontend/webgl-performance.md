---
title: WebGL/Three.js Performance Budgets
category: frontend
confidence: medium
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
tags: [webgl, threejs, performance]
---

# WebGL Performance Budgets

For 3D marketing/landing experiences. Measure on mid-tier mobile — desktop numbers lie.

## Budgets (mobile mid-tier)
- Scene init < 300ms after gate; frame < 8ms GPU target 60fps (or cap 30fps deliberately)
- Draw calls < 100; triangles < 200k; textures < 8MB total; DPR capped ≤1.5-2

## Tactics
- Interaction-gated init (don't render until visible/intent); IntersectionObserver pause offscreen
- Merge geometries; instancing for repeats; frustum culling on; compressed textures (KTX2/basis)
- Shader care: avoid per-fragment branches; prefer vertex math; precompute
- Fallback: poster frame or static render for reduced-motion/low-power (`navigator.gpu`/WebGL probe)
- Load sequencing: shell first → poster → scene behind interaction; never block LCP on WebGL
