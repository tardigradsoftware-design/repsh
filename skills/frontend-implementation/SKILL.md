---
name: frontend-implementation
version: 1.0.0
description: Verified-stack frontend implementation — Next.js + TypeScript + Tailwind + shadcn/Radix with current-API discipline
category: frontend
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
content_type: RECOMMENDATION
tags: [frontend, nextjs, react, typescript, tailwind]
requires: [frontend-design, research-before-code]
quality: { authority: 9, evidence: 9, recency: 9, adoption: 10, reproducibility: 9, practical_value: 10, maintenance: 9 }
---

# Frontend Implementation

## Purpose
Implement UI against verified current APIs of the recommended stack — no stale patterns, no hallucinated props.

## When to Use
Building/modify web apps in the recommended stack (see decision-records/technology-selection.md: Next.js default, React 19+, TypeScript strict, Tailwind v4, shadcn-ui/ui, motiondivision/motion).

## When NOT to Use
Projects pinned to other stacks (follow THEIR current docs; verify versions first).

## Inputs
Design tokens + component inventory (from frontend-design), data contracts.

## Required Context
`repositories/frontend/*.yaml` (versions + status, checked 2026-09-20); `knowledge/frontend/nextjs-app-router-patterns.md`; `patterns/frontend/`.

## Workflow
INPUT (design, contracts) → PROCESS (verify APIs → scaffold → components → wire data → polish) → OUTPUT (app) → VALIDATION (types, tests, a11y, screenshots)

## Research Phase
1. Confirm current major versions + breaking changes via official release notes (Next/React/Tailwind move fast; records say React canonical repo is now `react/react` — use official docs).
2. Verify every third-party component's install name (typosquat check) from the official repo.

## Planning Phase
Route map (app router); server/client component split; data fetching points; state strategy (URL → server → client, in that preference order).

## Implementation Phase
- Server Components by default; `"use client"` only for interactivity.
- TypeScript strict; no `any` without a recorded reason.
- Forms: server actions or route handlers + zod-style validation; optimistic UI where cheap.
- Data tables: TanStack/table; command palette for app navigation.
- Motion: `motion` for React physics/entrances; GSAP ScrollTrigger only for scroll storytelling.

## Validation Phase
- [ ] `tsc --noEmit` clean
- [ ] Key flows tested (testing skill)
- [ ] Lighthouse-style perf sanity on heaviest page
- [ ] Responsive + reduced-motion checked
- [ ] No deprecated API usage (verify warnings, don't ignore)

## Failure Modes
Using App Router like Pages Router (old data-fetch habits). Hydration mismatches from non-deterministic client renders. Bundle bloat from client-side everything.

## Quality Checklist
- [ ] Versions verified today · [ ] strict TS · [ ] server-first data · [ ] states designed

## Examples
SaaS dashboard: layout.tsx shell (sidebar via server component), table page streams data, filter state in URL searchParams (shareable), ⌘K palette client component.

## Anti-Patterns
`useEffect` fetch chains instead of server components/actions. Copying old blog tutorials for current versions.

## References
knowledge/frontend/ · repositories/frontend/ · decision-records/technology-selection.md

## Related Skills
frontend-design, testing, performance-audit, accessibility-audit

## Evaluation Criteria
App compiles strict, follows current-API patterns (verified against official docs during the run), passes validation checklist, no deprecated usage.
