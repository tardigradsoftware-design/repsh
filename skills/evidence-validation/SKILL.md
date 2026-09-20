---
name: evidence-validation
version: 1.0.0
description: Separate fact from recommendation from fabrication — grade claims (SUPPORTED/PARTIALLY/UNSUPPORTED/CONFLICTING) with cited evidence
category: meta
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [research, validation, fact-checking]
requires: [source-validation]
quality:
  authority: 9
  evidence: 9
  recency: 9
  adoption: 7
  reproducibility: 10
  practical_value: 9
  maintenance: 9
---

# Evidence Validation

## Purpose
Prevent AI-generated assertions from entering the record as facts. Every claim gets a status + evidence trail.

## When to Use
- Writing any knowledge note, README claim, or comparison in this repo
- Fact-checking agent output before delivery to a user
- Reviewing model/benchmark claims

## When NOT to Use
- Explicitly labeled opinions/hypotheses (must still be LABELED as such)

## Inputs
A set of claims (sentences or bullet points).

## Required Context
`skills/source-validation`, `agents/fact-checker`, `standards/conflict-resolution.md`.

## Workflow
INPUT (claims) → PROCESS (classify → evidence search → grade) → OUTPUT (graded claim table) → VALIDATION (no untagged claims remain)

## Research Phase — claim classes
FACT (verifiable, external) / RECOMMENDATION (our judgment) / EXPERIMENT (measured here) / OPINION / HYPOTHESIS / UNKNOWN.
Grade vs evidence: SUPPORTED · PARTIALLY_SUPPORTED · UNSUPPORTED · CONFLICTING · UNKNOWN.

## Planning Phase
For each FACT: find ≥2 independent sources (official + 1 more for HIGH). Benchmarks: check date + contamination notes in `evaluations/`.

## Implementation Phase
Output format:
```markdown
| Claim | Grade | Evidence | Confidence |
|---|---|---|---|
| X does Y | SUPPORTED | official docs; repo tests | HIGH |
| X is fastest | PARTIALLY_SUPPORTED | benchmark A (2026-01, v3.2) | MEDIUM — dated |
```
GENERATED-tag anything you produced without external evidence.

## Validation Phase
- [ ] Zero ungraded claims left
- [ ] Every SUPPORTED has working citations
- [ ] Dated benchmark claims include measured-date + version
- [ ] Conflicts surfaced, not resolved silently

## Failure Modes
- Citation theater (citing sources that don't contain the claim)
- Recency laundering (citing an old benchmark as current)
- Consensus mimicry ("everyone knows X" without a source)

## Quality Checklist
- [ ] Table complete · [ ] grades defensible · [ ] dates on volatile claims

## Examples
"AutoGen is deprecated" → PARTIALLY_SUPPORTED: not archived, but maintenance-mode + vendor directs new work to Agent Framework (sources: microsoft/agent-framework README, autogen repo status, checked 2026-09-20).

## Anti-Patterns
Marking model-generated guesswork as FACT. Hiding CONFLICTING grades to seem decisive.

## References
standards/conflict-resolution.md · agents/fact-checker/

## Related Skills
source-validation, web-research, research-synthesis

## Evaluation Criteria
Graded claim table where every grade is reproducible by a second reviewer using only the cited evidence.
