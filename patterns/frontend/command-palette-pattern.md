---
title: Command Palette Pattern
category: frontend
confidence: high
updated: 2026-09-20
tags: [navigation, frontend, ux]
---

# Command Palette Pattern (⌘K)

The navigation shortcut of professional tools (Linear/Raycast-class).

## Rules
- ⌘K / Ctrl+K global; triggers: navigation, actions, recent items; fuzzy search with grouped results
- Async results for entity search (debounced); keyboard-first (arrows + enter); escape closes
- Show shortcuts inline; empty state suggests; "no results" offers closest alternatives
- Dynamic actions per context (page-aware commands)

## When not
Content-first marketing sites; apps where <20 destinations exist (plain nav wins).
