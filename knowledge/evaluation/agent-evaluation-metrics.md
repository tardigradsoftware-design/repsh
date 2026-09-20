---
title: Agent Evaluation Metrics
category: evaluation
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [evaluation, agents, metrics]
---

# Agent Evaluation Metrics

"Did the AI say the right thing?" is not agent evaluation. Measure the system across:

## Outcome
task completion (verbatim-defined success) · recovery rate (from injected faults) · regression rate (over versions/time)

## Process
planning quality (plan-vs-executed divergence) · tool correctness (right tool, right args) · self-correction (detects + fixes own errors) · instruction following (constraint adherence)

## Safety & quality
hallucination rate (claims vs verifiable) · security (injection survival — see knowledge/security/prompt-injection.md) · code quality (if coding: tests pass, review findings severity)

## Economics
latency (p50/p95) · token efficiency (per completed task) · cost · cost-per-success (the number that actually matters)

## Method notes
- Evaluate on FIXED task suites with rubric scores (see evaluations/agents/ for benchmark references; build your own 20-50 real tasks — see `evaluations/agents/kb-eval-suite.md` for this repo's own suite).
- LLM-judge scores need: rubric, position-bias controls, and human spot-audits.
- Report deltas with N and variance; single-run "improvements" are noise.
