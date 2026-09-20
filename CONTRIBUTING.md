# Contributing

Thanks for improving this knowledge base. The rules are strict on purpose: **every entry here influences what future AI agents do**, so bad entries are worse than missing entries.

## Quality gate (all resource submissions)

A resource becomes **curated** only after all of:

- [ ] Source is valid and reachable (URL resolves, repo exists)
- [ ] License verified (SPDX id recorded; `CUSTOM/NOASSERTION` flagged; no-license → link-only, never copy)
- [ ] Metadata complete per `schemas/` (every required field)
- [ ] Quality scored via `scripts/score/sources.py` weights
- [ ] Duplicate-checked (`scripts/validate/duplicates.py`)
- [ ] Security-checked (MCP: permissions/exfiltration surface; tools: supply-chain basics)
- [ ] Category assigned + tags applied
- [ ] `verified_at` set; `expires_at` per freshness policy (models 7–30d, GitHub tools 30–60d, frameworks 30–90d, papers 180–365d, stable specs 365d+)
- [ ] Status vocabulary used exactly: `ACTIVE|STABLE|MAINTENANCE|ARCHIVED|EXPERIMENTAL|ABANDONED|UNKNOWN`

## Submission types

Use the issue templates in `.github/ISSUE_TEMPLATE/`:

| Template | For |
|---|---|
| `resource-submission.md` | new repository / tool / MCP / dataset |
| `skill-submission.md` | new agent skill |
| `research-submission.md` | paper / benchmark / method |
| `update-or-stale-report.md` | stale, broken, renamed, archived, or conflicting entry |

## Skill submissions

1. Follow `standards/skill-format.md` exactly (frontmatter + section order).
2. INPUT → PROCESS → OUTPUT → VALIDATION structure; no advice-only skills.
3. Include at least 3 test cases in `skills/<name>/tests/`.
4. Declare `requires:` dependencies; check `standards/skill-conflicts.md` for conflicts.
5. New skills start at `status: experimental`, `tier: Experimental`.

## AI-generated content pipeline

```
AI GENERATED → EXPERIMENTAL/ → HUMAN REVIEW → TEST → EVIDENCE → VALIDATED → CURATED
```

AI agents may add candidates to `experimental/` only. Humans promote. Agents never promote their own output to core.

## Original vs derived

- **ORIGINAL** — our own skills/workflows/checklists (mark `source_type: original`)
- **REFERENCE** — external artifacts (mark `source_type: reference`; summarize, don't republish)

Copy policy: no full README dumps. Store summary, key concepts, why/when useful, limitations, URL, license. See `standards/copy-policy.md`.

## Local validation before opening a PR

```bash
python3 scripts/validate/all.py
python3 scripts/generate-index/all.py   # commit regenerated indexes
```

CI runs the same checks; PRs must pass.
