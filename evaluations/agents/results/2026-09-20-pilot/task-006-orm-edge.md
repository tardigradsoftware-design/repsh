# Task 006 — Choose an ORM for an edge-deployed app

## Task prompt
"Choose an ORM for an edge-deployed TypeScript app. Recommend one."

## BASELINE output (no KB)
"Prisma is the most popular TypeScript ORM with great DX. For edge, use Prisma Driver Adapters or Prisma Accelerate. Drizzle is a lighter alternative popular for edge because it doesn't need an engine. Either works; Prisma if you want schema-first DX, Drizzle if you like SQL."

## KB output (with retrieval — records used)
Cited records: `repositories/databases/prisma_orm.yaml` (ACTIVE, HIGH confidence, verified 2026-09-20, notes repo renamed prisma/prisma → prisma/orm), `knowledge/databases/orm-comparison-drizzle-prisma.md`, `decision-records/technology-selection.md`.

**Decision: Drizzle** — edge-first driver story without an engine dependency; SQL-first types fit serverless/edge cold-start budgets.
**Acceptable alternative:** Prisma WITH driver adapters — verify the CURRENT adapter state for your exact edge runtime before committing (comparison note is version-dated 2026-09-20, expires 2026-12-20).
**Verification steps required (per research-before-code skill):** (1) confirm npm package names today — repo rename means `prisma/client` etc. must be checked against the registry at install time; (2) confirm the target platform's runtime compatibility page; (3) record the choice in an ADR (decision-records/adr-template.md) with a revisit-by date.

## Scores
| Dimension | BASELINE | KB | Evidence |
|---|---|---|---|
| task completion | 2 | 2 | both recommend an ORM |
| instruction following (suite: dated evidence required) | 1 | 2 | KB carries verified_at/expires_at; baseline undated |
| tool correctness (KB discipline) | 0 | 2 | baseline unaware of rename verification need |
| planning quality | 1 | 2 | KB adds verification steps + ADR |
| self-correction | 1 | 2 | KB flags its own note's expiry |
| hallucination | 2 | 2 | no false claims in either |
| efficiency | 2 | 1 | retrieval costs tokens |
| safety | 2 | 2 | — |
| **Total** | **11** | **16** | — |
