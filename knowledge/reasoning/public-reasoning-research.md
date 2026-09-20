---
title: Public Reasoning Research Map
category: reasoning
confidence: high
content_type: FACT
updated: 2026-09-20
verified_at: 2026-09-20
tags: [reasoning, research, public-only]
---

# Public Reasoning Research Map

SCOPE (hard rule from SECURITY.md): public research, open weights, published methods, reproducible implementations ONLY. No private chain-of-thought, no leaked internals, ever.

## Core lines of research (names to search)
- **CoT** (Chain-of-Thought prompting) — elicit stepwise solutions; the founding public technique
- **Self-Consistency** — sample k reasoning paths, majority vote
- **ToT / GoT** (Tree/Graph-of-Thought) — search over thought states
- **ReAct** — interleave reasoning + tool actions (the agent-era backbone)
- **Reflexion / Self-Refine** — verbal feedback loops, critique-and-revise
- **Verifier / Critic models** — separate models scoring candidate solutions
- **PRM vs ORM** (Process vs Outcome Reward Models) — supervision granularity for RL on reasoning
- **Test-time compute / inference-time scaling** — spending more compute at answer time for quality
- **Search-augmented reasoning (MCTS-class)** — planning via tree search (AlphaGo-lineage → modern LLM variants)
- **Tool-augmented reasoning (PAL-class)** — offload precise computation to code execution

## Open implementations & datasets (verified repos — see repositories/research/)
- **DeepSeek-R1** (deepseek-ai) — open-weight reasoning model; RL with verifiable rewards; distillation recipes. Repo pushed 2025-06 at verification → model evolution tracked on HF, repo is the canonical paper/weights pointer.
- **Open-R1** (huggingface) — full open reproduction: training pipeline + OpenR1-Math datasets. The best public "how it's actually done" reference.
- **Gorilla / BFCL** (ShishirPatil) — tool-use reliability measurement line.

## Eval surfaces
Reasoning benchmarks and their contamination caveats: see `evaluations/reasoning/` + `datasets/reasoning/`.

## Ethics boundary (repeated)
Public reasoning research advances agents. Collecting private CoT/hidden prompts does not — it's theft and it's poison for this KB (unverifiable, unlicensed). We don't index it, link it, or mirror it.
