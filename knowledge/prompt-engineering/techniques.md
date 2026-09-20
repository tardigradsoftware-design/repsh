---
title: Prompting Techniques That Survive Contact With Production
category: prompt-engineering
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
tags: [prompts, ai-engineering]
---

# Prompting Techniques

(Canonical templates: `prompts/`. Model-behavior caveats live in `models/` with dates — prompting advice decays.)

## Durable techniques
- **Structure over prose:** role/task/context/format/guardrails sections; explicit output schema with escape hatch ("missing info → null, never invent").
- **Few-shot with coverage:** 2-3 examples covering typical + ambiguous + adversarial; more examples ≠ better (quirk lock-in).
- **Decomposition:** complex tasks → explicit steps; separate generation from critique (different prompts beat "do it well in one").
- **Verification pass:** a differently-framed checker prompt catches more than re-reading.
- **Self-consistency (cheap):** sample k for verifiable answers; majority/verify.
- **Constraint-first:** define what NOT to do near the task, not buried in boilerplate.
- **Provenance-marked context:** "Context [1] is official docs (2026-09-20)…" improves weighting.

## Model-family caveat (verify current!)
Instruction-heavy scaffolds ("think step by step", "take a deep breath") helped pre-reasoning models; reasoning-trained models can degrade under forced CoT or redundant scaffolds. Check the model's official prompting guide (dated in models/) before shipping scaffolds.

## Anti-patterns
Prompt-as-string-in-code (unversioned); "be creative/robust/production-ready" as instructions; contradictory format demands; testing only happy paths.
