---
title: Tenant Isolation Pattern (RLS-first)
category: database
confidence: high
updated: 2026-09-20
tags: [multi-tenancy, rls, postgres, security]
---

# Tenant Isolation Pattern

Full notes: `knowledge/databases/rls-patterns.md` + `multi-tenancy.md`. Pattern card:

```
tenants(id, ...)
memberships(user_id, tenant_id, role)     -- user ↔ tenant relation
<entity>_tables(..., tenant_id FK)        -- every tenant row carries tenant_id
RLS ENABLED + policies keyed on auth context → tenant_id
Indexes: (tenant_id, ...) leading column on hot paths
Service role: bypasses RLS — scoped to narrow server modules only
```

## Invariants
New tenant table ⇒ RLS + policies + index in the SAME migration (checklist-enforced).
Testing: role-matrix test suite (anon/user-tenant-A/user-tenant-B/service) runs in CI.
