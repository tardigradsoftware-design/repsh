---
title: Visual Regression Testing
category: testing
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [testing, playwright, visual]
---

# Visual Regression Testing

## Approach
Playwright screenshots on stable viewports; per-component (not full-page-first); baselines in repo; diffs reviewed in CI artifacts. Interaction testing pairs with screenshots (states: hover/focus/open menus).

## Rules
- Mask/whitelist dynamic regions (timestamps, avatars, ads) BEFORE they train the team to auto-accept diffs.
- Baseline updates are REVIEWS: every accepted diff names the intended change.
- Deterministic rendering: frozen animation states, consistent fonts/DPR in CI.
- Full-page shots for marketing pages; component shots for design systems.

## Tools
Playwright built-ins (default choice — official, active); commercial cloud cross-browser grids when the matrix demands. Verify current Playwright major in repositories/browser-automation/.
