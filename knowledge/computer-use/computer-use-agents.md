---
title: Computer-Use Agents
category: computer-use
confidence: medium
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [computer-use, agents, browser, security]
---

# Computer-Use Agents

OS/desktop-level control (screenshots → coordinates → clicks/keys) vs browser-level agents (DOM/accessibility tree). Vendors ship computer-use APIs (Anthropic-class) and OS-agent frameworks; capabilities evolve fast — verify current docs before building (dated-claims policy).

## Decision ladder (cheapest reliable layer first)
1. **APIs/direct integration** — when a real API exists, don't click through a UI
2. **DOM/Playwright** — deterministic control of known flows
3. **Accessibility-tree agent** (playwright-mcp / browser-use) — ambiguous flows, structured navigation
4. **Computer use (pixels+coordinates)** — LAST resort: legacy desktop apps, canvas-only UIs, cross-app workflows with no API surface

## Reliability reality
Pixel-space control is the most fragile layer: resolution/DPI/theme changes break coordinates; screen inference adds error rates DOM agents don't have. Expect more retries, more verification steps, higher cost per action.

## Security (the big one)
A computer-use agent holds the KEYS TO THE MACHINE: screen contents (secrets in view!), clipboard, filesystem, credentials in apps. Rules:
- Dedicated VM/container/sandbox profile; never the operator's daily desktop
- No stored credentials in the reachable session beyond task scope
- Human gates on irreversible actions (delete, send, pay)
- Screenshot streams may contain PII — treat as sensitive data in logs

## Evaluation
Success rates drop sharply vs DOM agents on the same task — benchmark on YOUR target screens (evaluations/web/ has web-agent benchmarks; extend the method to your desktop flows: fixed task set, rubric, N≥3).
