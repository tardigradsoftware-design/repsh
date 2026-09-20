---
name: release-checklist
version: 1.0.0
category: devops
status: active
skills: [testing, security-audit, documentation]
updated: 2026-09-20
tags: [release, devops]
---

# Release Checklist Workflow

## Pre-release
- [ ] CI green (tests, lint, types, security scans)
- [ ] E2E critical journeys green on staging-like data
- [ ] Security review current for changed auth/data code
- [ ] Dependency audit clean; new deps license-checked
- [ ] Migrations: applied on staging clone; rollback path documented
- [ ] Env contract: new vars documented; secrets present in target env (never committed)
- [ ] Perf budgets spot-checked
- [ ] a11y spot-check on new UI

## Release
- [ ] Tag + changelog entry (Added/Updated/Deprecated/Removed/Security)
- [ ] Deploy with health check; smoke test in prod
- [ ] Feature flags default-safe

## Post-release
- [ ] Error rates/latency watched for first window
- [ ] Rollback criteria defined BEFORE deploy (what rate = rollback)
- [ ] Runbook updated

## Exit criteria
All boxes checked or waived with names + reasons; rollback plan tested once.
