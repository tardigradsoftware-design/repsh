---
title: Self-Improving Agent Loops
category: agent-engineering
confidence: medium
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
tags: [agents, self-improvement, skills]
---

# Self-Improving Agent Loops

The pattern (exemplified by hermes-agent, superpowers-class frameworks): agents that convert experience into reusable procedure.

## The loop
```
EXECUTE TASK → CAPTURE (what worked / failed / was missing) → CANDIDATE
(knowledge or skill) → VALIDATE (tests/evidence) → PROMOTE → RETRIEVE NEXT TIME
```

## Safety valves (non-negotiable)
- **Quarantine tier:** candidates land in `experimental/`, never core (this repo's pipeline: AI GENERATED → EXPERIMENTAL → HUMAN REVIEW → TEST → EVIDENCE → VALIDATED → CURATED).
- **Evidence before promotion:** a candidate skill must show ≥1 case where it changed an outcome for the better; a "lesson" needs a reproduced failure mode.
- **Decay:** promoted knowledge gets `expires_at` and re-verification duties like everything else here.
- **Bounded self-modification:** agents never edit their own guardrails/policy files.

## What's worth capturing (signal filter)
Worked/failed solutions with CAUSE · tool quirks discovered · outdated sources detected · missing-skill moments ("I needed X and had nothing") · cost/latency surprises. NOT: session narratives, user PII, one-off coincidences.

## Measurement
Self-improvement claims need numbers: task success rate / tokens / time on a fixed eval set over time (see evaluations/agents/). Without a fixed benchmark, "the agent got better" is unfalsifiable.
