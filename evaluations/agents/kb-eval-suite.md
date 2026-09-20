---
title: Knowledge Base Evaluation Suite (25 tasks)
category: agents
content_type: ORIGINAL
updated: 2026-09-20
tags: [evaluation, kb]
---

# KB Evaluation Suite

Purpose: measure whether THIS knowledge base actually improves agent performance. Run each task WITH the KB mounted and WITHOUT (baseline), compare.

## Tasks (id · prompt · judged dimensions)
001 · "Build an enterprise admin dashboard (Next.js+TS+Postgres, multi-tenant)" — architecture, RLS, UI quality
002 · "Add secure authentication with OTP email flow" — security, UX states
003 · "Design a SaaS billing database schema" — schema, indexes, migration story
004 · "Create a premium landing page for a developer tool" — slop-checklist, performance, copy honesty
005 · "Debug: intermittent 500s in production Next.js app" — method adherence, root-cause quality
006 · "Choose ORM for an edge-deployed app" — decision matrix quality, dated evidence
007 · "Write an ADR for queue infrastructure" — ADR completeness
008 · "Research: current state of X framework" — citation discipline, recency labels
009 · "Review this PR (seeded with IDOR + missing test)" — detection, severity accuracy
010 · "Make this page fast (seeded 4s LCP)" — measurement-before-optimization
011 · "Design multi-tenant RLS policies" — policy correctness, role-matrix tests
012 · "Build a browser test suite for checkout" — determinism, selector quality
013 · "Set up MCP servers for a coding agent safely" — scoping, risk grading
014 · "Extract design principles from 3 reference sites" — dated evidence, principle-not-pixel
015 · "Write an agent skill for API design" — format compliance, test cases
016 · "Answer: is framework X maintained?" — status vocabulary, evidence
017 · "Plan an 8-week SaaS MVP" — milestones demo-able, non-functionals
018 · "Audit this app's a11y (seeded traps)" — keyboard trap + contrast detection
019 · "Design an agent memory architecture" — trust tiers, provenance
020 · "Evaluate two models for code review tasks" — eval design quality, cost-per-success
021 · "Migrate REST to add SSE for streaming" — technology fit, migration safety
022 · "Detect slop in this AI-generated page (seeded)" — detection rate, fix quality
023 · "Write AGENTS.md for a new repo" — standard sections, command verification
024 · "Investigate mysterious DB load" — systematic method, EXPLAIN evidence
025 · "Design release checklist for a payments feature" — rollback, monitoring, gates

## Scoring
Rubric per task (0-2 × dimensions, judge prompt in `prompts/evaluation/`) + human spot-audit ≥20%.
Report: success rate, time, tokens, defect counts — WITH vs WITHOUT KB, N=3 runs each (variance reported).

## Runs
- **PILOT executed 2026-09-20** — 4 tasks (006/016/011/013), baseline vs KB: mean 10.25 → 16.0 /16. Self-scored, N=1 — directional only. Full methodology + limitations: `results/2026-09-20-pilot/`.

## Success criterion
KB-mounted runs show statistically meaningful improvement on knowledge-dependent tasks (006/008/013/016/019/020) without slowing trivial tasks. If not: the KB is decoration — fix the KB, not the metric.
