---
name: performance-audit
version: 1.0.0
description: Web performance audit — Core Web Vitals, bundle/asset analysis, rendering bottlenecks with measured evidence
category: performance
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-09-20
content_type: RECOMMENDATION
tags: [performance, web-vitals, frontend, core]
requires: []
quality: { authority: 8, evidence: 9, recency: 8, adoption: 8, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# Performance Audit

## Purpose
Make pages fast with MEASURED evidence: Core Web Vitals as outcome metrics, targeted fixes at actual bottlenecks.

## When to Use
Before release; after heavy dependencies land; marketing/landing pages especially (SEO-coupled).

## When NOT to Use
Chasing 100/100 on internal tools where 95 is fine — state the budget instead.

## Inputs
URL or local build; target device class (mobile-first!); analytics if available.

## Required Context
`knowledge/performance/core-web-vitals.md` (verify current threshold definitions — Google revises), `knowledge/frontend/webgl-performance.md` for 3D pages.

## Workflow
INPUT (page) → PROCESS (measure → analyze → fix top offenders → re-measure) → OUTPUT (report + diffs) → VALIDATION (numbers improve, function intact)

## Research Phase
Measure on throttled mobile CPU/network (the median user, not your laptop). Capture LCP/INP/CLS + TTFB. Chrome DevTools MCP performance traces are ideal evidence (see knowledge/mcp/registry/chrome-devtools-mcp.yaml).

## Planning Phase
Rank fixes by measured impact: 1) LCP element (image? preload, right format/size) 2) JS payload (route-level code split, drop dead deps, tree-shake icons) 3) CLS (size media, no layout-shifting embeds) 4) INP (long tasks → chunk/defer).

## Implementation Phase
- Images: modern formats + explicit dimensions + priority hint for LCP.
- Fonts: subset + `font-display`; self-host when licensing allows.
- 3D/motion: lazy-init on interaction/visibility; degrade on mobile; honor reduced-motion.
- Data: stream what's ready; defer below-fold queries.

## Validation Phase
- [ ] Before/after metrics table (same throttle)
- [ ] No functional regressions (E2E suite green)
- [ ] Budget recorded for future diffs (e.g., LCP < 2.5s, route JS < 200KB gzip)

## Failure Modes
Micro-optimizing while shipping a 2MB hero image. Lab-only numbers ignoring field data. Fixing INP by breaking interactivity.

## Quality Checklist
- [ ] Measured twice · [ ] top-3 offenders addressed · [ ] budget documented

## Examples
Landing LCP 4.1s → hero PNG 1.8MB → AVIF 180KB + priority → 1.9s. Chart lib moved to dynamic import on scroll-into-view.

## Anti-Patterns
Lazy-loading the LCP image. Service-worker caching broken auth pages. Premature virtualization of 50-row tables.

## References
knowledge/performance/ · chrome-devtools-mcp (tracing evidence) · evaluations/web/

## Related Skills
frontend-implementation, browser-testing, website-quality-reviewer

## Evaluation Criteria
Report shows measured before/after on throttled profile; improvements hold in re-test; budgets written down.
