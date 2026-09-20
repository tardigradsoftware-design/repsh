---
title: Case Study — Manus Context Engineering Lessons
type: case-study
organization: Manus (Yichao "Peak" Ji, co-founder/chief scientist)
published: 2025-07-18
sources_verified_at: 2026-09-20
confidence: high
source_url: https://manus.im/blog/Context-Engineering-for-AI-Agents-Lessons-from-Building-Manus
source_type: official (vendor engineering blog)
tags: [context-engineering, kv-cache, agents, production]
---

# Manus: Context Engineering Lessons (production agent, millions of users)

## The six practices (their words, condensed)
1. **Design for KV-cache first** — stable prompt prefixes (no timestamps), append-only context, deterministic serialization (JSON key order matters). Cache hit cost ≈ 1/10 of input tokens; misses are the dominant cost bug.
2. **Mask tools, don't remove them** — dynamically editing the tool list invalidates the cache and confuses the model; constrain via logit masking with stable prefixes (`browser_*`, `shell_*`).
3. **Filesystem as unbounded context** — compress observations into restorable files instead of truncating; the FS is persistent, directly manipulable memory.
4. **Recite the plan** — a continuously rewritten todo.md at the context tail manipulates attention ("recitation") against lost-in-the-middle drift on long tasks.
5. **Keep errors in the trace** — leaving failures visible teaches the model to avoid them; hiding/cleaning errors causes repetition.
6. **Inject controlled few-shot noise** — break the agent's mimicry of previous trajectory patterns on repetitive tasks.

## Meta-lesson
Context engineering as experimental science ("stochastic gradient descent" via 4 framework rebuilds): measure → rebuild → measure. Not elegant; honest.

## Lessons for this KB
- Validates our context-engineering notes (packing, long-context failures) with production numbers — especially cache-prefix stability, which our notes underweighted; now promoted into context-packing.md's principles.
- todo.md recitation is a cheap pattern agents here should default to for long tasks.
- "Keep errors in trace" aligns with our failure-knowledge doctrine (§53) — at trajectory level.

## Limitations
Single-vendor experience tuned to their model/stack; techniques (e.g., logit masking) require infra control others may not have. RECOMMENDATION-grade for generalization.
