---
title: ADR-001: This KB uses file-based records + generated indexes (no database)
date: 2026-09-20
status: accepted
---

# ADR-001: File-based records + generated indexes

## Context
Knowledge base must be consumable by agents (RAG/vector/API-ready later), versionable by git, validatable in CI, and zero-infra for contributors.

## Decision
YAML/JSON records in plain directories; `metadata/index.json` + `indexes/*.md` GENERATED from records by scripts; no runtime database.

## Consequences
+ zero infra, git-native review, CI-validatable, RAG-importable later (schemas normalize shape)
− cross-record queries require regeneration (acceptable: generate-index script, seconds)
− scale ceiling (thousands of records fine; millions would need real storage — out of scope)

## Alternatives rejected
SQLite store — breaks git review ergonomics. Hosted CMS — external dependency, violates zero-infra goal.

## Revisit by
When record count or query complexity outgrows generated indexes.
