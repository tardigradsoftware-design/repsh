---
title: Durable LLM Limitation Classes
category: models
confidence: high
content_type: FACT
verified_at: 2026-09-20
tags: [models, limitations]
---

# Durable Limitation Classes (survive model generations)

1. **Hallucination under absence** — fluent output for missing facts. Counter: cite-or-refuse contracts, provenance-marked context.
2. **Instruction/data entanglement** — context content can act as instructions (prompt injection). Counter: least-privilege tools (security/prompt-injection.md).
3. **Arithmetic/precision drift** — offload exact computation to code/tools.
4. **Long-context degradation** — lost-in-middle, needle dilution (context-engineering notes).
5. **Date/knowledge cutoff** — "latest X" answers go stale silently; give the model dated sources.
6. **Format regression under complexity** — schema compliance decays with task size; validate + retry at boundary.
7. **Sycophancy** — agreement pressure under pushback; decisions need written evidence, not confidence tone.
