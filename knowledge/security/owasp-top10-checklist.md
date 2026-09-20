---
title: Web Security Checklist (OWASP-aligned)
category: security
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [security, owasp, checklist]
---

# Web Security Checklist

Primary references: OWASP Cheat Sheet Series (official) + OWASP Top 10 — see repositories/developer-tools/owasp_cheatsheetseries.yaml (verified 2026-09-20). This checklist operationalizes them for web app delivery.

## Access control
- [ ] Server-side authz on EVERY endpoint (never trust client checks)
- [ ] IDOR test: user B cannot read/write user A's resources by ID guessing
- [ ] Admin routes behind role checks + separate audit trail

## Injection
- [ ] Parameterized queries only (ORM count as parameterized IF no raw string concat)
- [ ] No shell-out with user input; template engines auto-escaping on

## Auth & sessions
- [ ] Rate-limited login (+ credential stuffing defenses), MFA support where stakes justify
- [ ] Session fixation protected; secure/httpOnly/sameSite cookies; short-lived JWTs + rotation story
- [ ] OAuth: state/PKCE; redirect allowlist exact-match

## Data exposure
- [ ] TLS everywhere; no secrets in client bundles (scan builds)
- [ ] PII minimized in logs; error responses leak-free (stack traces off in prod)
- [ ] RLS/row scoping verified for multi-tenant data (see databases/rls-patterns.md)

## XSS/CSRF
- [ ] Framework default escaping kept; `dangerouslySetInnerHTML` audited; CSP defined
- [ ] CSRF tokens or sameSite=strict on state-changing routes

## SSRF & file handling
- [ ] Outbound fetches to user-supplied URLs: allowlist + no internal ranges
- [ ] Uploads: type/size validation, stored outside web root or object storage, no direct execution

## Supply chain & ops
- [ ] Lockfiles committed; dependency audit in CI; secret scanning (trufflehog-class)
- [ ] Security headers: CSP, HSTS, X-Content-Type-Options, frame-ancestors
- [ ] Backups restored-in-test at least once
