---
name: testing
version: 1.0.0
description: Proportional test strategy — unit, integration, E2E pyramid with the right tool per layer
category: testing
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
content_type: RECOMMENDATION
tags: [testing, quality, e2e, vitest, playwright]
requires: []
quality: { authority: 8, evidence: 8, recency: 9, adoption: 9, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# Testing

## Purpose
Right-sized automated testing: fast unit tests for logic, few integration tests for seams, E2E only for critical journeys.

## When to Use
Before delivering any feature; whenever a bug is fixed (regression test mandatory).

## When NOT to Use
Throwaway spikes (say so explicitly instead of writing fake tests).

## Inputs
Feature spec, risk areas (money, auth, data mutation = highest).

## Required Context
`knowledge/testing/strategy.md`; `skills/browser-testing` for E2E specifics.

## Workflow
INPUT (feature + risks) → PROCESS (risk map → pyramid allocation → implement → CI) → OUTPUT (suite) → VALIDATION (mutation spot-checks, flake audit)

## Research Phase
Verify current tool versions (Vitest, Playwright majors) — breaking changes are frequent; check repositories/ records.

## Planning Phase
Allocate by risk, not coverage vanity: auth flows, payments, data migrations get E2E; pure logic gets unit; DB seams get integration against a REAL database (testcontainers or branch DB), never mocks of SQL.

## Implementation Phase
- Arrange-Act-Assert; one behavior per test; deterministic (fake clocks, seeded data).
- E2E: user-visible selectors (roles/labels), not brittle CSS chains; auto-waiting, no sleeps.
- Flaky test policy: quarantine + fix within the sprint, never permanent skip.

## Validation Phase
- [ ] Suite green locally + CI
- [ ] Mutation spot-check (break code, test should fail)
- [ ] Runtime < feedback-friendly budget
- [ ] No network calls in unit tests

## Failure Modes
Mock-everything suites that test the mocks. Coverage % as goal. Sleep-based E2E flakes.

## Quality Checklist
- [ ] Risk-ranked · [ ] real DB at integration layer · [ ] deterministic · [ ] regression test per bug

## Examples
Checkout: unit-test pricing math, integration-test order persistence, E2E-test one happy-path purchase with test card 4242…, stub external webhooks at contract level.

## Anti-Patterns
Snapshot tests as primary strategy. Testing implementation details (private methods). One giant E2E that must pass for every deploy.

## References
knowledge/testing/ · skills/browser-testing · evaluations/web/

## Related Skills
browser-testing, debugging, code-review

## Evaluation Criteria
Deleting a core line of logic makes the suite fail (mutation-verified); suite runs < 5min for CI feedback.
