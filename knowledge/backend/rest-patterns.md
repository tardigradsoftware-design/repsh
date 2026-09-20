---
title: REST API Patterns
category: backend
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [api, rest, backend]
---

# REST Patterns (condensed contract rules)

Full design skill: `skills/api-design`. WebSockets/SSE/event patterns below.

## Core contract rules
- Plural nouns, stable error envelope, cursor pagination, idempotency keys on retryable unsafe methods, version prefix when external.

## Streaming & realtime
- **SSE** default for server→client updates (AI token streams): simple, proxy-friendly, auto-reconnect.
- **WebSockets** for bidirectional (collab, chat): plan auth handshake + reconnect + heartbeats.
- **Webhooks** for outbound events: signature verification + idempotent processing + fast-2xx-then-queue.

## Background jobs & queues
- Never long work in request path (serverless timeouts!). Enqueue → return 202.
- Idempotency per job (dedupe key); retries with exponential backoff + dead-letter queue.
- Scheduled work: platform cron; watch timezone assumptions.

## Event-driven notes
- Start with queue-per-task, not full event bus; introduce event sourcing/CQRS only with recorded reasons (see patterns/architecture/).
