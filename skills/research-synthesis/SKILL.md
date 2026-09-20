---
name: research-synthesis
version: 1.0.0
description: Combine multiple verified sources into a single honest answer — with confidence labels, conflicts surfaced, and limitations stated
category: research
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [research, synthesis, core]
requires: [web-research, source-validation, evidence-validation]
quality: { authority: 8, evidence: 8, recency: 8, adoption: 7, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# Research Synthesis

## Purpose
Move from "collected sources" to "defensible answer": weigh evidence, merge agreements, expose disagreements.

## When to Use
After web-research collection; writing any knowledge note or comparison in this repo; answering user questions with stakes.

## When NOT to Use
Single-fact lookups already validated.

## Inputs
Source set (validated), question to answer.

## Required Context
`standards/conflict-resolution.md`, `skills/evidence-validation`.

## Workflow
INPUT (sources) → PROCESS (cluster → weigh → merge → flag conflicts → conclude) → OUTPUT (synthesis) → VALIDATION (no claim without grade; conflicts visible)

## Research Phase
Cluster sources by claim. Weight: authority × recency × independence. Note funding/interest bias where relevant (vendor benchmarks!).

## Planning Phase
Decide: is evidence sufficient for HIGH? If not, say so — "insufficient evidence" is a valid, valuable answer.

## Implementation Phase
Structure: Answer → Evidence table (claim × sources × grades) → Conflicts → Limitations → Re-verify-by date. Never blend sources silently into one voice.

## Validation Phase
- [ ] Every sentence of the answer traceable to the table
- [ ] Conflicts in standard conflict format
- [ ] Limitations honest (n=1 benchmarks, vendor claims labeled)

## Failure Modes
False balance (treating a vendor blog equal to an official benchmark). Synthesis-by-majority (3 weak blogs ≠ 1 official doc). Hiding the one dissenting source.

## Quality Checklist
- [ ] Evidence table complete · [ ] grades assigned · [ ] limitations stated · [ ] re-verify date set

## Examples
"Is ORM X faster than Y?" → official benchmarks (dated) + independent tests + our EXPERIMENT note → answer scoped to workload with versions pinned.

## Anti-Patterns
Averaging scores across incompatible benchmarks. Presenting a synthesis as FACT when it's a RECOMMENDATION.

## References
standards/conflict-resolution.md · knowledge/research/

## Related Skills
web-research, evidence-validation, competitive-analysis

## Evaluation Criteria
A skeptical reviewer following citations reaches the same conclusion; conflicts are findable in the output.
