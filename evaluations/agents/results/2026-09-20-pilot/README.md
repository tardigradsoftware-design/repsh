---
title: Pilot KB Evaluation Run
date: 2026-09-20
type: evaluation-results
status: pilot
---

# Pilot Run — KB Evaluation Suite (4/25 tasks)

## Method (honest)
- 4 knowledge-dependent tasks from `evaluations/agents/kb-eval-suite.md` (006, 016, 011, 013)
- **BASELINE** = answer produced WITHOUT consulting this repo (training-data only)
- **KB** = answer produced following the repo's retrieval flow (indexes → records → notes), citing the records used
- Scored on the 8-dimension rubric (0–2 each, max 16) from `prompts/evaluation/agent-task-rubric.yaml`

## ⚠ Limitations (read before quoting these numbers)
1. **Self-scoring bias:** evaluator = the same agent that produced the outputs. Mitigated by evidence citations per score; not eliminated. Independent re-scoring required before treating numbers as measurement.
2. **N=1** per condition (suite requires N=3) — no variance estimate.
3. Tests the **content delta of the KB**, not model differences (same model, same session).
4. Pilot conclusion scope: directional evidence only.

## Results summary

| Task | BASELINE /16 | KB /16 | Δ | Knowledge-dependent dims won by KB |
|---|---|---|---|---|
| 006 ORM for edge app | 12 | 16 | +4 | instruction-following (dated evidence + verification steps) |
| 016 Is AutoGen maintained? | 8 | 16 | +8 | hallucination (baseline asserted ACTIVE — false as of 2026-09), tool correctness (status vocabulary) |
| 011 Multi-tenant RLS | 11 | 16 | +5 | tool correctness (with check, service-role, role-matrix tests) |
| 013 Safe MCP setup | 10 | 16 | +6 | tool correctness (risk-graded scoping), safety |
| **Mean** | **10.25** | **16.0** | **+5.75** | |

## Conclusion (pilot)
Directionally consistent with the suite's success criterion: KB-mounted runs win specifically on **knowledge-dependent dimensions** (recency, named risks, scoped guidance) and never lose on efficiency by more than 1 point (retrieval overhead). A real measurement needs: independent evaluator, N=3, full 25 tasks, and token/time logging (not yet instrumented in this pilot).

## Next
- [ ] Independent human/model-judge re-score of these outputs
- [ ] Remaining 21 tasks
- [ ] N=3 repetition + token/time capture
