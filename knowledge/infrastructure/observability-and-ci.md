---
title: Observability & CI for AI Applications
category: infrastructure
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [devops, observability, ci, llm]
---

# Observability & CI for AI Applications

## CI pipeline for AI features (beyond lint/tests)
1. Unit/integration/E2E (normal gates)
2. **Prompt/agent regression suite** — promptfoo-class declarative evals in CI on every prompt/agent change (record verified, ACTIVE) — fail on metric drop vs baseline
3. **Schema-contract checks** — structured outputs validated against schemas with bounded retries; assert parse rate
4. **Cost/latency budget assertions** — token-per-task and p95 latency thresholds flagged in PRs
5. Red-team spot suite for tool-using flows (injection set — knowledge/security/prompt-injection.md)

## Observability stack (pick per ecosystem)
| Tool | Fit | Verified |
|---|---|---|
| langfuse | self-hostable traces + evals + prompt mgmt | 2026-09-20 |
| Arize phoenix | OTel-based, notebook/CI ergonomics | 2026-09-20 |
| pydantic/logfire | pydantic-ai native, OTel | 2026-09-20 |
All OpenTelemetry-aligned — standardize on OTel spans so you can swap vendors.

## What to trace (minimum)
Every LLM call: model+version, full prompt assembly (or hash + snapshot store), latency, tokens in/out, cost, tool calls with args, and parent task correlation. Agent trajectories = inspectable reasoning (feeds debugging + self-improvement loops).

## Ops practices
- Model version pinning + canary on model upgrades (silent behavior shifts are the classic outage)
- Cache monitoring (KV/prompt-cache hit rates — cost lever #1, see case-studies/manus)
- Error budgets for AI features (hallucination reports as incidents with postmortems)
- Dashboards: success rate, cost-per-success, p95 latency, tool failure rates, injection-alert count
