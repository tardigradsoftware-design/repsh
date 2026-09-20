---
title: Model Selection Framework
category: ai-engineering
confidence: medium
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-09-20
tags: [models, selection]
---

# Model Selection Framework

> All specific "model X is best" claims REQUIRE dated verification (this note expires fast BY DESIGN). Check `models/` notes + vendor model cards + current leaderboards before deciding. Never let a training-data-era answer pick your model.

## Decision dimensions
task fit (coding/reasoning/vision/long-context) · context needs · latency budget · cost per successful outcome · structured output reliability · tool-use reliability · ecosystem (SDK/MCP support) · deployment constraint (cloud API vs open-weights/self-host) · data governance

## Process
1. Define success metrics FIRST (task-specific, not vibes).
2. Shortlist 3 candidates across tiers (frontier / efficient / open-weights).
3. Eval on YOUR tasks (≥30 cases; see evaluation/agent-evaluation-metrics.md) — public benchmarks only shortlist.
4. Cost-per-SUCCESS comparison (including retries).
5. Re-eval on vendor major releases; record in models/ with dates.

## Open-weights line
DeepSeek-R1-lineage (open reasoning), Qwen/Llama/Mistral families for self-host — verify current releases on Hugging Face (our datasets/models notes are dated pointers, not truth).
