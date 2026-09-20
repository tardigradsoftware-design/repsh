---
name: research-before-coding
version: 1.0.0
category: meta
status: active
skills: [research-before-code, web-research, source-validation, evidence-validation]
agents: [researcher, architect]
updated: 2026-09-20
tags: [core, research]
---

# Research Before Coding Workflow

Runs as the FIRST phase of any non-trivial implementation task.

## Steps
1. **UNDERSTAND** — restate task; list constraints + assumptions (tagged).
2. **KB CHECK** — `indexes/topics.md` → relevant skills/repos/patterns/anti-patterns. Check `expires_at` on records.
3. **SEARCH** — official docs/repos first; web-research skill for anything the KB lacks or that's dated.
4. **COMPARE** — build-vs-reuse analysis; decision matrix for ≥2 options.
5. **VERIFY** — source-validation on load-bearing claims; ≥2 sources for HIGH.
6. **PLAN** — research note (decision/evidence/alternatives/risks/reuse list) committed before code.
7. Hand off to implementation with the plan as contract.

## Exit criteria
Research note exists; every decision cited; assumptions listed; reuse decisions explicit.

## Anti-patterns
Skipping step 4 (defaulting to build-your-own); citing without opening sources.
