---
title: Avoiding AI-Slop UI
category: ui-ux
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [ui, ai-slop, frontend]
---

# Avoiding AI-Slop UI

Why AI-generated sites look AI-generated, and the defaults that fix it. (Detection workflow lives in `skills/ai-slop-detection`.)

## Root causes
1. **Central-tendency training** — models average the web: purple gradients, glassmorphism, floating orbs. Unchecked generation regresses to this mean.
2. **Decoration as substitution** — no design system → ornament fills the vacuum.
3. **Fabrication pressure** — filler metrics/badges because real content wasn't provided.
4. **Layout template lock-in** — sidebar+cards+chart skeleton stamped on every screen.

## Default fixes (bake into generation)
- Generate the token sheet FIRST; constrain all output to it.
- One accent, neutral ramp, real type scale, single radius system.
- Require real content: if a claim can't be substantiated, remove it — never invent numbers.
- Vary layout by task: let information shape structure.
- Motion budget: total entrance choreography ≤1 per view; interactions 150-200ms.
- Post-generation lint: run the slop checklist, fix, re-render.

## Copy-level slop
"Revolutionary AI-powered next-gen platform" → name the actual workflow, user, and outcome. Specificity is the anti-slop of language.
