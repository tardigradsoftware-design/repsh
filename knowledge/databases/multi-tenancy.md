---
title: Multi-Tenancy Models
category: databases
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [multi-tenancy, saas, postgres]
---

# Multi-Tenancy: Choosing the Model

| Model | Isolation | Ops cost | When |
|---|---|---|---|
| Shared schema + tenant_id + RLS | Logical | Lowest | DEFAULT for SaaS; smallest tenants |
| Schema-per-tenant | Strong | Medium | Compliance middle-ground; ≤1000s tenants |
| Database-per-tenant / cluster-per-tier | Strongest | Highest | Enterprise/regulatory tiers; noisy-neighbor escape |

## Decision inputs
Compliance promises (SOC2/ISO scope, data residency), tenant size skew, per-tenant backup/restore requirements, migration blast radius, price tier economics.

## Shared-schema rules (the default)
- tenant_id on EVERY tenant row; FK to tenants; RLS enforced (see rls-patterns.md)
- Global tables (plans, features) explicit and reviewed — no tenant data hiding there
- Per-tenant resource limits (rate limits, quotas) at app layer; watch hot-tenant noisy neighbors on shared indexes
- Cross-tenant analytics → separate replica/pipeline, never live OLTP queries over all tenants from app paths

## Migration & ops
- One migration pipeline; test with representative multi-tenant data volumes
- Tenant-level restore strategy defined BEFORE enterprise asks for it
