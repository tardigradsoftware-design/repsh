---
name: performance-review
version: 1.0.0
category: performance
status: active
skills: [performance-audit]
agents: [performance-engineer]
updated: 2026-09-20
tags: [performance]
---

# Performance Review Workflow

## Steps
1. Define the budget (targets per page type) BEFORE measuring.
2. Measure throttled mobile profile: CWV (LCP/INP/CLS) + TTFB + route JS size.
3. Trace the top offender (DevTools MCP perf trace ideal); identify cause not symptom.
4. Fix ranked by measured impact; re-measure each fix independently.
5. Check data paths: N+1 queries, missing indexes (EXPLAIN), unbounded lists.
6. Server: pool/timeouts under concurrency; queue lag.
7. Record budgets + before/after table; add CI perf budget where feasible.

## Exit criteria
Budgets met or consciously waived by owner; evidence table committed.
