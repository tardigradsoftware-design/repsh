---
name: backend-engineering
version: 1.0.0
description: API and service implementation patterns — FastAPI/NestJS, background jobs, queues, event-driven design with verified current APIs
category: backend
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
content_type: RECOMMENDATION
tags: [backend, api, nodejs, python, queues]
requires: [research-before-code, api-design]
quality: { authority: 8, evidence: 8, recency: 9, adoption: 9, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# Backend Engineering

## Purpose
Build services that are boring in the right ways: explicit contracts, validated boundaries, resilient async work.

## When to Use
APIs, webhooks, background workers, scheduled jobs, integrations.

## When NOT to Use
Static sites with no backend needs.

## Inputs
Domain requirements, data model, SLA/performance expectations.

## Required Context
`knowledge/backend/` (rest-patterns, background-jobs, event-driven), `knowledge/backend/nodejs-python-stack.md`, repositories/backend records.

## Workflow
INPUT (requirements) → PROCESS (contract → implementation → async work → hardening) → OUTPUT (service + tests) → VALIDATION (contract tests, load sanity, security checklist)

## Research Phase
Confirm framework versions (FastAPI, NestJS current majors) and driver/runtime support from official docs. Prefer managed queues/DBs available in the target platform (Vercel/Supabase/Railway constraints shape choices).

## Planning Phase
Define: authN/Z boundary, idempotency strategy for webhooks, retry/dead-letter policy for queues, rate limits, logging/trace correlation.

## Implementation Phase
- Validate at every boundary (request schemas; no raw client data into domain logic).
- Long work → jobs + queue, never in request path; make handlers idempotent.
- Errors: structured, mapped to correct status codes, no internal leaks.
- Config via env; secrets never in code (see security-audit).

## Validation Phase
- [ ] Contract tests (request/response shapes)
- [ ] Webhook signature verification tested
- [ ] Queue retry + poison-message path tested
- [ ] Rate limiting on public endpoints
- [ ] No secrets in logs

## Failure Modes
Fire-and-forget promises losing work on crash. Non-idempotent webhook handlers double-charging. Sync calls in request path exceeding platform timeouts (serverless!).

## Quality Checklist
- [ ] Idempotency where money/state changes · [ ] timeouts+retries on ALL external calls · [ ] structured logging w/ request ids

## Examples
Stripe webhook endpoint: verify signature → enqueue → worker processes idempotently keyed on event id → respond 2xx fast.

## Anti-Patterns
Doing 5 sequential third-party calls inside one request. Trusting queue exactly-once delivery.

## References
knowledge/backend/ · repositories/backend/ · patterns/backend/

## Related Skills
api-design, database-design, testing, security-audit

## Evaluation Criteria
Service survives the failure-mode checklist; contract tests prove the API matches its documented schema.
