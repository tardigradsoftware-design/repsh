---
title: Code Review Checklist
category: coding
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [review, quality]
---

# Code Review Checklist

## Correctness
- [ ] Does what the spec says (not what the code looks like it should do)
- [ ] Edge cases: empty, huge, concurrent, failure paths
- [ ] Error handling: real failures surface; no swallowed exceptions

## Security (auth/data paths especially)
- [ ] Authz on new endpoints; IDOR check; input validation at boundary
- [ ] No secrets in code/logs; new deps license+maintenance checked (repositories/ records)

## Design
- [ ] Fits existing conventions/patterns (repository-analysis note is the reference)
- [ ] No new abstractions without a second user; naming honest

## Tests
- [ ] New behavior tested; regression added for the bug being fixed
- [ ] Tests meaningful (mutation spot-check), deterministic

## AI-generated code (mandatory extra lens)
- [ ] Every API call verified to exist (hallucination check)
- [ ] Deps pinned + audited (AI loves inventing packages)
- [ ] No invented config options/env vars

Severity discipline: BLOCKER / MAJOR / MINOR / NIT — see skills/code-review.
