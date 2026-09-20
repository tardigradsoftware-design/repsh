---
name: api-design
version: 1.0.0
description: Contract-first API design — REST resources, versioning, pagination, errors, and consistency rules
category: backend
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-03-20
content_type: RECOMMENDATION
tags: [api, rest, architecture, backend]
requires: []
quality: { authority: 8, evidence: 7, recency: 8, adoption: 9, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# API Design

## Purpose
Design API contracts that stay consistent as the product grows: predictable resources, explicit errors, evolvable versions.

## When to Use
New public/internal APIs; when an API is getting incoherent.

## When NOT to Use
Internal-only server actions where a typed function call is the contract.

## Inputs
Domain model; consumer needs (who calls this and with what latency budget).

## Required Context
`knowledge/backend/rest-patterns.md`; `patterns/backend/`.

## Workflow
INPUT (domain) → PROCESS (resources → verbs → shapes → errors → versioning) → OUTPUT (OpenAPI/schema + code) → VALIDATION (contract tests + docs match)

## Research Phase
Check the target framework's canonical patterns; if GraphQL/tRPC chosen, document WHY (our default: REST + typed server functions; see decision-records).

## Planning Phase
- Nouns for resources, plural (`/projects/{id}/tasks`)
- Filtering/sorting/pagination: cursor pagination for scale, documented envelope
- Error shape: `{ error: { code, message, details } }` — stable machine codes
- Idempotency keys on unsafe methods clients may retry
- Version from day one if external (`/v1/`)

## Implementation Phase
Generate schemas from code where possible (typed frameworks); docs generated, never hand-synced.

## Validation Phase
- [ ] Contract tests = docs
- [ ] 401/403/404/409/422 used correctly (not everything 400)
- [ ] Pagination + rate-limit headers present
- [ ] Breaking-change process documented

## Failure Modes
Chatty APIs (N+1 client calls) — offer batch/compose endpoints where hot. Leaking internal IDs/enums. Silent 200-with-error-body.

## Quality Checklist
- [ ] Consistent naming · [ ] stable error codes · [ ] idempotency on retries · [ ] generated docs

## Examples
Tasks API: cursor pagination (`?cursor=&limit=`), `POST /v1/tasks` returns 201+Location, idempotency-key header honored for 24h.

## Anti-Patterns
Verb URLs (`/getTasks`). Changing response shapes without version. Boolean-in-disguise enums.

## References
patterns/backend/ · decision-records/rest-vs-graphql.md

## Related Skills
backend-engineering, documentation, testing

## Evaluation Criteria
Two consumers can be written against the spec without reading the implementation.
