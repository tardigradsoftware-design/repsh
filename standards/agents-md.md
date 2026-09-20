---
title: AGENTS.md Standard (normalized)
updated: 2026-09-20
verified_at: 2026-09-20
tags: [standards, agent-instructions]
---

# AGENTS.md Standard

Source: the open AGENTS.md format (verified record: repositories/skills/agentsmd_agents.md.yaml, 24k+ stars 2026-09-20). Related formats normalized for our purposes: CLAUDE.md, GEMINI.md, .cursor/rules, .github/copilot-instructions.md — same job, different names; AGENTS.md is the cross-agent open standard.

## Normalized sections for projects adopting it
1. **Project context** — what this is, in 3 sentences
2. **Build/test commands** — verified-by-running commands only
3. **Architecture** — map + where things live + do-not-touch zones
4. **Coding conventions** — the ones that differ from language defaults
5. **Security** — auth boundaries, secrets policy, RLS notes
6. **Testing** — how to run, flaky policy, coverage-by-risk expectations
7. **Update rules** — when to regenerate docs/indexes, PR etiquette

## Rules for writing
- Commands must be executed during writing (doc drift is a bug)
- Keep it ≤ ~150 lines; link to deeper docs
- Dated volatile facts; agent-facing = terse imperative
