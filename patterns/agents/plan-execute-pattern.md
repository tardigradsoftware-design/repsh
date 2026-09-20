---
title: Plan-then-Execute Pattern
category: agents
confidence: high
updated: 2026-09-20
tags: [agents, planning]
---

# Plan-then-Execute

For multi-step tasks: a planning pass produces an explicit step list (with success criteria per step); execution follows the plan stepwise with re-planning allowed when evidence contradicts it.

## Rules
- Plan items are verifiable ("page returns 200 with auth cookie" not "make auth work")
- Re-plan is explicit: state what evidence triggered the change (no silent drift)
- Long tasks checkpoint state (resumable) — LangGraph-class durable execution fits (records verified)
- Progress surfaced to the operator at plan + milestone boundaries, not every micro-step
