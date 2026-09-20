---
title: Webhook Processing Pattern
category: backend
confidence: high
updated: 2026-09-20
tags: [webhooks, backend, reliability]
---

# Webhook Processing Pattern

## The contract
1. Verify signature FIRST (constant-time compare; reject early)
2. Persist raw event + dedupe key (event id) with UNIQUE constraint → duplicates become no-ops
3. Enqueue for processing; return 2xx immediately (providers time out at ~5-10s)
4. Worker processes idempotently; retries with backoff; dead-letter after N
5. Reconciliation job polls the source of truth (webhooks DO get lost)

## Failure modes
Processing inside the request (timeout = provider retries = duplicates) · trusting delivery order · signature check skipped on "trusted" networks.
