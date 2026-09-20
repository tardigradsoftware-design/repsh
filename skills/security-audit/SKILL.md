---
name: security-audit
version: 1.0.0
description: Web + LLM application security review — OWASP Top 10, auth/RLS verification, prompt-injection and MCP risk assessment
category: security
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-09-20
content_type: RECOMMENDATION
tags: [security, owasp, llm, mcp, core]
requires: []
quality: { authority: 9, evidence: 9, recency: 9, adoption: 8, reproducibility: 8, practical_value: 10, maintenance: 8 }
---

# Security Audit

## Purpose
Find the exploitable, not the theoretical: auth boundaries, injection, secret handling, supply chain, and — for AI apps — prompt injection and tool abuse.

## When to Use
Before any release; whenever auth/payments/user-data code changes; when adopting a new MCP server or agent tool.

## When NOT to Use
Formal compliance audits (this complements, never replaces, professional pentesting).

## Inputs
Codebase access, auth flows, env/secret inventory, dependency list, MCP/tool permissions.

## Required Context
`knowledge/security/owasp-top10-checklist.md`, `knowledge/security/prompt-injection.md`, `knowledge/security/mcp-security.md`, OWASP Cheat Sheet Series (repositories/developer-tools/owasp_cheatsheetseries.yaml — official), OWASP Top 10 for LLM Applications.

## Workflow
INPUT (app surface) → PROCESS (enumerate → test each class → grade → report) → OUTPUT (findings w/ severity + fixes) → VALIDATION (retest after fixes)

## Research Phase
Map the attack surface: public endpoints, auth flows, file/network-touching tools, admin functions, third-party data flows.

## Planning Phase — checklist per class
Web: injection (SQL/command), broken auth, sensitive-data exposure, broken access control (IDOR!), security misconfig, XSS, CSRF, SSRF, insecure deps, logging failures.
Data: RLS actually enforced (test as anon/user/service); no service-role keys client-side.
AI: direct/indirect prompt injection (untrusted content = instructions?), tool permission scope, data exfiltration via tool calls (URLs, webhooks), MCP server risk grades from our registry, output handling (rendering model output as HTML?).
Secrets: scanned (trufflehog-class), rotation story, least-privilege tokens.

## Implementation Phase (reporting)
Findings: `SEV-CRITICAL/HIGH/MEDIUM/LOW` + reproduction + concrete fix. No vague "consider hardening".

## Validation Phase
- [ ] Every HIGH reproduced (proof-of-concept or test)
- [ ] Fixes retested
- [ ] Dependency audit clean or waivers documented
- [ ] AI-app: injection test set executed against tool-using flows

## Failure Modes
Checklist theater (ticking without testing). Client-side-only validation assumed secure. "Our MCP only reads" without verifying scope.

## Quality Checklist
- [ ] Surface mapped · [ ] each class tested · [ ] severities justified · [ ] retest done

## Examples
Supabase app: RLS policy review finds `USING (true)` on a table reachable via anon key → SEV-CRITICAL → policy rewrite + role-matrix test added.

## Anti-Patterns
Security through obscurity. Storing secrets in env files committed to repo. Treating prompt injection as unsolvable (layered defenses exist: scope tools, sanitize content, constrain outputs).

## References
knowledge/security/ · OWASP Cheat Sheet Series (official) · knowledge/mcp/registry/

## Related Skills
code-review, security-review workflow, fact-checker (for advisory claims)

## Evaluation Criteria
Audit report where every finding has: location, exploit path, severity, fix — and the fixes actually close the holes (retest evidence).
