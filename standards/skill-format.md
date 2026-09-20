---
title: Skill Format Standard
updated: 2026-09-20
---

# Skill Format Standard

Every skill = `skills/<name>/SKILL.md` (+ optional references/ examples/ checklists/ tests/).

## Frontmatter (validated against schemas/skill.schema.json)
```yaml
name: kebab-case        # unique repo-wide
version: X.Y.Z          # semver; CHANGELOG entry on bump
description: ≤300 chars
category: <domain>
status: active|experimental|deprecated|draft
confidence: very-high|high|medium|low|unverified|conflicting
source_type: original|reference|hybrid
updated: YYYY-MM-DD
verified_at: YYYY-MM-DD
expires_at: YYYY-MM-DD  # per freshness policy
content_type: FACT|RECOMMENDATION|EXPERIMENT|OPINION|HYPOTHESIS|UNKNOWN
tags: [...]
requires: [skill-names]  # dependencies
quality: { authority, evidence, recency, adoption, reproducibility, practical_value, maintenance }  # each 0-10
```

## Section order (canonical, parser-checked)
`# <Name>` → Purpose → When to Use → When NOT to Use → Inputs → Required Context → Workflow → Research Phase → Planning Phase → Implementation Phase → Validation Phase → Failure Modes → Quality Checklist → Examples → Anti-Patterns → References → Related Skills → Evaluation Criteria

## Rules
- INPUT → PROCESS → OUTPUT → VALIDATION discipline; advice-only skills rejected
- ≥3 test cases for promotion to active
- Conflicts with other skills → resolve per conflict-resolution.md (priority/authority/scope/recency)
