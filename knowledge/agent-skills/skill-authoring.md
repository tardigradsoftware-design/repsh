---
title: Skill Authoring Guide
category: agent-skills
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [skills, standards]
---

# Skill Authoring Guide

Canonical format: `standards/skill-format.md` + `schemas/skill.schema.json`. Live exemplars: `skills/research-before-code`, `skills/ai-slop-detection`.

## What makes a skill (not a tip)
- INPUT → PROCESS → OUTPUT → VALIDATION shape
- When-to-use AND when-NOT-to-use
- Failure modes section (skills without failure modes are untested opinions)
- Test cases that can fail

## Format rules
- YAML frontmatter exactly per schema; `quality` block scored honestly (scorer recomputes tier).
- Sections in canonical order (parseable by our validators).
- References point to KB-relative paths or absolute URLs with dates.

## Anatomy of workflow steps
Each phase: goal, actions (verb-first), exit criteria. If a phase has no exit criteria, it's decoration.

## Quality bar for promotion (experimental → active)
- Frontmatter complete + valid
- ≥3 test cases, at least one designed to FAIL a bad run
- Duplicate check passed (grep for overlapping skills — link, don't repeat)
- One real-world run recorded (evidence)
