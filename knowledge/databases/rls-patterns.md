---
title: Row-Level Security Patterns
category: databases
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [postgres, rls, security, supabase, multi-tenancy]
---

# Row-Level Security (RLS) Patterns

Primary defense for tenant isolation in Supabase/Postgres SaaS. The audit skill tests this — RLS theater is our most-flagged finding class.

## Non-negotiables
- RLS ENABLED on every tenant table; **no policy is deny-by-default** — a missing policy on a new table = invisible to clients (safe) but `USING (true)` = open (unsafe). Review policies, not just the RLS flag.
- Test the full role matrix: anon, authenticated, other-tenant authenticated, service role.

## Canonical policy set
```sql
alter table tasks enable row level security;

create policy "tasks_select_own_tenant" on tasks
  for select using (tenant_id = (auth.jwt() -> 'app_metadata' ->> 'tenant_id')::uuid);

-- separate policies per operation; write policies check BOTH using and with check
create policy "tasks_insert_own_tenant" on tasks
  for insert with check (tenant_id = (auth.jwt() -> 'app_metadata' ->> 'tenant_id')::uuid);
```

## Service role reality
`service_role` BYPASSES RLS — that's its purpose. Rules: never in client code, never in browser-exposed edge functions without reason, scope its use in server code to narrow modules.

## Performance
- Wrap auth functions `select`-stable; index tenant_id (leading column of composites); RLS adds predicate to every query — EXPLAIN with roles, not just as superuser.
- Complex authorization (roles/sharing) → policy functions in SECURITY DEFINER SQL (kept minimal + audited), or push to app layer for exotic cases.

## Failure modes (real audits)
- `USING (true)` "temporarily". Policies for select but forgot `with check` on update → tenant A writes into tenant B. Views bypassing RLS (use `security_invoker` views). New table forgotten in the policy sweep.
