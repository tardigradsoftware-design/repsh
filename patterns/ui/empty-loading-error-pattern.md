---
title: Empty / Loading / Error State Pattern
category: ui
confidence: high
updated: 2026-09-20
tags: [ui, states, ux]
---

# States Pattern (the professionalism giveaway)

- **Loading:** skeletons after ~300ms delay (no flash); match final layout shapes; never spinners for lists.
- **Empty:** three jobs — say what this is, why it's empty, give the next action (button). Example data > blank voids.
- **Error:** human message + what user can do + retry affordance + error reference id for support. Never raw stack traces.
- **Partial:** show good data + badge the failed section (don't blank the page for one failed widget).

Every data surface ships all four. Missing states = the difference between "demo" and "product".
