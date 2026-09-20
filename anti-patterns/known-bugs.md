---
title: Known Bugs & Gotchas (by error class)
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [debugging, gotchas]
---

# Known Bugs & Gotchas

## Next.js / React
- **Hydration mismatch** — `Date.now()`/`Math.random()`/locale formatting in shared render. Fix: deterministic rendering or client-only islands.
- **Server-only leak** — server module imported by client component pulls secrets into bundle. Fix: `server-only` package + architecture check.
- **Stale cache semantics** — caching defaults changed across majors; don't cargo-cult old config. Fix: verify current version docs.
- **`useEffect` fetch chains** — waterfalls + race conditions. Fix: server components/actions.

## Supabase / Postgres
- **RLS theater** — RLS enabled but `USING (true)`; missing `with check` on writes; views bypassing policies. Fix: role-matrix tests in CI (knowledge/databases/rls-patterns.md).
- **Service role in client** — catastrophic. Fix: server-only modules + secret scanning.
- **Missing composite index** `(tenant_id, …)` — list endpoints seq-scan at scale.

## Serverless platforms
- **Connection pool exhaustion** — per-lambda connections overwhelm Postgres. Fix: pooling proxy (pgbouncer/supavisor-class) + connection limits.
- **Long work in request** — platform timeout kills it silently. Fix: enqueue + 202.
- **Cold-start budget lies** — lab numbers on warm instances.

## TypeScript
- **`any` contagion** — one any at the boundary types the graph. Fix: unknown + narrowing.
- **enum/const misuse** — TS enums have runtime footguns; prefer const objects + unions.

## Playwright/E2E
- **Sleep-based waits** — flake factory. Fix: web-first assertions.
- **CSS-chain selectors** — break on restyle. Fix: role/label selectors.

## LLM apps
- **Prompt-injection via fetched content** — page content steers the agent. Fix: least-privilege tools + provenance.
- **Schema compliance decay** — long outputs drift from JSON contract. Fix: validate + bounded retries.
- **Undated model assumptions** — prompting for the wrong model family (see models/).
