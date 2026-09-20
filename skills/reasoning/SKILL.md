---
name: reasoning
version: 1.0.0
description: Structured reasoning patterns for agents — decomposition, verification, self-consistency, reflection applied at the right dose
category: reasoning
status: active
confidence: medium
source_type: reference
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
content_type: RECOMMENDATION
tags: [reasoning, agents, research]
requires: [prompt-engineering]
quality: { authority: 8, evidence: 9, recency: 8, adoption: 8, reproducibility: 7, practical_value: 8, maintenance: 8 }
---

# Reasoning (Applied Patterns)

## Purpose
Apply the public reasoning-research toolkit (CoT, self-consistency, verification, decomposition, reflection) proportionally — reasoning compute is a budget, not a default.

## When to Use
Math/logic/planning tasks; high-stakes answers needing verification; agent steps with tool calls.

## When NOT to Use
Simple retrieval/rephrasing (reasoning scaffolds add latency + sometimes errors). Modern reasoning models often need LESS scaffolding — don't force CoT on models trained to reason natively (verify per model family; see models/ notes).

## Inputs
Problem type; stakes; model capabilities (dated verification!).

## Required Context
`knowledge/reasoning/` (public research survey: CoT, ToT, self-consistency, Reflexion, PRM/ORM, test-time scaling); `datasets/reasoning/` for eval sources.

## Workflow
INPUT (problem) → PROCESS (decompose → solve → verify → (sample k if cheap)) → OUTPUT (answer + verification evidence) → VALIDATION (independent check path)

## Research Phase — pattern selection
- Decomposition: multi-constraint problems (plan → sub-answers → compose)
- Self-consistency: cheap-to-sample verifiable answers (k samples, majority/verify)
- Verifier pass: separate check step with DIFFERENT framing (catches more than re-reading)
- Reflection/revision: when verification fails, revise with failure EXPLICIT
- Search (tree): huge branching problems — rare; cost first

## Planning Phase
Choose minimum sufficient pattern; define the verification method BEFORE solving (what would prove the answer wrong?).

## Implementation Phase
Keep reasoning steps inspectable (agent logs/agent trajectories) — needed for debugging and for feeding our self-improvement loop (what worked/failed).

## Validation Phase
- [ ] Verification step ran and its result recorded
- [ ] Answer doesn't contradict its own sub-steps
- [ ] Cost proportional to stakes

## Failure Modes
Reasoning theater (elaborate chains arriving at unjustified confidence). Verification collapse (checking with the same faulty assumption). Forced CoT on natively-reasoning models degrading output.

## Quality Checklist
- [ ] Pattern justified by problem type · [ ] independent verification · [ ] inspectable steps

## Examples
Migration planning: decompose into schema/data/cutover/rollback sub-problems; solve each with domain checks; verify with a "what breaks on day 1" adversarial pass.

## Anti-Patterns
Chain-of-thought on every trivial call. Trusting "I verified it" without a distinct verification procedure.

## References
knowledge/reasoning/ (public research only — see SECURITY policy: no private CoT collection) · deepseek-ai/DeepSeek-R1 + huggingface/open-r1 records (open implementations)

## Related Skills
prompt-engineering, context-engineering, evidence-validation

## Evaluation Criteria
On a verification-seeded test set (answers with plausible-but-wrong traps), pattern use catches ≥70% of traps without 2x cost blowup.
