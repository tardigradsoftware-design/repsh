---
title: Hugging Face Research Layer
category: research
confidence: high
updated: 2026-09-20
verified_at: 2026-09-20
tags: [huggingface, models, datasets, discovery]
---

# Hugging Face Layer

The open-weights ecosystem's primary surface. Use it deliberately (allowlisted for bot-blocking in link checker — verify key pages by hand).

## What to mine
- **Models** — open model families (DeepSeek-R1 lineage, Qwen, Llama, Mistral, Gemma): model cards = context window, license (CRITICAL: gate-2.0-class licenses are NOT Apache), usage notes. License check per card, every time.
- **Datasets** — reasoning traces (OpenR1-Math-class, public-only per policy), coding (SWE-bench family), tool-use (BFCL-family). Check license + contamination status before eval use.
- **Spaces** — demos as quick capability smoke-tests (never as evidence of production behavior).
- **Evaluation** — Open LLM Leaderboard lineage + community evals; prefer lm-evaluation-harness task registry for reproducibility.
- **Papers (HF papers page)** — trending with code links; feed the paper→code→dataset relation records (sources/papers/ template).
- **Leaderboards** — SHORTLIST signal only; contaminated/benchmark-saturated sets are common (evaluations/reasoning/benchmarks.md rules).

## Integration rules
1. Model facts from HF cards expire in days — record `verified_at` + re-check at decision time (models/ policy).
2. Dataset downloads: respect licenses; gate/restricted datasets need account-level terms acceptance — do not mirror.
3. Compare models on YOUR tasks (models/comparisons/evaluation-first.md); leaderboards only shortlist.
4. Track org pages (knowledge/research/organizations-to-watch.md) for release signals.
