---
name: database-design
version: 1.0.0
description: Relational schema design — modeling, indexing, RLS, multi-tenancy, migrations with Postgres-first discipline
category: database
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
content_type: RECOMMENDATION
tags: [database, postgres, rls, saas, drizzle, supabase]
requires: [research-before-code]
quality: { authority: 8, evidence: 8, recency: 9, adoption: 9, reproducibility: 9, practical_value: 10, maintenance: 8 }
---

# Database Design

## Purpose
Schemas that stay correct and fast as the product grows: right keys, right indexes, right tenancy model, safe migrations.

## When to Use
Any persistent data modeling; multi-tenant SaaS especially.

## When NOT to Use
Trivial key-value needs already solved by the platform.

## Inputs
Domain entities, access patterns (which queries run at what frequency), tenancy requirements.

## Required Context
`knowledge/databases/postgres-schema-design.md`, `knowledge/databases/rls-patterns.md`, `knowledge/databases/multi-tenancy.md`, `knowledge/databases/orm-comparison-drizzle-prisma.md`.

## Workflow
INPUT (entities + access patterns) → PROCESS (model → normalize → index → secure → migrate) → OUTPUT (schema + migrations) → VALIDATION (query plan review, RLS tests, migration dry-run)

## Research Phase
Default stack: PostgreSQL (Supabase when BaaS fits) + Drizzle (SQL-first) or Prisma (schema-first DX) — current comparison in decision-records. Verify ORM current major + driver notes (Prisma renamed prisma/orm; verify package names today).

## Planning Phase
- Model from ACCESS PATTERNS, not just entities: list the top queries first.
- Tenancy choice: shared-schema + `tenant_id` + RLS (default) vs schema-per-tenant vs DB-per-tenant (see knowledge note).
- Every FK gets an index; every hot query path gets a covering/partial index.

## Implementation Phase
- `uuid` or `bigint` PKs consciously chosen; timestamps `timestamptz`; money in minor units + currency; soft-delete via `deleted_at` only when required.
- Migrations: forward-only, reviewed, reversible plan noted; never edit applied migrations.
- RLS: enable by default on tenant tables in Supabase; test the BYPASS risk (service role).

## Validation Phase
- [ ] EXPLAIN on top queries (no sequential scans on hot paths)
- [ ] RLS tested as anon + authenticated + service roles
- [ ] Migration applied on staging clone
- [ ] Backfill strategy for new NOT NULL columns

## Failure Modes
Missing composite indexes for (tenant_id, created_at) list queries. RLS "enabled" but policies `USING (true)` (theater). Editing migration files after apply.

## Quality Checklist
- [ ] Access patterns drove design · [ ] FKs indexed · [ ] RLS tested per role · [ ] migrations reviewed

## Examples
Multi-tenant tasks: `tasks(id, tenant_id, project_id, title, status, created_at)` + index `(tenant_id, project_id, created_at)` + RLS policy `tenant_id = auth.jwt() ->> 'tenant_id'`.

## Anti-Patterns
EAV "flexible" schemas. JSONB for everything relational. Premature sharding.

## References
knowledge/databases/ · repositories/databases/ · patterns/database/

## Related Skills
backend-engineering, security-audit, api-design

## Evaluation Criteria
Top-5 access patterns have EXPLAIN-verified plans; RLS matrix test passes for all roles; migration history is linear and reviewed.
