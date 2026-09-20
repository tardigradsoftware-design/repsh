---
title: Context Packing
category: context-engineering
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [context, agents, retrieval]
---

# Context Packing

Design the context assembly order for agents. Goal: the model acts on the right information without wading through noise.

## Layers (in stable order)
1. **Identity/rules** (small, stable): role, policies, output contracts
2. **Task dossier:** current task + its constraints + success criteria
3. **Working knowledge:** the exact skill/knowledge SECTIONS needed (progressive disclosure — index → summary → section)
4. **Evidence:** retrieved excerpts WITH provenance (source + date + confidence) so the model can weigh trust
5. **Recent state:** last actions/results, errors to avoid repeating

## Principles
- **Cache-first ordering (production-validated — case-studies/manus-context-engineering.md):** stable prefix first (identity/rules NEVER carry timestamps), append-only context, deterministic serialization. Cache hits cost ~1/10 of input tokens; prefix churn is the dominant hidden cost bug.
- Relevance beats completeness: measure what the model USES (utilization check); cut dead weight.
- Critical constraints repeated at the end for long contexts (recency effect).
- Compression: extractive excerpts for facts (summaries lose specifics); summaries for orientation only.
- Provenance always: unmarked sources get over-trusted; dated+graded sources get used correctly.
- Freshness: stale cached context contradicts fresh instructions — inject `as-of` dates.

## Anti-patterns
Everything-in-one-window stuffing (attention dilution); retrieval chunks without neighbors (unanswerable); instructions at position 0 in 100k+ contexts (lost-in-middle); mixing conflicting versions of the same doc.
