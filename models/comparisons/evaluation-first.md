---
title: Comparison Method (Evaluation-First)
category: models
confidence: high
verified_at: 2026-09-20
tags: [models, method]
---

# Comparing Models: Method Over Verdicts

Public leaderboard deltas ≠ your task. Method:
1. Define 3-5 task-representative eval sets (real inputs, rubric-scored)
2. Test ≥3 candidates incl. one efficient/cheap tier
3. Measure: success rate, cost-per-SUCCESS (retries included), p95 latency, format compliance
4. Decide on cost-per-success at required quality; record in models/model-cards/ template with dates
5. Re-run on notable releases; revisit-by date set

Vendor-published comparisons are marketing until reproduced on your tasks (grade them RECOMMENDATION, not FACT).
