---
title: Frontend Stack Recommendations (9 Profiles)
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
tags: [frontend, stack, selection]
---

# Frontend Stack Profiles

Components verified 2026-09-20 (repositories/frontend/ records). Versions move — re-verify at project start.

## 1. Recommended default (most projects)
Next.js + TypeScript strict + Tailwind v4 + shadcn-ui/ui + Drizzle + Postgres (Supabase) + Vercel. Motion: `motion`.
WHY: one coherent, hireable, AI-agent-friendly path. TRADEOFF: Vercel-coupled conventions.

## 2. Small project / MVP
Next.js + TypeScript + Tailwind + shadcn + Supabase (auth+DB+storage) on Vercel free tier. Skip: custom design system, queues, Redis.
TRADEOFF: migration debt if it grows big — acceptable, token discipline keeps options open.

## 3. Startup (product-market-fit track)
Default stack + PostHog-class analytics + Stripe + background jobs (platform cron / Inngest-class) + error tracking (Sentry).
TRADEOFF: vendor sprawl — keep env contract documented from day 1.

## 4. Enterprise / B2B
Default stack + NestJS-class API tier where teams/COMPLIANCE demand separation + MS Entra/Okta SSO + audit logging + on-prem/VPC Postgres option.
TRADEOFF: velocity cost; justified by procurement/security requirements.

## 5. Data-heavy app
Next.js + TanStack/table (server-side: sort/filter/keyset pagination) + columnar warehouses via API (not direct OLTP) + virtualized lists + charts lazy-loaded.
WHY: tables break naive client pagination at ~10k rows. TRADEOFF: server-state complexity.

## 6. Marketing website
Next.js static/ISR + Tailwind + minimal JS + GSAP ScrollTrigger (one hero moment) or pure CSS + CMS (MDX/Sanity-class).
WHY: LCP is everything. TRADEOFF: motion budget must stay tiny.

## 7. 3D website
Next.js + three.js via @react-three/fiber + GSAP timeline + static poster fallback + interaction-gated scene init.
TRADEOFF: mobile GPU budgets (knowledge/frontend/webgl-performance.md); fail-open to static.

## 8. AI SaaS
Default + AI SDK-class streaming (SSE) + pydantic-ai/mastra backend agent tier + promptfoo in CI + Langfuse-class tracing + model-abstraction layer (dated model policy — models/).
TRADEOFF: token cost engineering becomes a product concern.

## 9. B2B SaaS (dashboard-dense)
Default + multi-tenancy from day 1 (RLS — knowledge/databases/) + command palette + saved views/export + granular RBAC + white-label tokens.
TRADEOFF: theming discipline (design tokens) is non-negotiable or white-label rots.
