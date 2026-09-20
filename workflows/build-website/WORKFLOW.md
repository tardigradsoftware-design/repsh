---
name: build-website
version: 1.0.0
category: web
status: active
skills: [project-planning, research-before-code, frontend-design, frontend-implementation, ai-slop-detection, testing, security-audit, performance-audit, accessibility-audit, documentation]
agents: [architect, frontend-engineer, website-quality-reviewer, qa-engineer]
updated: 2026-09-20
tags: [web, saas, core]
---

# Build Website Playbook

The end-to-end sequence for web projects (landing, SaaS app, dashboard). Each stage names its exit criteria — don't advance with failures.

```
idea → research → competitor research → design system → architecture →
implementation → animation → responsive → accessibility → performance →
SEO → testing → deployment
```

## 1. Idea → Requirements (project-planning)
Functional + non-functional + out-of-scope. Exit: written spec, assumptions confirmed.

## 2. Research (research-before-code)
Stack selection via `decision-records/technology-selection.md`; verify current versions (dated). Exit: research note with citations.

## 3. Competitor research (competitive-analysis)
Live dated evidence; extract principles, not pixels. Exit: adopt/avoid/gap decisions.

## 4. Design system (frontend-design)
Tokens (type/space/color/radius/motion) BEFORE components. Exit: token sheet.

## 5. Architecture (architect)
Routes, data model + RLS, auth boundaries, deployment target. Exit: ADRs + schema migration v0.

## 6. Implementation (frontend-engineer, backend-engineer)
Hardest screen first. Server-first data. Exit: core flows working, tests green.

## 7. Animation (frontend-design + knowledge/frontend/animation-knowledge.md)
Motion budget: ≤1 hero moment; interaction feedback everywhere; nothing loops without cause. `prefers-reduced-motion` honored. Exit: motion inventory with justifications.

## 8. Responsive
375/768/1440 screenshots reviewed; touch targets ≥44px. Exit: no horizontal overflow, key flows work on mobile.

## 9. Accessibility (accessibility-audit)
Keyboard journeys, SR spot-check, contrast per theme. Exit: audit findings resolved.

## 10. Performance (performance-audit)
Throttled measurement; top-3 offenders fixed; budgets recorded. Exit: before/after table.

## 11. SEO
Titles/meta/OG/sitemap/robots/heading order/canonical. Exit: checks pass.

## 12. Testing (testing + browser-testing)
Unit + integration + E2E for critical journeys; visual regression on design system. Exit: suite green, no flakes.

## 13. Quality gate (website-quality-reviewer)
Full report; CRITICAL+HIGH resolved. Exit: report in repo.

## 14. Security (security-audit)
Auth boundaries, RLS matrix, secrets scan, dependency audit. Exit: findings resolved.

## 15. Deployment + docs
Env contract documented, rollback plan, README verified. Exit: deployed + runbook.

## Failure modes
- Skipping stage 4 (tokens) → inconsistency tax forever.
- Testing only stage 12 — test beds must exist by stage 6.
- "We'll add security at the end" — never true.
