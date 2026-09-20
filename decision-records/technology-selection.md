---
title: Technology Selection Matrices
updated: 2026-09-20
verified_at: 2026-09-20
---

# Technology Selection (working defaults + tradeoffs)

> Defaults validated 2026-09-20 against repositories/ records. Re-verify before commitment; conflicts → conflict-resolution format.

| Decision | Default | When to deviate | Key tradeoff |
|---|---|---|---|
| Next.js vs plain React | Next.js | pure SPA/embeds | framework weight vs built-in rendering/data |
| Postgres vs MongoDB | Postgres | document-heavy, schema-flex domains | relational integrity vs schema flexibility |
| Supabase vs Firebase | Supabase | deep mobile ecosystem needs | Postgres+RLS power vs Google mobile stack |
| Drizzle vs Prisma | Drizzle (SQL-first teams) / Prisma (schema-DX teams) | — | knowledge transfer vs DSL DX (knowledge/databases/orm-comparison) |
| REST vs GraphQL | REST + typed server functions | many diverse clients, nested queries | simplicity/cache vs query flexibility |
| Redis vs DB cache | DB cache first | rate-limiting/queues/sessions | infra vs capability |
| Vercel vs Cloudflare vs containers | Vercel (Next) → Cloudflare (edge-heavy) → containers (long tasks) | see knowledge/devops/platform-selection | platform limits vs control |
| Agent framework | pydantic-ai (Py, typed) / Mastra (TS) / LangGraph (stateful graph) / MS Agent Framework (.NET/enterprise) | see repositories/agent-frameworks/ records | type-safety vs graph-control vs ecosystem |
| Tailwind vs CSS-in-JS | Tailwind v4 + tokens | heavy theming/multi-brand runtime | token discipline vs runtime theming |
| shadcn/ui vs MUI-class | shadcn/ui (owned components) | teams wanting versioned component deps | ownership vs upgrade simplicity |
