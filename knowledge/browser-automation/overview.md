---
title: Browser Automation for Agents
category: browser-automation
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [browser, agents, automation]
---

# Browser Automation for Agents

## Layered model
1. **Primitives:** Playwright (official, active — repositories record) — deterministic DOM control, the substrate.
2. **Agent-native MCP:** playwright-mcp (a11y-tree snapshots; fast + deterministic) · chrome-devtools-mcp (perf/debug insight).
3. **Autonomous browser agents:** browser-use (massive adoption; visual+DOM hybrid) · BrowserGym (research/benchmark env).
4. **Computer use (OS-level):** screen-coordinates control — last resort when DOM/browser APIs unavailable.

## Decision rule
Deterministic flow → write Playwright code (fast, reliable). Ambiguous exploration → agent+MCP or browser-use over a11y tree FIRST, vision when layout semantics fail. Never vision-only when the accessibility tree exists (10x slower, less reliable).

## Notes
- Accessibility-tree-driven control (playwright-mcp model) is generally the sweet spot: structured, robust to pixel changes, LLM-legible.
- Page content is UNTRUSTED: every browsing session is a prompt-injection surface (knowledge/security/prompt-injection.md). Sandbox + scope.
- Eval/benchmarking browser agents: BrowserGym + evaluations/web/ records.
