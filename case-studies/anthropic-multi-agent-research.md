---
title: Case Study — Anthropic Multi-Agent Research System
type: case-study
organization: Anthropic
published: 2025-06-13
sources_verified_at: 2026-09-20
confidence: high
source_url: https://www.anthropic.com/engineering/multi-agent-research-system  # canonical; verified by direct fetch 2026-09-20
source_type: official (vendor engineering blog — architecture claims primary; performance claims vendor-stated)
tags: [multi-agent, orchestrator-worker, research-agents, production]
---

# Anthropic: Multi-Agent Research System (production)

## Architecture
Orchestrator-worker: a **lead agent** (Opus-class) plans the research strategy, writes the plan to external memory before its context fills, then spawns **3–5 parallel subagents** (Sonnet-class), each with its own context window, each given: objective, output format, tool list, and an explicit done-condition. A separate **citation pass** with fresh context verifies every citation before anything reaches the user.

## Reported results (vendor-stated; verified against full text 2026-09-20)
- +90.2% over single-agent Opus 4 on their internal research eval (breadth-first queries)
- Multi-agent ≈ 15× chat token cost; agents ≈ 4× chat
- On BrowseComp: token usage alone explains 80% of performance variance (95% with tool-call count + model choice)
- Plan persisted to external memory because >200k-token contexts get truncated
- Follow-up guidance (2026-07, claude.com blog): start with the SIMPLEST system that works; multi-agent only when evidence supports it

## Lessons for this KB
1. **Parallel context windows beat one big window** for breadth-first problems — corroborates our context-packing notes (subagents = context isolation as architecture).
2. **Externalize the plan** (memory before context overflow) — matches plan-then-execute pattern's checkpointing rule.
3. **Separate citation/verification pass** — the fact-checker agent pattern, production-validated.
4. **The cost curve is real** — multi-agent is a budget decision first (15×), an intelligence decision second. Our agent-evaluation-metrics cost-per-success applies.

## Limitations
Vendor-reported numbers on internal evals (not independently reproduced). Architecture description is primary-source; effect sizes are RECOMMENDATION-grade until reproduced. Detailed notes: knowledge/multi-agent/multi-agent-patterns.md.
