---
title: Core Web Vitals Working Notes
category: performance
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-09-20
tags: [performance, web-vitals]
---

# Core Web Vitals

> THRESHOLDS RE-VERIFY POLICY: Google revises CWV definitions/thresholds; check web.dev before quoting exact numbers (this note verified 2026-09-20, expires soon by design).

## The three (outcome metrics, field data first)
- **LCP** — largest contentful paint: hero image/font/render path. Fix: priority hints, right-sized modern formats, edge caching.
- **INP** — interaction to next paint: worst-case interaction feel. Fix: break long tasks, defer hydration work, reduce client JS.
- **CLS** — cumulative layout shift. Fix: explicit dimensions, reserved space for embeds/ads/fonts.

## Measurement hierarchy
Field data (RUM) > lab throttle (Lighthouse/DevTools) > nothing. Lab is for debugging; field is truth.

## Practice
Budgets per page type recorded at project start (see performance-audit skill); CI checks bundle-size deltas; panic threshold documented.
