# Task 016 — "Is AutoGen still maintained?"

## BASELINE output (no KB)
"Yes — AutoGen is actively maintained by Microsoft. It's one of the most popular multi-agent frameworks (60k+ stars), widely used in production, and a safe choice for new multi-agent projects."

## KB output (with retrieval — records used)
Cited record: `repositories/agent-frameworks/microsoft_autogen.yaml` (generated from live GitHub API, checked 2026-09-20).

**Answer: PARTIALLY — it is maintained, but in maintenance mode.** Status `MAINTENANCE` (auto-derived from push cadence: last push 2026-04, ~5 months before verification). Microsoft directs **new** projects to **Microsoft Agent Framework** (verified ACTIVE, pushed within a day of verification), which succeeds AutoGen and Semantic Kernel. Confidence HIGH. Recommended_for: legacy deployments, research references. Not recommended_for: new projects.

## Scores
| Dimension | BASELINE | KB | Evidence |
|---|---|---|---|
| task completion | 2 | 2 | both answer yes/no-ish |
| instruction following | 0 | 2 | baseline: no status vocabulary, no dates |
| tool correctness (status vocab + successor mapping) | 0 | 2 | baseline missed maintenance-mode entirely |
| planning quality | 1 | 2 | KB gives decision consequence (don't choose for new work) |
| self-correction | 1 | 1 | — |
| hallucination | 0 | 2 | **baseline "safe choice for new projects" is false as of verification date** |
| efficiency | 2 | 1 | — |
| safety | 1 | 2 | wrong framework choice for new work = real project risk |
| **Total** | **8** | **16** | — |
