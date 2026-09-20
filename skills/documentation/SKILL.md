---
name: documentation
version: 1.0.0
description: Writing docs that stay true — READMEs, runbooks, ADRs, and knowledge notes with verification dates and audience discipline
category: documentation
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [documentation, core]
requires: []
quality: { authority: 7, evidence: 7, recency: 8, adoption: 8, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# Documentation

## Purpose
Docs a stranger (human or agent) can act on: right depth per audience, verified commands, dated volatile facts.

## When to Use
Any new project (README+AGENTS.md), any non-obvious decision (ADR), any knowledge note in this repo.

## When NOT to Use
Docs for their own sake — if nothing acts differently after reading it, don't write it.

## Inputs
Working code/decisions; verified facts.

## Required Context
This repo's own README/AGENTS.md as format exemplars; `standards/agents-md.md`.

## Workflow
INPUT (subject) → PROCESS (audience → outline → draft → verify commands → date volatile facts) → OUTPUT (doc) → VALIDATION (every command runs; every volatile fact dated)

## Research Phase
Inventory what EXISTS before writing (docs drift when written from intention instead of code).

## Planning Phase
Audience first: operator (runbooks), developer (setup+architecture), agent (AGENTS.md), future-self (ADRs). One doc = one audience.

## Implementation Phase
- Commands in copy-paste blocks, verified by RUNNING them.
- Volatile facts (versions, counts, links to live dashboards) dated `as of YYYY-MM-DD`.
- ADRs: context → decision → consequences → alternatives rejected.

## Validation Phase
- [ ] Every command executed successfully
- [ ] Links resolve (CI checks this repo's docs)
- [ ] No undated volatile claims

## Failure Modes
README theater (quickstart that never worked). Undocumented "temporary" hacks surviving years. Version-less instructions.

## Quality Checklist
- [ ] Commands verified · [ ] dated facts · [ ] single audience per doc

## Examples
ADR-007: chose Drizzle over Prisma for edge-runtime driver support; consequences recorded; alternatives rejected with reasons + revisit-by date.

## Anti-Patterns
Auto-generated docs nobody reads. Screenshots-of-UIs-that-already-changed without dates. Docs claiming "simple" three-step processes that are actually nine steps.

## References
standards/agents-md.md · CHANGELOG.md conventions

## Related Skills
repository-analysis, project-planning, research-synthesis

## Evaluation Criteria
A fresh agent completes setup+first-task using only the doc; every command works as written.
