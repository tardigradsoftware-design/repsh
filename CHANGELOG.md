# Changelog

All notable changes to this knowledge base. Format: Added / Updated / Deprecated / Removed / Security.

## [1.0.0] — 2026-09-20

### Added
- Repository architecture: knowledge (28 areas), skills (25), agents (11), workflows (8), repositories, patterns, prompts, evaluations, datasets, models, standards, anti-patterns, decision-records, experimental, metadata, schemas, scripts, indexes.
- JSON Schemas: skill, repository, source, mcp, agent, evaluation.
- Repository database: 64 records generated from live GitHub API snapshot (`metadata/raw/github-2026-09-20.jsonl`).
  - Notable status findings recorded: AutoGen → MAINTENANCE (successor: Microsoft Agent Framework); browserbase/mcp-server-browser-base → ARCHIVED; React canonical location now `react/react`; Prisma renamed `prisma/orm`; `openai/skills` and `anthropics/skills` have no SPDX license (reference-only).
- MCP registry (12 entries) with security assessments (permissions, exfiltration, injection, poisoning risk).
- Skills library with tier scoring (S/A/B/C) and test-case scaffolds.
- Agent role definitions incl. website-quality-reviewer and fact-checker.
- Workflows: build-website, research-before-coding, analyze-existing-project, bug-investigation, architecture-review, security-review, performance-review, release-checklist.
- Reasoning research section (public sources only: DeepSeek-R1, Open-R1, CoT/ToT/self-consistency/PRM/ORM references).
- Evaluation library: HELM, lm-evaluation-harness, SWE-bench, AgentBench, promptfoo, observability platforms.
- Automation: repositories generator, source scorer, validators (YAML/JSON/schema/frontmatter/duplicates/links/secrets), index generator.
- CI: validate workflow (push/PR), weekly link freshness check, dependabot, issue templates.
- Indexes: generated human + machine-readable (`metadata/index.json`).

### Security
- Copy policy + license intelligence enforced; secret-pattern scanning in CI; MCP security schema mandatory.
- Public-research-only policy for reasoning/model internals codified in AGENTS.md.

## [1.0.1] — 2026-09-20 (prompt-compliance audit)

### Added
- indexes/best-of.md — 15 BEST-OF collections (BEST FOR/WHY/TRADEOFFS/ALTERNATIVES/LAST VERIFIED) [§48].
- metadata/relations.json — knowledge graph: nodes + typed edges (uses/requires/assessed_by/documented_by/implements) [§33].
- decision-records/frontend-stacks.md — 9 stack profiles (default/small/startup/enterprise/data-heavy/marketing/3D/AI SaaS/B2B) [§96].
- knowledge/research/organizations-to-watch.md — 15 org tracking table [§88].
- knowledge/research/huggingface-layer.md — models/datasets/spaces/eval/papers/leaderboards layer [§89].
- sources/papers/ template — full §90 paper record fields incl. paper→code→dataset relations [§90, §91].
- sources/research/YYYY/MM archive convention [§86].

### Fixed
- Prompt-compliance audit against all 105 sections: 7 gaps found and closed in this release.
