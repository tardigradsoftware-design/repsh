---
title: Next.js App Router Patterns
category: frontend
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
tags: [nextjs, react, frontend]
---

# Next.js App Router Patterns

> Version-sensitive note. Verified against official docs 2026-09-20. Next.js majors ship breaking changes — ALWAYS re-verify current behaviors at nextjs.org/docs before implementing (the KB record `repositories/frontend/vercel_next.js.yaml` tracks activity).

## Server-first rules
- Server Components by default; `"use client"` only for interactivity/state/effects.
- Data fetching: server components (async/await) or server actions; not useEffect+fetch chains.
- Mutations: server actions with zod-style validation + revalidatePath/revalidateTag.
- Keep secrets server-side; never pass service keys across the RSC boundary.

## State ladder (preference order)
1. URL (searchParams/params) — shareable, restorable: filters, tabs, pagination
2. Server cache (fetch cache, revalidate) — cross-user data
3. React state — ephemeral UI only
Everything in client state management libs first = the classic App Router mistake.

## Layout & composition
- layout.tsx for shells (sidebar persists across routes — no re-render churn)
- Route groups `(marketing)` vs `(app)` for different shells
- loading.tsx/streaming Suspense for progressive delivery; error.tsx per segment
- Parallel + intercepting routes for modal-over-page patterns

## Performance hooks
- next/image with priority for LCP; font optimization built-in
- Dynamic import below-fold/interaction-gated heavy clients (charts, editors)
- Route-level code splitting is automatic — don't fight it with giant client barrels

## Gotchas (see anti-patterns/known-bugs.md)
- Hydration mismatch: no Date.now()/Math.random() in shared render paths
- Server-only imports leaking into client bundles ("server-only" package)
- Caching semantics changed across majors — verify current defaults per version
