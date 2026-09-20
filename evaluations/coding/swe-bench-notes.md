---
title: SWE-bench Usage Notes
category: coding
confidence: high
updated: 2026-09-20
tags: [benchmark, coding-agents]
---

# SWE-bench Notes

Canonical coding-agent benchmark: resolve real GitHub issues, judged by repo tests. Verified active (repositories/evaluation/ record, 2026-09-20).

## Usage guidance
- **SWE-bench Verified** subset for human-validated grading (fewer false negatives).
- Contamination awareness: newer models may have seen issue text; interpret leaderboard deltas cautiously; prefer fresh/unseen splits when precision matters.
- It measures issue-resolution, not code review/refactor/design — complement with task-specific evals (see agent-evaluation-metrics).
