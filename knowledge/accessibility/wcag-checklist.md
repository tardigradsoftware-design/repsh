---
title: Practical WCAG Checklist
category: accessibility
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
tags: [accessibility, wcag]
---

# Practical WCAG Checklist (AA baseline)

> Verify current WCAG version guidance at W3C before compliance claims (2.2-lineage at verification).

## Perceivable
- [ ] Text alt for meaningful images; decorative marked aria-hidden
- [ ] Contrast: 4.5:1 body, 3:1 large text + UI components (per theme incl. dark)
- [ ] Content reflows at 320px width without loss; no information by color alone

## Operable
- [ ] All functionality keyboard-reachable; visible focus; no traps
- [ ] Skip link to main; focus management on route/modal change
- [ ] Timing adjustable; motion/autoplay pausable; reduced-motion honored

## Understandable
- [ ] lang attribute; consistent navigation; errors in text (not color/shape alone)
- [ ] Labels for every input; instructions not shape-dependent

## Robust
- [ ] Semantic HTML first; ARIA only to fill real gaps (no aria-soup)
- [ ] Status messages announced (toast/aria-live patterns)
- [ ] Name-role-value correct on custom widgets (Radix-class primitives do this for you)
