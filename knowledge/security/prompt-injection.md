---
title: Prompt Injection (Direct & Indirect)
category: security
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [security, llm, agents, owasp]
---

# Prompt Injection

LLM Top-10 #1 class (see OWASP Top 10 for LLM Applications — official, in repositories/). Not "fixable" — layered risk management.

## Taxonomy
- **Direct:** user input carries instructions ("ignore previous…").
- **Indirect:** untrusted CONTENT the agent ingests (web pages, emails, docs, tickets, code comments) carries instructions. This is the agent-era killer: browsing tools make every web page a potential instruction channel.

## Why it works
Instruction/data separation in LLMs is statistical, not structural. Any text in context can act as instructions. Filtering "bad strings" fails (encoding, paraphrase, multilingual).

## Layered defenses
1. **Least-privilege tools** (biggest lever): an agent that can only read docs can't exfiltrate secrets. Scope per session; write actions need confirmation gates.
2. **Trust-marking content:** wrap untrusted content in provenance markers; instruct the model to treat marked content as data, never instructions.
3. **Output side guards:** validate ACTIONABLE outputs (URLs, emails, code execution, payments) against allowlists before executing; nothing important triggered by content-originated instructions without human confirmation.
4. **Exfil monitoring:** log outbound calls; alert on secrets-shaped strings in URLs/params.
5. **Dual-LLM / privileged-query patterns:** sensitive ops handled by a separate context that never sees untrusted content.
6. **Red-team routinely:** promptfoo-class injection test suites in CI (see evaluations/ + promptfoo record).

## Known limits (honesty)
No complete defense exists. For high-stakes tools (payments, prod DB writes, code execution, messaging), design ASSUMING injection will eventually succeed: blast-radius control > string matching.
