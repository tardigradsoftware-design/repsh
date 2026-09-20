---
title: Visual Design Research Method
category: ui-ux
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [research, ui, method]
---

# Visual Design Research Method

How to study reference sites (Apple, Linear, Stripe, Vercel, Raycast, Arc, Notion, Framer, Supabase, Resend, Clerk, Lemon Squeezy) legally and usefully.

## Rules
1. **Verify today** — screenshot + date every observation. Sites ship changes weekly; stale references poison decisions (our `currentness policy` applies to visuals too).
2. **Extract principles, never pixels** — layout logic, hierarchy strategy, motion causality, density decisions. Direct copying produces incoherent Frankenstein UI and can infringe.
3. **Multiple examples per principle** — one site's quirk is not a pattern; three sites' convergence is.

## Extraction template (per site)
- First-viewport strategy: what does it lead with? (product? proof? motion?)
- Hierarchy: how many levels visible? how is accent used?
- Density decision: air vs data?
- Navigation: primary pattern + shortcut affordances (⌘K, etc.)
- Motion: what animates, when, how long, reduced-motion behavior?
- Trust signals placement: logos? numbers? testimonials? where?

## Output
A principles memo feeding `frontend-design` — e.g., "all 6 references gate heavy content behind interaction (⌘K/modal), lead viewport is one idea + one CTA."
