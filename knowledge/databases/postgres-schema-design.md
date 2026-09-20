---
title: PostgreSQL Schema Design
category: databases
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [postgres, database, indexing]
---

# Postgres Schema Design

## Types & keys
- `timestamptz` always; `numeric` for money or integer minor units + currency code; `uuid` v7 or `bigint identity` for PKs (v7 sorts by time — index friendly).
- Text: `text` + CHECK constraints over magic lengths; enums via lookup tables or PG enums when stable.
- JSONB for genuinely schemaless bits; never as the default dumping ground.

## Indexing discipline
- Every FK indexed. Composite indexes match query shape: `(tenant_id, project_id, created_at DESC)` for list screens.
- Partial indexes for hot filtered subsets (`WHERE status = 'active'`).
- Covering (`INCLUDE`) to skip heap fetches on hot paths. Verify with EXPLAIN (ANALYZE, BUFFERS).

## Query optimization
- Kill N+1 at the ORM layer (joins/batching); watch `rows` vs `loops` in plans.
- Pagination: keyset (`WHERE created_at < $cursor`) over OFFSET at scale.
- Index bloat/dead tuples: monitor; autovacuum tuning is a real production task.

## Migrations
- Forward-only; expand-migrate-contract for zero-downtime; NEVER edit applied migrations.
- Backfills in batches (avoid long locks); `NOT NULL` additions via backfill+constraint steps.
