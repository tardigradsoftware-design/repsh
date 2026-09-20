---
name: security-review
version: 1.0.0
category: security
status: active
skills: [security-audit]
agents: [security-reviewer]
updated: 2026-09-20
tags: [security, core]
---

# Security Review Workflow

## Steps
1. Map attack surface (public endpoints, auth flows, admin, tools/MCP, data flows).
2. Test per class: injection, authN/authZ (incl. IDOR), SSRF, XSS, CSRF, misconfig, secrets, deps.
3. Data layer: RLS matrix test (anon/user/service roles), backup/restore sanity.
4. AI-specific: prompt-injection paths (any untrusted content reaching instructions?), tool permission scope, exfiltration routes (URLs/webhooks in tool calls), MCP risk grades from `knowledge/mcp/registry/`.
5. Supply chain: dependency audit, typosquat check on new packages, secret scanning.
6. Report: SEV-ranked findings + proof + concrete fix per finding.
7. Retest after fixes; record evidence.

## Exit criteria
No unresolved CRITICAL/HIGH; retest evidence recorded; AI-surface findings included when applicable.
