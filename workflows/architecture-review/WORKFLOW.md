---
name: architecture-review
version: 1.0.0
category: engineering
status: active
skills: [repository-analysis, code-review, security-audit]
agents: [architect, security-reviewer]
updated: 2026-09-20
tags: [architecture, review]
---

# Architecture Review Workflow

## Review lens
1. **Boundaries** — modules/ownership clear? Data flows explicit? Circular deps?
2. **Data integrity** — where does state live? who can mutate? migration story?
3. **Security boundaries** — auth surface, trust transitions, tenant isolation.
4. **Scalability** — first bottleneck at 10x (compute? DB? third-party rate limits?).
5. **Failure modes** — what happens when each dependency dies? retry/timeout story?
6. **Operability** — deploy rollback, observability, config management.
7. **Knowledge fit** — check `patterns/architecture/` + `decision-records/` for named patterns before judging custom solutions.

## Output
Findings ranked by risk + ADR proposals for each architectural change recommended. Conflicts with the codebase's own documented decisions are surfaced, not silently overridden.
