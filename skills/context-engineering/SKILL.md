---
name: context-engineering
version: 1.0.0
description: Give AI the right information at the right time — selection, compression, progressive disclosure, and pollution control
category: ai-engineering
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
content_type: RECOMMENDATION
tags: [context, retrieval, core, agents]
requires: []
quality: { authority: 8, evidence: 8, recency: 9, adoption: 9, reproducibility: 8, practical_value: 10, maintenance: 8 }
---

# Context Engineering

## Purpose
Optimize what enters the model's window: not "more context" but the RIGHT context at the RIGHT moment, structured for retrieval.

## When to Use
Designing any agent/feature that assembles context; building RAG; writing knowledge files (like this repo!); fixing "the model keeps forgetting/ignoring X".

## When NOT to Use
Single-shot prompts with trivial inputs.

## Inputs
Task types, corpus structure, token budget, latency constraints.

## Required Context
`knowledge/context-engineering/context-packing.md`, `knowledge/context-engineering/long-context-failures.md`; this repo's progressive-disclosure design (AGENTS.md §5) as reference implementation.

## Workflow
INPUT (task) → PROCESS (select → structure → compress → reserve → assemble) → OUTPUT (context payload) → VALIDATION (utilization check — was the context actually used?)

## Research Phase
Inventory knowledge sources and their trust grades; identify per-task minimal context sets (measure: what does the model cite/use?).

## Planning Phase
- Layer context: persistent identity/rules (small, stable) → task dossier (medium) → on-demand detail (retrieved just-in-time).
- Reserve output headroom; put instructions at boundaries; repeat critical constraints at the END for long contexts (recency).

## Implementation Phase
- Progressive disclosure: index → summary → section → full doc (this repo's pattern).
- Compression: extractives over summaries for facts (summaries drop specifics).
- Pollution control: drop irrelevant-but-impressive content; mark provenance so the model can weigh trust.

## Validation Phase
- [ ] Model cites/uses the provided context (trace check)
- [ ] No context component that never gets used (dead weight)
- [ ] Failure analysis on long-context cases (lost-in-middle checks)

## Failure Modes
Stuffing everything "to be safe" → attention dilution. Instructions at position 0 in 100k contexts getting lost. Stale cached context contradicting fresh instructions.

## Quality Checklist
- [ ] Layered assembly · [ ] provenance marks · [ ] utilization measured · [ ] headroom reserved

## Examples
Coding agent context: system rules (2k) + AGENTS.md summary (1k) + relevant skill section (1-2k) + precise file excerpts (not whole files) + task spec last.

## Anti-Patterns
One mega-prompt with everything. Context-free retrieval chunks (unanswerable without neighbors). Ignoring token cost curves.

## References
knowledge/context-engineering/ · AGENTS.md §5 (progressive disclosure)

## Related Skills
prompt-engineering, web-research, knowledge files in this repo generally

## Evaluation Criteria
Measured utilization: provided context appears in model's reasoning/outputs; removal of any component measurably hurts — else it's dead weight.
