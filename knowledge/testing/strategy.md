---
title: Test Strategy
category: testing
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [testing, strategy]
---

# Test Strategy

## The matrix per web project
Functional (unit/integration/E2E by risk) · Visual (design-system screenshots) · Responsive (3 viewports) · Accessibility (keyboard+scan) · Performance (budgets) · Security (auth/RLS/injection spot-tests) · SEO (meta/structure) · Browser compatibility (top-3 engines by your analytics, not folklore)

## Allocation by risk
Money/auth/data-migration → E2E + integration with REAL database. Pure logic → unit. Styling → visual snapshots. Everything else → proportional, not maximal.

## Rules
- Deterministic: fake clocks, seeded data, no network in unit layer.
- Real DB at integration (testcontainers/branch DBs); SQL mocks lie.
- Flaky policy: quarantine + fix in-sprint. Permanent skips are bugs in the suite.
- Bug fix → regression test, always (workflows/bug-investigation).
