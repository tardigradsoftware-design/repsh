---
name: browser-testing
version: 1.0.0
description: Playwright-based E2E and visual regression testing for web apps, including agent-driven exploration patterns
category: testing
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
content_type: RECOMMENDATION
tags: [testing, e2e, playwright, visual-regression]
requires: [testing]
quality: { authority: 9, evidence: 9, recency: 9, adoption: 9, reproducibility: 9, practical_value: 9, maintenance: 9 }
---

# Browser Testing

## Purpose
Deterministic browser tests + visual regression + (optionally) LLM-assisted exploration — using Playwright primitives for determinism and AI only where ambiguity demands it.

## When to Use
Critical user journeys, visual regression on design systems, cross-viewport checks, testing AI-web-apps end to end.

## When NOT to Use
Pure logic (use unit tests); scraping (that's browser-automation knowledge, not testing).

## Inputs
App URL + auth strategy, list of critical journeys, design-system components.

## Required Context
`repositories/browser-automation/microsoft_playwright.yaml` (official, ACTIVE, verified 2026-09-20); `knowledge/testing/visual-regression.md`; `evaluations/web/` for web-agent benchmarks if exploring.

## Workflow
INPUT (journeys) → PROCESS (scaffold → selectors → assertions → visual baselines → CI) → OUTPUT (suite + reports) → VALIDATION (stability across 10 runs)

## Research Phase
Verify Playwright current major + browser channel support from official docs. If using MCP-driven exploration (playwright-mcp / chrome-devtools-mcp), review their security entries in knowledge/mcp/registry/.

## Planning Phase
Journeys: login, core CRUD, payment, recovery paths. Viewports: 375/768/1440. Auth: storageState reuse, not login-per-test (speed) except one auth test.

## Implementation Phase
- Role/label selectors: `getByRole('button', { name: 'Checkout' })`.
- Web-first assertions (`expect(locator).toBeVisible()`), zero sleeps.
- Visual: per-component screenshots on a stable viewport; baselines committed; review diffs in CI artifacts.
- Traces on retry for diagnosis (`trace: 'on-first-retry'`).

## Validation Phase
- [ ] 10 consecutive green runs (flake audit)
- [ ] Visual diffs reviewed intentionally, not auto-accepted
- [ ] Parallel-safe (no shared test data collisions)

## Failure Modes
Tests coupled to styling internals. Timezone/locale-dependent assertions. Visual baselines auto-updated to hide real regressions.

## Quality Checklist
- [ ] No sleeps · [ ] semantic selectors · [ ] trace-on-retry · [ ] baselines reviewed

## Examples
Checkout E2E: add-to-cart → apply test code → pay with 4242… → assert confirmation contains order id; full-page screenshot diffed at 1440px.

## Anti-Patterns
Pixel-perfect full-page diffs on dynamic content (whitelist dynamic regions first). Testing third-party embeds' internals.

## References
knowledge/testing/ · microsoft/playwright-mcp registry entry · evaluations/web/

## Related Skills
testing, ai-slop-detection (visual audit), performance-audit

## Evaluation Criteria
Suite detects an intentionally-injected visual + functional regression; 10/10 stable runs; zero hardcoded waits.
