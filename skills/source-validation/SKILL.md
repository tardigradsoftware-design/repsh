---
name: source-validation
version: 1.0.0
description: Verify external sources before trusting or recording them — existence, license, maintenance, adoption, and claim support
category: meta
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [research, validation, core]
requires: []
quality:
  authority: 9
  evidence: 9
  recency: 9
  adoption: 8
  reproducibility: 10
  practical_value: 10
  maintenance: 9
---

# Source Validation

## Purpose
Grade any external source (repo, doc, paper, blog, MCP, dataset) BEFORE it influences a decision or enters this knowledge base.

## When to Use
- Before adding ANY record to `repositories/`, `knowledge/`, `sources/`, `evaluations/`
- Before relying on a Stack Overflow/blog snippet for load-bearing code
- Before trusting this KB's own cached records (check `expires_at` first!)

## When NOT to Use
- Casual background reading that won't influence output

## Inputs
URL(s) + the claim(s) they are supposed to support.

## Required Context
`standards/knowledge-priority.md`, `schemas/source.schema.json`.

## Workflow
INPUT (url, claim) → PROCESS (12-point check) → OUTPUT (validated record w/ confidence) → VALIDATION (cross-check count ≥2 for HIGH)

## Research Phase — the 12-point check
1. URL resolves (HTTP 200, not a redirect to a parked domain)
2. Repo/resource actually exists as described
3. Archived? (GitHub API `archived` flag)
4. Last commit/push date ( staleness bands: ≤30d active, ≤120d regular, ≤365d sporadic, else stale)
5. License present? Which SPDX? No-license = no-reuse
6. Who maintains it (org? individual? abandoned?)
7. Stars/forks (adoption signal ONLY — never quality proof alone)
8. Security policy / recent advisories
9. Documentation quality (can you actually reproduce the setup?)
10. Reproducibility: can the claim be independently tested?
11. Independent corroboration: ≥2 credible sources agree?
12. Does the content actually DO what it claims (smoke-test, don't assume)?

## Planning Phase
Assign: `source_type` (official/research-paper/github-repository/blog/discussion/…), `confidence` (VERY HIGH…CONFLICTING), `verified_at`, `expires_at` (models 7–30d, tools 30–60d, frameworks 30–90d, papers 180–365d, specs 365d+).

## Implementation Phase
Record per schema. Single-source claims stay LOW/UNVERIFIED. Conflicts recorded in conflict format (Source A says X, Source B says Y, likely explanation, current recommendation).

## Validation Phase
- [ ] All 12 checks recorded or explicitly N/A'd
- [ ] Confidence consistent with evidence count
- [ ] expires_at set
- [ ] No claim recorded beyond what the source states

## Failure Modes
- Star-blindness (treating popularity as verification)
- Wayback laundering (citing dead pages as live)
- License optimism (assuming MIT without checking)

## Quality Checklist
- [ ] 12 checks done · [ ] confidence justified · [ ] dated + expiring

## Examples
Verifying `microsoft/autogen` (2026-09-20): exists, NOT archived, last push 2026-04 → status MAINTENANCE, notes successor = microsoft/agent-framework. Recorded with confidence HIGH and not_recommended_for new projects.

## Anti-Patterns
Recording a repo because a list mentioned it. Trusting `archived: false` as "active" without push dates.

## References
standards/knowledge-priority.md · schemas/source.schema.json · scripts/validate/

## Related Skills
evidence-validation, web-research, research-before-code

## Evaluation Criteria
Given 5 URLs (one dead, one archived, one license-less, one conflicting), the skill correctly classifies all 5 with correct confidence labels.
