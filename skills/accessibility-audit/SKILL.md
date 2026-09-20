---
name: accessibility-audit
version: 1.0.0
description: WCAG-aligned accessibility review — semantics, keyboard, ARIA, contrast, motion sensitivity
category: accessibility
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2026-12-20
content_type: RECOMMENDATION
tags: [accessibility, wcag, a11y, frontend]
requires: []
quality: { authority: 9, evidence: 8, recency: 8, adoption: 8, reproducibility: 9, practical_value: 9, maintenance: 8 }
---

# Accessibility Audit

## Purpose
Make interfaces usable with keyboard, screen readers, and motion sensitivity — the fastest route is semantic HTML + Radix-class primitives, not ARIA patching.

## When to Use
Every UI deliverable; every new component pattern; after any custom interactive widget.

## When NOT to Use
Never (skip only for explicitly internal-only prototypes).

## Inputs
Rendered app + component code.

## Required Context
`knowledge/accessibility/wcag-checklist.md` (verify current WCAG version guidance), radix-ui/primitives record (a11y substrate).

## Workflow
INPUT (app) → PROCESS (semantics → keyboard → ARIA → contrast → motion → SR pass) → OUTPUT (findings + fixes) → VALIDATION (keyboard-only + SR spot-check)

## Research Phase
Automated scan first (catches ~30-40%): headings order, alt text, form labels, contrast. Automation CANNOT verify: focus logic, SR announcements, meaningful alt.

## Planning Phase
Prioritize: keyboard traps & focus order (blockers) → form/SR labeling → contrast → motion.

## Implementation Phase
- Native elements first (`button` not div-with-onClick); Radix primitives for menus/dialogs/popovers.
- Focus visible (never outline:none without replacement); focus moved into modals, restored on close.
- `prefers-reduced-motion` honored globally.
- Alt text meaningful; decorative images `alt=""`.
- Error messages associated with inputs (`aria-describedby`), not color-only.

## Validation Phase
- [ ] Full keyboard walkthrough of critical journeys
- [ ] Screen-reader spot-check (headings land, forms announce, modals trap+restore)
- [ ] Contrast AA (4.5:1 text, 3:1 large/UI) verified per theme incl. dark
- [ ] Automated scans pass

## Failure Modes
ARIA overlay on wrong semantics (div-button with role=button but no keyboard). Focus lost after SPA route change. Carousels with no pause control.

## Quality Checklist
- [ ] Keyboard journey complete · [ ] SR spot-check · [ ] contrast per theme · [ ] reduced-motion

## Examples
Custom dropdown rebuilt on Radix: arrow-key nav, typeahead, aria-activedescendant, Escape/outside-close — previously div soup.

## Anti-Patterns
role="button" everywhere instead of button. Title attributes as tooltips-for-a11y. Autoplaying carousels.

## References
knowledge/accessibility/ · radix-ui/primitives · shadcn-ui/ui

## Related Skills
frontend-implementation, browser-testing, code-review

## Evaluation Criteria
Critical journey completable by keyboard-only + SR spot-check; zero automated-scan violations; contrast verified per theme.
