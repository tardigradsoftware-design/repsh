---
title: Modular Monolith Pattern
category: architecture
confidence: high
updated: 2026-09-20
tags: [architecture]
---

# Modular Monolith (the default)

One deployable; internal modules with explicit ownership boundaries (no reaching into another module's tables — service interfaces only).

## Rules
- Modules own their schema sections; cross-module data via interfaces/events
- Dependency direction documented (domain ← services ← api)
- Extraction path preserved: module boundaries drawn so a future service split is mechanical, not archaeological

## Why default
Microservice costs (networks, versioning, observability, ops) without the org scale that justifies them is the #1 architecture mistake in small teams. Split when: independent deploy cadence + scaling + team ownership demands are PROVEN.
