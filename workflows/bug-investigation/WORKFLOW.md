---
name: bug-investigation
version: 1.0.0
category: engineering
status: active
skills: [debugging, testing, repository-analysis]
agents: [qa-engineer]
updated: 2026-09-20
tags: [debugging, quality]
---

# Bug Investigation Workflow

## Steps
1. **Triage** — severity (data loss/security = P0), affected surface, since-when (diff/history).
2. **Reproduce** — deterministic repro or minimal repro; not reproducible = instrument, don't guess.
3. **KB check** — `anti-patterns/known-bugs.md` for the exact error class; stack gotchas.
4. **Isolate** — bisect: recent change? data? environment? component boundary?
5. **Hypothesize** — ≥2 competing hypotheses with discriminating evidence defined BEFORE fixing.
6. **Verify cause** — evidence picks the winner; document why others rejected.
7. **Fix minimally** — root cause, smallest change; no stacked hacks.
8. **Regression test** — fails-before/passes-after.
9. **Sweep** — same bug class in sibling paths.
10. **Record** — if novel/gotcha-worthy → propose `anti-patterns/` entry (experimental pipeline).

## Exit criteria
Regression test merged; root cause sentence a reviewer accepts; siblings audited.
