---
title: Data Table Pattern (Enterprise UI)
category: frontend
confidence: high
updated: 2026-09-20
tags: [tables, frontend, data-heavy]
---

# Data Table Pattern

Enterprise/data-heavy UIs live or die here. Stack: TanStack/table (headless) + shadcn styling (records verified 2026-09-20).

## Requirements checklist
- Sticky header (+ sticky first column for wide sets) · column visibility prefs persisted
- Server-side: sorting, filtering, keyset pagination (never OFFSET at scale)
- Row selection with bulk actions bar · loading = skeleton rows · empty state with next action
- Cell renderers: badges for status, relative time with absolute title, truncation with tooltip
- Density toggle (comfortable/compact) for data-dense users
- Keyboard: arrows navigate, Enter opens, space selects

## Failure modes
Client-side pagination of 10k+ rows (memory + latency lie). Filter state lost on reload (put in URL). Column widths jumping when data loads.
