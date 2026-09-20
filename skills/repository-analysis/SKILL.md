---
name: repository-analysis
version: 1.0.0
description: Rapidly understand an unfamiliar codebase — architecture, conventions, risks — before modifying it
category: research
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [research, onboarding, architecture]
requires: []
quality: { authority: 8, evidence: 7, recency: 8, adoption: 8, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# Repository Analysis

## Purpose
Build an accurate mental model of a codebase before touching it: entry points, layering, conventions, test strategy, risk hotspots.

## When to Use
First session in any existing project; before large refactors; evaluating a third-party repo for adoption (feeds repositories/ records).

## When NOT to Use
Greenfield (nothing to analyze).

## Inputs
Repo checkout (or remote); docs; git history.

## Required Context
`skills/documentation` for producing the output note; `standards/agents-md.md` for checking/creating AGENTS.md.

## Workflow
INPUT (repo) → PROCESS (map → trace → conventions → risks → summarize) → OUTPUT (analysis note) → VALIDATION (predictions tested by reading key files)

## Research Phase
1. Read: README, AGENTS.md/CLAUDE.md, package/dependency manifests, CI config, LICENSE.
2. Map: entry points, route handlers, DB schema/migrations, env contract.
3. History: `git log --oneline -30` (activity), recent hot files, release tags.

## Planning Phase
Identify: layering rule (where does business logic live?), error-handling convention, test placement convention, dependency risk (abandoned? conflicting licenses?).

## Implementation Phase
Write `analysis.md`: architecture diagram (text), conventions list, "how to run/build/test", risk list, DO-NOT-TOUCH areas.

## Validation Phase
- [ ] Claimed conventions verified in ≥3 files
- [ ] Build + test commands actually run
- [ ] Risks concrete (file/line), not vibes

## Failure Modes
Pattern-matching one file into a "rule". Trusting stale READMEs over current code. Missing the second half of the monorepo.

## Quality Checklist
- [ ] Conventions evidence-backed · [ ] commands verified · [ ] risks located

## Examples
Next.js repo analysis finds: server actions pattern for mutations, Drizzle for DB, tests colocated `*.test.ts`, DO-NOT-TOUCH: generated `supabase/types.ts`.

## Anti-Patterns
Refactoring before analysis. Assuming framework defaults where the repo overrides them.

## References
standards/agents-md.md · skills/documentation

## Related Skills
documentation, research-before-code, code-review

## Evaluation Criteria
A second agent can onboard in <10 minutes using only the analysis note; stated conventions hold under spot-checks.
