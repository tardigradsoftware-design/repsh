# AI Engineering Knowledge Base

> A continuously maintainable, machine-readable **engineering intelligence layer** for AI agents — skill registry, verified repository database, MCP directory, research archive, and evaluation library in one evidence-scored repo.

**Version:** 1.0.0 · **Created:** 2026-09-20 · **Status:** active · **License:** MIT · **CI:** validate + weekly link/metadata refresh

---

## What is this?

A structured knowledge base that AI coding/research agents consult **before** acting. When an agent is asked to build, debug, research, or review something, it should retrieve proven skills, validated tools, known pitfalls, and evaluation criteria from here first — instead of relying purely on training data or guessing.

## The problem it solves

LLM training data goes stale the moment it is frozen. Frameworks get renamed (AutoGen → maintenance; Microsoft Agent Framework takes over), repos move (`facebook/react` → `react/react`), licenses change, and "latest best practice" claims rot. Meanwhile agents invent solutions that mature libraries already solve, hallucinate APIs, and produce generic AI-slop UI.

This repo counters that with **verified, scored, dated, machine-readable knowledge** plus **executable validation** so staleness is detectable, not silent.

## How information is curated

1. **Discover** — via official orgs, research venues, and vetted seed lists (never random awesome-list ingestion).
2. **Verify** — every source checked live: URL, repo existence, archived status, last push, license, maintainer, docs, adoption. Snapshots stored in `metadata/raw/`.
3. **Score** — weighted quality model (authority 20%, maintenance 15%, adoption 15%, documentation 10%, reproducibility 10%, security 10%, recency 10%, evidence 10%) → S/A/B/C tier.
4. **Record** — normalized YAML/JSON conforming to `schemas/`, with `verified_at` / `expires_at` freshness policy.
5. **Maintain** — refresh scripts + CI validation flag stale, broken, or conflicting records.

Nothing enters core knowledge without passing this gate. Unverified candidates live in `experimental/`.

## How an AI agent consumes it

Progressive disclosure — **never read everything**:

```
indexes/topics.md  →  indexes/skills.md  →  skills/<name>/SKILL.md frontmatter
                   →  relevant section   →  referenced source
```

- `AGENTS.md` — operating contract (read first)
- `indexes/skills.md`, `indexes/repositories.md`, `indexes/mcp.md`, `indexes/research.md`, `indexes/evaluations.md`, `indexes/topics.md` — generated entry points
- `metadata/index.json` — consolidated machine-readable index (RAG/vector/API-ready)
- `schemas/*.json` — record contracts for programmatic consumption
- Every document is chunked into semantic sections (Overview / When to use / Implementation / Pitfalls / Validation / References)

## Repository map

```
├── knowledge/        domain notes (28 areas: frontend…reasoning)
├── skills/           26 agent skills with SKILL.md + quality metadata
├── agents/           11 specialized agent role definitions
├── workflows/        8 end-to-end playbooks
├── repositories/     64 verified GitHub records (live-API 2026-09-20)
├── patterns/         named implementation patterns
├── prompts/          structured prompt templates
├── evaluations/      benchmarks + eval methodology
├── datasets/         public dataset index
├── models/           model cards (verified_at + expires_at)
├── standards/        AGENTS.md, skill-format, MCP security norms
├── anti-patterns/    failure knowledge & gotchas
├── decision-records/ tech selection matrices
├── experimental/     unverified candidates (not core)
├── metadata/         raw snapshots + consolidated index.json
├── schemas/          JSON Schema for all record types
├── scripts/          validate / score / generate-index / update
└── .github/          CI, templates, dependabot
```

## Quick start

**Humans:**

```bash
git clone <this-repo>
python3 scripts/validate/all.py   # no dependencies needed
```

**AI agents:** start at `AGENTS.md`, then use `indexes/`.

**Programmatic:** read `metadata/index.json`; validate records against `schemas/*.schema.json`.

## Quality policy (summary)

- Evidence > assumption. Proven patterns > invention. Official sources > blog posts.
- Stars alone never justify inclusion; archived repos are marked, never presented as active.
- Conflicting evidence is surfaced, never hidden.
- Volatile facts carry `verified_at` + `expires_at` (models 7–30d, tools 30–60d, frameworks 30–90d, papers 180–365d, stable specs 365d+).
- Failure knowledge (anti-patterns, gotchas) is first-class — often more valuable than success stories.

## Contributing

See `CONTRIBUTING.md` for the quality gate and submission templates. AI-generated skills enter via `experimental/` → human review → test → promote.

## License

Repository scaffolding and original notes: MIT (see `LICENSE`). Referenced external resources keep their own licenses — this repo links, it does not republish.

## Maintainer commandments

```
DON'T GUESS — RESEARCH FIRST · DON'T COPY — VERIFY FIRST · DON'T TRUST STARS — EVALUATE QUALITY
DON'T USE OUTDATED INFO — CHECK RECENCY · DON'T HALLUCINATE SOURCES — CITE THEM · DON'T OVERLOAD CONTEXT — RETRIEVE PROGRESSIVELY
DON'T REINVENT MATURE SOLUTIONS — SEARCH FIRST · DON'T HIDE CONFLICTS — SURFACE THEM · DON'T TOUCH PRIVATE/STOLEN MODEL INTERNALS — PUBLIC RESEARCH ONLY
```
