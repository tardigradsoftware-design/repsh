---
name: code-review
version: 1.0.0
description: Structured code review — correctness, security, architecture fit, test quality, with actionable severity-ranked feedback
category: quality
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [review, quality, core]
requires: []
quality: { authority: 8, evidence: 7, recency: 8, adoption: 9, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# Code Review

## Purpose
Reviews that change outcomes: every finding is specific, severity-ranked, and either fixed or consciously waived.

## When to Use
Before merging any non-trivial change; reviewing AI-generated code (mandatory — never trust, always review).

## When NOT to Use
Style-only nitpicks on working code (automate those instead).

## Inputs
Diff, linked issue/spec, test results.

## Required Context
`knowledge/coding/review-checklist.md`; security-audit for auth/data paths.

## Workflow
INPUT (diff) → PROCESS (understand intent → correctness → security → design → tests → readability) → OUTPUT (severity-ranked findings) → VALIDATION (findings resolved or waived with reason)

## Research Phase
Understand WHAT the change claims to do before HOW it does it. Run the tests. Check `anti-patterns/` for the touched area.

## Planning Phase — finding severities
BLOCKER (breaks/must not merge) · MAJOR (correctness/security/perf risk) · MINOR (maintainability) · NIT (taste — batch or drop).

## Implementation Phase
Per finding: file:line + what breaks + concrete suggestion. Questions when intent is unclear — don't assume.

## Validation Phase
- [ ] Tests actually test the new behavior
- [ ] No new deps without license/maintenance check (cross-check repositories/ records)
- [ ] Security-sensitive paths reviewed with security-audit lens
- [ ] All BLOCKER/MAJOR resolved before merge

## Failure Modes
Rubber-stamping AI code ("looks fine"). Reviewing line-by-line but missing the architectural mismatch.nitpick floods burying real issues.

## Quality Checklist
- [ ] Intent understood · [ ] tests verified meaningfully · [ ] deps checked · [ ] severity discipline kept

## Examples
PR adds webhook handler: found missing signature verification (BLOCKER), non-idempotent insert (MAJOR), else-branch unreachable (MINOR) — each with line refs and fixes.

## Anti-Patterns
"LGTM" without running tests. Rewriting someone's architecture in review comments instead of discussing first.

## References
knowledge/coding/review-checklist.md · skills/security-audit · anti-patterns/

## Related Skills
security-audit, testing, debugging

## Evaluation Criteria
Injected bugs (auth bypass, race, leak) in review samples are caught with correct severities and actionable fixes.
