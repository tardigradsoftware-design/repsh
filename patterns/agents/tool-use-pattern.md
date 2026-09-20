---
title: Tool-Use Pattern (Agent)
category: agents
confidence: high
updated: 2026-09-20
tags: [agents, tools, mcp]
---

# Tool-Use Pattern (agents)

## Design
- Tool descriptions are PROMPTS: precise, example-bearing, scoped ("read-only: lists files under root").
- Validate ALL args with schemas at the boundary; never trust model-generated params.
- Idempotency keys for side-effecting tools; confirmation gates for destructive ones.
- Return structured results + truncation signals; errors as first-class results (model can recover).

## Loop safety
Cap iterations; detect loops (same tool+args repeated); budget tokens; escalate to human on repeated failures.

## Security
Page/tool-result content is untrusted (indirect injection) — provenance-mark everything entering context; see knowledge/security/prompt-injection.md + mcp-security.md.
