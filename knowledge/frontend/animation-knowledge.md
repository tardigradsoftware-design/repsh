---
title: Web Animation Techniques
category: frontend
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
tags: [animation, frontend, webgl]
---

# Web Animation Techniques

Scope: page transitions, scroll-driven, staggered reveal, SVG path, WebGL/Three.js, shaders/particles, microinteractions, loading choreography, magnetic/cursor effects, parallax, camera/timeline, spring physics. (Principles in `knowledge/ui-ux/animation-principles.md`.)

## Technique map
| Effect | Tool | Notes |
|---|---|---|
| UI state/entrance | motion (React) | springs, layout animations, AnimatePresence |
| Scroll storytelling | GSAP ScrollTrigger | pin + scrub; test mobile hard |
| SVG draw | stroke-dashoffset / GSAP DrawSVG | cheap and classy for line art |
| 3D scenes | three.js via @react-three/fiber | lazy-load, interaction-gated |
| Shaders/particles | three.js + custom GLSL | GPU budget on mobile is ~10x worse |
| Magnetic buttons/cursor | pointer handlers + spring | tiny doses; a11y-neutral |
| Parallax | transform + scroll progress | depth ≤2 layers to stay classy |

## Performance rules
- Compositor-only properties (transform/opacity/filter); will-change sparingly.
- Pause offscreen canvases (IntersectionObserver); cap DPR on mobile; degrade particle counts.
- Cinematic 3D landing = preload budget disaster otherwise: code-split + progressive enhance (static frame → interactive).

## Accessibility
- Global `prefers-reduced-motion`: kill transforms/parallax, keep opacity fades ≤200ms.
- No seizure-risk flashing; honor pause-on-interaction for autoplaying scenes.
