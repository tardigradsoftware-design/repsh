---
title: Architecture Pattern Selection
category: architecture
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [architecture, patterns]
---

# Architecture Pattern Selection

| Pattern | Choose when | Avoid when |
|---|---|---|
| Monolith (modular) | default; team ≤ ~10; product-market fit not found | org genuinely independent-deploying |
| Microservices | independent scaling/teams/deploy cadence proven needs | resumé-driven design; small teams |
| Serverless/edge | spiky/low-traffic; global latency matters | long tasks; stateful connections; timeout walls |
| Event-driven | integration of many systems; audit/replay value | simple CRUD with one consumer |
| CQRS/ES | complex read/write asymmetry; audit as product | "might need it someday" |
| Hexagonal/clean | core domain logic worth isolating from I/O | thin CRUD wrappers over the DB |

## Defaults for this KB's audience (AI-built web/SaaS)
Modular monolith → deploy on managed platform → Postgres (+RLS) → queue for async work → edge/CDN for static. Introduce the fancy patterns with ADRs, not vibes. Named decisions live in `decision-records/`.
