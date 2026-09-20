# AGENTS.md

> **Read this first.** This file is the operating contract for any AI agent (coding, research, or autonomous) working *on this repository* or *consuming it as a knowledge source*.

## 1. What this repository is

An **AI Engineering Knowledge Base + Skill Registry + Agent Playbook + Research Archive + Tool/MCP Directory + Evaluation Library**.

It exists to make AI agents *make better decisions* — not to dump more files into context. Priority order:

```
RELEVANCE > QUALITY > EVIDENCE > RECENCY > STRUCTURE > RETRIEVABILITY > VALIDATION
```

Its primary consumer is an agent that, when asked e.g. "build a SaaS dashboard with Next.js + TypeScript + Supabase", first retrieves relevant skills, proven repositories, patterns, pitfalls, and evaluation criteria from here — then executes.

## 2. Repository map

| Path | Purpose |
|---|---|
| `knowledge/` | Domain knowledge notes (frontend, backend, security, reasoning, context engineering, …) |
| `skills/` | Reusable agent skills — each with `SKILL.md`, structured workflow, quality metadata |
| `agents/` | Specialized agent role definitions (researcher, architect, fact-checker, …) |
| `workflows/` | End-to-end playbooks that chain skills (build-website, bug-investigation, …) |
| `repositories/` | Verified GitHub repository database (YAML records, live-API-derived) |
| `patterns/` | Named implementation patterns (frontend, DB, agent, animation, architecture) |
| `prompts/` | Structured prompt templates with task/eval/failure-mode metadata |
| `evaluations/` | Benchmarks, eval frameworks, and methodology notes |
| `datasets/` | Public datasets index (reasoning, coding, agents, benchmarks) |
| `models/` | Model cards & capability notes — always with `verified_at` |
| `sources/` | Source records & provenance tracking |
| `standards/` | Normalized standards summaries (AGENTS.md, skill format, MCP) |
| `anti-patterns/` | Failure knowledge, known bugs, gotchas |
| `decision-records/` | Technology selection matrices and ADRs |
| `experimental/` | Unverified candidates — **never** referenced as core knowledge |
| `metadata/` | Raw API snapshots + consolidated machine-readable indexes |
| `schemas/` | JSON Schema for every record type |
| `scripts/` | Validation, scoring, index generation, refresh automation |
| `indexes/` | Generated entry-point indexes (human + machine readable) |
| `.github/` | CI workflows, issue templates, dependabot |

## 3. Ground rules for agents operating here

### Truth & evidence
1. **DON'T GUESS. RESEARCH FIRST.** Prefer `skills/research-before-code` before implementing anything non-trivial.
2. Every factual claim in a committed file must trace to a source with a URL. Cite it.
3. Mark model-generated content as `content_type: GENERATED/RECOMMENDATION`; never record it as fact.
4. Conflicting sources: **surface the conflict** (`confidence: CONFLICTING`) — use the conflict-resolution format in `standards/conflict-resolution.md`.
5. Never present a single number (stars, benchmark score) as timeless. Every volatile value carries `stars_checked_at` / `verified_at` / `expires_at`.

### Legality & safety (hard limits)
6. Never collect, store, or redistribute: private chain-of-thought, stolen model internals, credentials, tokens, cookies, private repo content, personal data, leaked/proprietary system prompts, hacked datasets.
7. Public reasoning research only: open-weight models, published papers, public datasets, reproducible implementations (e.g., DeepSeek-R1, Open-R1).
8. No-license code = **no redistribution**. Record license as `CUSTOM/NOASSERTION` and link instead of copying.
9. Don't wholesale-copy external READMEs. Store summary + key concepts + why/when useful + license + URL (see `standards/copy-policy.md`).

### Adding or changing knowledge
10. New resources start in `experimental/` unless they pass the quality gate in `CONTRIBUTING.md`.
11. Duplicate knowledge is a bug. Use references/links between records; run `scripts/validate/duplicates.py`.
12. Every skill follows the standard `SKILL.md` frontmatter (see `schemas/skill.schema.json` + `standards/skill-format.md`).
13. Update the affected `indexes/` files (or regenerate: `python3 scripts/generate-index/all.py`).
14. Status vocabulary is fixed: repositories use `ACTIVE|STABLE|MAINTENANCE|ARCHIVED|EXPERIMENTAL|ABANDONED|UNKNOWN`; confidence uses `VERY HIGH|HIGH|MEDIUM|LOW|UNVERIFIED|CONFLICTING`.

### Execution behavior
15. Retrieve progressively: index → summary → metadata → relevant section → full skill. Don't read the whole repo.
16. Validate before finishing: `python3 scripts/validate/all.py` must pass.
17. Write for chunking: documents are organized in semantic sections (Overview / When to use / Implementation / Pitfalls / Validation / References) so retrieval can extract just what's needed.

## 4. Build / validate / test commands

```bash
python3 scripts/validate/all.py        # full validation (YAML, JSON, schemas, links, frontmatter, duplicates)
python3 scripts/generate-index/all.py  # regenerate all indexes/
python3 scripts/update/repositories.py # refresh repo records from metadata/raw snapshots
python3 scripts/score/sources.py       # recompute quality scores
```

No external dependencies are required for validation (Python 3.11+ stdlib only). Keep it that way for agent portability.

## 5. When you (the agent) find new knowledge mid-task

Use the self-improvement loop: record what worked/failed/outdated as a **knowledge candidate** in `experimental/` using `templates/` formats. Human review promotes it to core. Never self-promote.
