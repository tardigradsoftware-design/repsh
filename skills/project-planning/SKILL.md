---
name: project-planning
version: 1.0.0
description: Task decomposition and milestone planning — requirements → scope → milestones → risks, with explicit assumptions
category: planning
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [planning, core, requirements]
requires: [research-before-code]
quality: { authority: 8, evidence: 7, recency: 8, adoption: 8, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# Project Planning

## Purpose
Turn a vague request into an executable plan with explicit scope, sequence, and risks — so implementation agents don't improvise requirements.

## When to Use
Any multi-day feature; new project kickoff; ambiguous requests ("build me a SaaS").

## When NOT to Use
Single-session tasks (one-paragraph plan inline is enough).

## Inputs
User goals, constraints (time/budget/stack), success criteria.

## Required Context
`workflows/build-website/` for web projects; `decision-records/technology-selection.md`.

## Workflow
INPUT (goal) → PROCESS (requirements → scope → milestones → risks) → OUTPUT (plan doc) → VALIDATION (each milestone demo-able)

## Research Phase
- Requirements: functional list + NON-functional (perf, security, compliance) + explicit out-of-scope list.
- Surface assumptions: every "the user probably wants X" gets written down and confirmed for big bets.

## Planning Phase
- Milestones that each end in something demo-able (walking skeleton first, then depth).
- Sequence by risk: riskiest unknowns earliest.
- Definition of done per milestone (tests? deploy? review?).

## Implementation Phase
Track as issues/checklist; plan lives in-repo (`docs/plan.md` or issues), not in chat history.

## Validation Phase
- [ ] Every requirement traceable to a milestone
- [ ] Out-of-scope explicit
- [ ] Risks have mitigations or accepted-by decisions

## Failure Modes
Planning the happy path only (no auth/error/empty states = incomplete product). Big-bang milestones that demo nothing for weeks. Scope silent-assumption growth.

## Quality Checklist
- [ ] Non-functionals included · [ ] out-of-scope listed · [ ] milestones demo-able · [ ] assumptions confirmed

## Examples
SaaS MVP plan: M1 auth+tenancy skeleton deployed, M2 core entity CRUD + RLS, M3 payments + billing states, M4 polish/a11y/perf pass. Each demo-able.

## Anti-Patterns
Estimating in fantasy precision. Planning UI polish before data model settles.

## References
workflows/build-website/ · decision-records/

## Related Skills
requirements-analysis (embedded), research-before-code, documentation

## Evaluation Criteria
Plan review: a stranger could execute M1 without asking a question; risks each have an owner-action.
