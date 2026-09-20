---
name: prompt-engineering
version: 1.0.0
description: Structured prompt design — role/task/context/format/eval scaffolding, few-shot discipline, verification loops
category: ai-engineering
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
content_type: RECOMMENDATION
tags: [prompts, ai-engineering, core]
requires: [context-engineering]
quality: { authority: 8, evidence: 8, recency: 8, adoption: 9, reproducibility: 8, practical_value: 9, maintenance: 8 }
---

# Prompt Engineering

## Purpose
Prompts as engineered artifacts: versioned, evaluated against test cases, with known failure modes — not vibes in a config file.

## When to Use
Building any LLM feature; writing templates for `prompts/`; tuning failing generations.

## When NOT to Use
One-off interactive chats (still: state role+format for quality).

## Inputs
Task definition, model (with date — behavior differs!), success examples, failure examples.

## Required Context
`prompts/` templates; `knowledge/prompt-engineering/techniques.md`; model notes in `models/` (dated!).

## Workflow
INPUT (task) → PROCESS (structure → few-shot → constraints → eval set) → OUTPUT (versioned prompt + eval) → VALIDATION (eval pass-rate; regression suite)

## Research Phase
Check vendor-official prompting guides for the CURRENT model (techniques age: what helped GPT-4-class models can hurt newer reasoners — e.g., over-prompting reasoning models to "think step by step" is often counterproductive; verify per model family).

## Planning Phase
Anatomy: ROLE (who) → TASK (what, verb-first) → CONTEXT (facts, provenance-marked) → FORMAT (exact output contract) → GUARDRAILS (what not to do) → EXAMPLES (2-3 edge-covering, not 10 redundant).

## Implementation Phase
- Output contracts: schemas/JSON where parseable; escape hatches ("if info missing, say MISSING" — never invent).
- Few-shot: cover the boundaries (one typical, one ambiguous, one adversarial).
- Version prompts like code; changelog entries.

## Validation Phase
- [ ] Eval set ≥10 cases incl. failures-to-avoid
- [ ] Deterministic-format prompts parse 100% (or instrumented retries)
- [ ] Failure modes documented from real runs

## Failure Modes
Example lock-in (model mimics example quirks). Contradictory instructions (format says JSON, prose says "explain"). Missing escape hatch → hallucinated specifics.

## Quality Checklist
- [ ] Structured anatomy · [ ] eval set exists · [ ] versioned · [ ] escape hatch present

## Examples
Extraction prompt: task verb → schema contract → "output exactly this JSON; unknown fields = null" → 3 examples (clean/messy/adversarial) → eval on 20 labeled docs.

## Anti-Patterns
"Be creative" as an instruction. Prompt-length-as-quality. Prompt pasted into code as an unversioned string.

## References
prompts/ · knowledge/prompt-engineering/ · models/ (dated model notes)

## Related Skills
context-engineering, evaluations (testing prompts), reasoning

## Evaluation Criteria
Prompt survives its eval suite across ≥2 runs; format compliance 100%; documented failure modes match reality.
