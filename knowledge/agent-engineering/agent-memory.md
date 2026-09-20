---
title: Agent Memory Architecture
category: agent-engineering
confidence: medium
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
tags: [memory, agents]
---

# Agent Memory Architecture

## Memory types (working taxonomy)
- **Working** — current context window (see context-engineering/)
- **Episodic** — what happened (sessions, trajectories, tool results)
- **Semantic** — facts about user/project/domain (knowledge base, profiles)
- **Procedural** — HOW to do things: skills, playbooks, learned routines
- **Project** — repo-scoped state (AGENTS.md, decisions, TODOs)

## Stores
Vector stores (semantic recall) · knowledge graphs (relations — memory-mcp pattern) · structured files/DBs (procedural + project) · conversation logs (episodic). Most production systems combine ≥2.

## Design rules
1. **Write with provenance + timestamps** — memory without dates rots into misinformation.
2. **Trust tiers:** observed-by-agent < human-confirmed < verified-external. Poisoned memory (false observations persisting) is the failure mode that compounds.
3. **Retrieval on demand, not bulk:** memory returns as ranked evidence, provenance-marked — not as a second context dump.
4. **Consolidation loop:** periodic distillation of episodes → semantic notes (with sources) → occasionally procedural skills (the self-improvement path — see self-improving-agents.md).
5. **Forgetting is a feature:** TTL/decay + explicit invalidation (e.g., "that library version changed") beat infinite append.

## Reference architectures (public)
- NousResearch hermes-agent (repositories/agent-frameworks/) — experience→skill synthesis loop, personal memory growth; massive adoption at verification. Treat architecture descriptions as primary-source; capability claims as vendor-stated.
- memory-mcp (knowledge/mcp/registry/) — knowledge-graph memory reference.
