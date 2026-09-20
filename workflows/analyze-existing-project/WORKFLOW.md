---
name: analyze-existing-project
version: 1.0.0
category: engineering
status: active
skills: [repository-analysis, documentation, code-review]
agents: [architect]
updated: 2026-09-20
tags: [onboarding, architecture]
---

# Analyze Existing Project Workflow

## Steps
1. Read repo map: README, AGENTS.md/CLAUDE.md, manifests, CI config, migrations.
2. Trace entry points → routes → services → data layer.
3. Extract conventions from ≥3 files each (naming, testing, error handling, state).
4. Verify commands: build/test/run actually work — fix doc drift notes.
5. Risk scan: abandoned deps, license conflicts, TODO graveyards, secret patterns, `anti-patterns/known-bugs.md` hits.
6. Produce `analysis.md`: architecture text-diagram, conventions, how-to-run, risks, do-not-touch zones.
7. If no AGENTS.md exists → propose one from findings (standards/agents-md.md).

## Exit criteria
analysis.md committed; commands verified; a second agent onboards in <10 min from it.
