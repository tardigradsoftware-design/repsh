# Task 011 — "Design multi-tenant RLS policies for a Postgres SaaS"

## BASELINE output (no KB)
"Enable RLS on tenant tables and add policies like `create policy p on tasks using (tenant_id = current_setting('app.tenant_id')::uuid)`. Use the app to set the tenant per request. That isolates tenants."

## KB output (with retrieval — records used)
Cited: `knowledge/databases/rls-patterns.md`, `knowledge/databases/multi-tenancy.md`, `patterns/database/tenant-isolation-pattern.md`.

1. **Separate policies per operation** — SELECT (USING) + INSERT/UPDATE (**with check**, else tenant A writes into tenant B — the audit skill's most-flagged finding)
2. **Service-role reality:** `service_role` BYPASSES RLS — never client-side; scoped to narrow server modules
3. **Role-matrix test suite in CI** (anon / tenant-A user / tenant-B user / service) — RLS theater is the failure mode
4. **Performance:** wrap auth functions stable; composite indexes with tenant_id LEADING (`(tenant_id, project_id, created_at DESC)`); EXPLAIN per role, not as superuser
5. **Views bypass policies** → `security_invoker` views
6. **Model choice first:** shared-schema+RLS is the DEFAULT; schema/DB-per-tenant for compliance tiers (decision table cited)

## Scores
| Dimension | BASELINE | KB | Evidence |
|---|---|---|---|
| task completion | 2 | 2 | — |
| instruction following | 1 | 2 | — |
| tool correctness (with check, service role, security_invoker) | 1 | 2 | baseline: write-hole + service-role bypass unaddressed |
| planning quality | 1 | 2 | model-choice table + invariants in same-migration rule |
| self-correction | 1 | 2 | KB names its own failure modes explicitly |
| hallucination | 2 | 2 | baseline policies are syntactically fine |
| efficiency | 2 | 1 | — |
| safety | 1 | 2 | baseline design has exploitable write path |
| **Total** | **11** | **16** | — |
