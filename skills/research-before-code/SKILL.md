---
name: research-before-code
version: 1.0.0
description: Force research-first behavior — investigate the problem space, existing solutions, and proven patterns before writing any non-trivial code
category: meta
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [research, planning, decision-making, core]
requires: [source-validation, web-research]
quality:
  authority: 9
  evidence: 8
  recency: 9
  adoption: 9
  reproducibility: 9
  practical_value: 10
  maintenance: 9
---

# Research Before Code

## Purpose

Replace "start typing code from training-data memory" with a disciplined research phase that produces an evidence-backed plan. Agents that skip this hallucinate APIs, reinvent mature libraries, and bake in stale patterns.

## When to Use

- Any task estimated at >30 minutes of work or touching an unfamiliar library/framework/API
- New project setup, architecture decisions, technology selection
- Adding a dependency; integrating a third-party service; touching auth/payments/security
- When the user's request names a technology your knowledge may predate
- Debugging persistent failures (research the error class, not just the instance)

## When NOT to Use

- Trivial, fully-specified edits (rename, copy tweak, one-file CSS fix)
- Exploration spikes explicitly declared as throwaway (still timebox them)
- When the user explicitly says "just do it, don't research"

## Inputs

- Task description / user intent
- Target stack constraints (languages, frameworks, hosting, budget)
- This knowledge base: `indexes/topics.md`, `repositories/`, `decision-records/`, `anti-patterns/`
- Web access (search + official docs) when available

## Required Context

- `skills/source-validation` (to grade what you find)
- `skills/web-research` (search strategy)
- `decision-records/technology-selection.md` (known comparisons)
- `anti-patterns/` (known failure modes for the domain)

## Workflow

```
UNDERSTAND → SEARCH → COMPARE → VERIFY → PLAN → IMPLEMENT → TEST → REVIEW
```

## Research Phase

1. **UNDERSTAND** — restate the task in one sentence. List hard constraints (stack, deadline, compliance). List assumptions you are making; mark each `ASSUMPTION`.
2. **SEARCH** — for each major component, query in this order:
   - Official docs / organization repos (source_type: official)
   - This KB: `repositories/*.yaml` records (pre-verified, with tier + status)
   - Published benchmarks / papers if performance claims matter
   - High-quality community sources (only to cross-check, never alone)
3. **COMPARE** — for every "should I build or reuse?" decision answer, in order:
   - Does a mature library exist? A standard? A proven repo (check `repositories/` tier)? An MCP server? An established pattern (`patterns/`)? An official implementation?
   - Record each candidate with: version, license, maintenance status, last release.
4. **VERIFY** — run `source-validation` on every load-bearing source. Any single-source claim → `UNVERIFIED`. Conflicts → surface them explicitly in the plan.

## Planning Phase

Produce a short research note (commit alongside the work when non-trivial):

```markdown
# Research: <task>
Decision: <chosen approach>
Evidence: [source → confidence] × N
Alternatives rejected: <name> — why
Risks / unknowns: <list, each tagged ASSUMPTION or VERIFIED>
Reuse: <libraries/repos/MCPs adopted, with versions>
```

## Implementation Phase

- Implement against **verified current APIs** (check doc pages, not memory). If unsure an API exists → verify now.
- Prefer the smallest proven component over a custom build unless a recorded reason exists.
- Follow patterns from `patterns/` where they match.

## Validation Phase

- [ ] Every load-bearing decision cites ≥1 HIGH-or-better source
- [ ] No dependency added without license + maintenance check
- [ ] Plan written BEFORE implementation for anything non-trivial
- [ ] Assumptions that remained unverified are listed as risks for the user
- [ ] Tests pass; behavior matches the researched contracts

## Failure Modes

- **Research theater** — searching but not letting evidence change the plan. Counter: the plan must name what evidence changed your mind.
- **Paralysis** — researching forever on small tasks. Counter: timebox proportional to blast radius; trivial tasks skip straight to code.
- **Cache confusion** — trusting this KB's cached metadata past `expires_at`. Counter: check `verified_at`; re-verify if expired.
- **Awesomelist drift** — treating any list inclusion as endorsement. Counter: only `repositories/` records with `source_verified: true` count as pre-verified.

## Quality Checklist

- [ ] UNDERSTAND restatement done
- [ ] ≥2 independent sources for load-bearing claims
- [ ] Build-vs-reuse question explicitly answered
- [ ] License + maintenance recorded for every new dependency
- [ ] Research note committed

## Examples

- Task: "Add payments" → research: Stripe (official, S-tier in records) vs Paddle vs Lemon Squeezy → decision matrix → integration guide from official docs → implement → test webhooks with official CLI.
- Task: "State management" → check `decision-records/technology-selection.md` → default React built-ins (URL state → hooks; server state → server components/fetch cache) — document if deviating.

## Anti-Patterns

- Copying the first Stack Overflow answer without version check
- Using an API "as you remember it" without doc verification
- Adding a dependency because it was popular in training data (stars ≠ current truth — check `stars_checked_at`, maintenance status)

## References

- `skills/source-validation/SKILL.md` (grading sources)
- `standards/knowledge-priority.md` (source precedence order)
- `repositories/` (pre-verified repo database)

## Related Skills

source-validation, web-research, evidence-validation, repository-analysis

## Evaluation Criteria

A run of this skill passes when: (1) plan predates implementation, (2) every decision has cited evidence with confidence labels, (3) at least one build-vs-reuse tradeoff is explicit, (4) test phase validates against the researched contracts.
