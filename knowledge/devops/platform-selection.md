---
title: Deployment Platform Selection
category: devops
confidence: medium
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
tags: [devops, deployment]
---

# Deployment Platform Selection (web/SaaS shape)

| Platform | Sweet spot | Watch-outs |
|---|---|---|
| Vercel | Next.js-first, preview deploys, edge | function limits/timeout walls; egress costs |
| Cloudflare (Workers/Pages) | global edge, generous free tier, D1/R2/KV | runtime constraints (not full Node); cold starts tuning |
| Railway/Render/Fly | full servers, containers, long tasks | ops maturity lower than big clouds |
| AWS/GCP/Azure | compliance, scale, existing ecosystem | complexity tax; need platform skills |

## Default for this KB's audience
Vercel or Cloudflare for Next.js apps + Supabase (DB/auth/storage) + platform cron/queues. Move to containers (Fly/Railway) when long-running processes or heavy background compute appear. ADR per choice in `decision-records/`.

## Non-negotiables anywhere
Env contract documented · health checks · rollback tested · secrets in platform vault (never in repo) · preview-env parity with prod caveats written down.
