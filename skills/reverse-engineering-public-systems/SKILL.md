---
name: reverse-engineering-public-systems
version: 1.0.0
description: Understand publicly documented or observable systems (APIs, formats, protocols) through legal, documented signals only
category: research
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [research, integration, ethics]
requires: [source-validation]
quality: { authority: 7, evidence: 7, recency: 8, adoption: 7, reproducibility: 8, practical_value: 8, maintenance: 8 }
---

# Reverse-Engineering Public Systems

## Purpose
Integrate with systems lacking full docs by using PUBLIC evidence: official partial docs, published SDKs, OpenAPI specs, public changelogs, observable behavior YOU are authorized to see.

## When to Use
Third-party APIs with incomplete docs; undocumented-but-public file formats; missing SDK for your language.

## When NOT to Use — HARD LIMITS
- Never bypass auth, rate limits, robots/ToS, or paywalls
- Never probe private/internal endpoints, admin surfaces, or other users' data
- Never deobfuscate proprietary binaries to extract private logic/model internals
- Never collect leaked credentials/tokens/system prompts — report and move on

## Inputs
Authorized access credentials, official docs (even partial), public SDK source, YOUR OWN account's observable traffic.

## Required Context
`standards/copy-policy.md`; `knowledge/security/prompt-injection.md` when the system serves content.

## Workflow
INPUT (system + authorization) → PROCESS (gather public evidence → hypothesize → verify via authorized calls → document) → OUTPUT (integration + findings doc) → VALIDATION (works within documented/observed contract; ToS respected)

## Research Phase
1. Official docs, changelogs, status pages, openapi/swagger files, official SDK source (often reveals undocumented fields).
2. Observe behavior of YOUR OWN authorized requests/responses.

## Planning Phase
Map known vs unknown; hypothesize unknowns; design minimal authorized experiments.

## Implementation Phase
- Tolerant clients (unknown fields ignored) — public APIs evolve.
- Document discovered behavior with evidence + date; flag as OBSERVED not OFFICIAL.

## Validation Phase
- [ ] All evidence legally obtained (authorized account, public sources)
- [ ] Client handles undocumented fields gracefully
- [ ] ToS/rate limits respected in design

## Failure Modes
Building on observed-but-unofficial behavior that breaks silently (mitigate: contract tests + alerts). Scope creep into prohibited probing.

## Quality Checklist
- [ ] Ethics checklist passed · [ ] observed vs official clearly labeled · [ ] tolerant parsing

## Examples
Learning a CMS's public GraphQL schema shape from its published playground + SDK source to build a typed client in a language with no official SDK.

## Anti-Patterns
Aggressive endpoint scanning. Presenting reverse-engineered guesses as documented fact.

## References
standards/copy-policy.md · knowledge/security/

## Related Skills
source-validation, web-research, api-design

## Evaluation Criteria
Integration works, is ToS-compliant, and a reviewer can distinguish OBSERVED vs OFFICIAL behavior throughout the findings doc.
