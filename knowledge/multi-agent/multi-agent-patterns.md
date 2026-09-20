---
title: Multi-Agent Patterns
category: multi-agent
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [multi-agent, orchestration, agents]
---

# Multi-Agent Patterns

## When multi-agent (and when NOT)
Anthropic's own follow-up guidance (2026-07): **start with the simplest system that works** — add agents only when evidence demands it. Go multi-agent when: work decomposes into INDEPENDENT parallel facets, total context needed exceeds one window, or roles need different tool scopes. Stay single-agent when: tasks are sequential, coordination cost > parallelism gain, or the budget can't absorb multi-agent economics.

## Pattern catalog
| Pattern | Shape | Use when | Risk |
|---|---|---|---|
| Orchestrator-worker | lead plans → N workers execute in parallel → lead synthesizes | breadth-first, parallelizable research/tasks | token cost ~linear in workers |
| Pipeline | A → B → C specialists | staged transforms (generate → verify → format) | serialization; handoff fidelity |
| Debater/critic | generator ↔ adversarial checker | high-stakes correctness | convergence theater without rubric |
| Hierarchical | manager → sub-teams | large task trees | compounding latency + cost |
| Blackboard | shared state, specialists contribute | heterogeneous expertise | state races; needs locking model |

## Orchestrator-worker in practice (validated by Anthropic case study — case-studies/)
- Subagent brief = objective + output format + tool list + done-condition (self-contained; no shared chat history)
- Lead writes the plan to EXTERNAL memory before its context fills
- Separate verification/citation pass with fresh context
- Budget rule: workers' token spend is the quality driver AND the cost driver — cap and monitor

## Coordination rules
- Communication = structured handoffs (schemas), never free chat transcripts
- Failure isolation: one worker failing ≠ workflow failing (retry/replan at orchestrator)
- State: single source of truth (checkpoint store), not agents' memories
- Observability: per-agent traces with parent correlation (langfuse/phoenix records)

## Cost/economics
Multi-agent spends tokens to buy context isolation and parallelism. Measure cost-per-successful-task, not per-agent-output (knowledge/evaluation/agent-evaluation-metrics.md). Framework fit: LangGraph (stateful graphs), Microsoft Agent Framework (orchestration), crewAI (role crews) — records verified 2026-09-20.
