---
title: Model Selection (Dated Method)
category: models
confidence: high
content_type: RECOMMENDATION
verified_at: 2026-09-20
expires_at: 2026-09-27
---

# Model Selection Method (no absolute model claims stored)

This KB deliberately stores NO "model X is currently best" verdicts — they decay in weeks. Stored instead:

- The selection method (knowledge/ai-engineering/model-selection.md)
- Durable failure classes (limitations/)
- Where to verify: vendor model cards (context window/modalities/pricing CHANGE — read the card the week you decide), HF model pages, current leaderboards

## Record template (fill per decision, with dates)
```yaml
model: <name + exact version>
decided_for: <task>
verified_at: <date>
context_window: <from official card>
pricing: <from official pricing page>
eval_result_on_our_tasks: <N runs, success rate, cost/success>
re_evaluate_by: <date>
```
