---
name: frontend-design
version: 1.0.0
description: Professional frontend design workflow — coherent design systems, premium SaaS aesthetics, and disciplined visual decisions for web applications
category: frontend
status: active
confidence: high
source_type: hybrid
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-03-20
content_type: RECOMMENDATION
tags: [ui, ux, frontend, design, saas, web]
requires: [research-before-code, ai-slop-detection]
quality:
  authority: 8
  evidence: 8
  recency: 9
  adoption: 9
  reproducibility: 8
  practical_value: 10
  maintenance: 9
---

# Frontend Design

## Purpose

Produce interfaces that look intentionally designed: coherent design system, clear hierarchy, disciplined color/type/motion — the opposite of default-looking AI output.

## When to Use

- Any new web UI: marketing site, SaaS dashboard, B2B tool, landing page
- Restyling existing apps that drifted visually

## When NOT to Use

- Pure logic work (APIs, jobs) — use backend-engineering
- Quick prototypes explicitly labeled throwaway (still keep contrast/accessibility)

## Inputs

- Product domain + audience (developer? enterprise buyer? consumer?)
- Brand constraints (logo, colors, existing patterns) or freedom to define
- Content inventory (real copy/screenshots if available)

## Required Context

- `knowledge/ui-ux/what-makes-ui-professional.md` — principles extracted from Linear/Stripe/Vercel/Apple-class products
- `knowledge/ui-ux/avoiding-ai-slop-ui.md` — what to avoid
- `knowledge/ui-ux/animation-principles.md`, `knowledge/frontend/animation-knowledge.md`
- `repositories/frontend/` — verified component libraries (shadcn-ui/ui, radix-ui/primitives, TanStack/table, motiondivision/motion)
- `skills/ai-slop-detection` — the lint pass

## Workflow

INPUT (domain, audience, content) → PROCESS (system definition → layout → component → polish) → OUTPUT (implemented, tokenized UI) → VALIDATION (audit checklist + screenshots)

## Research Phase

1. Study 2–3 best-in-class products in the same genre (note layout principles, NOT pixel copying — see `knowledge/ui-ux/visual-design-research.md`).
2. Verify current versions: Next.js/React/Tailwind/shadcn releases move fast (check `repositories/frontend/*.yaml` `last_push`).
3. Collect real content — headings, feature names, numbers you can defend.

## Planning Phase

Define the design system BEFORE components:

```markdown
# Design tokens
Type scale: 12/14/16/20/24/32/48 (one display face + one UI face max)
Space scale: 4/8/12/16/24/32/48/64/96
Color: 1 neutral ramp (10 steps), 1 accent, ≤2 semantic (success/danger)
Radius: pick 1–2 values, apply consistently
Elevation: shadows for overlays only; borders for structure
Motion: 150–200ms ease-out interactions; 300–500ms entrances; nothing loops without cause
Grid: 12-col fluid, max-width per content type (prose 65–75ch, dashboards full)
```

## Implementation Phase

1. Tokens first (CSS variables / Tailwind theme), then primitives (shadcn/Radix), then composed components, then pages.
2. Build the hardest screen first (usually the data-dense one) — it exposes system weaknesses early.
3. Data-dense screens: TanStack/table for grids, command palettes for navigation, skeletons (not spinners) for loads.
4. Marketing pages: one strong hero idea; specific copy; real product visuals; one signature motion moment.

## Validation Phase

Run `ai-slop-detection` checklist. Then:

- [ ] Typography: clear 3+ level hierarchy on every screen
- [ ] Spacing: every value from the scale; optical rhythm consistent
- [ ] Color: accent used sparingly (<10% of surface); semantic colors only for semantics
- [ ] All interactive elements have hover/focus/active states incl. keyboard focus-visible
- [ ] Dark mode (if shipped) re-checks contrast, not just inverts
- [ ] Responsive: 375px, 768px, 1440px screenshots reviewed
- [ ] `prefers-reduced-motion` honored
- [ ] Empty/loading/error states designed (not afterthoughts)

## Failure Modes

- **Token drift** — ad-hoc values sneak in. Counter: lint config for arbitrary Tailwind values in CI where possible.
- **Dashboard genericism** — every screen same skeleton. Counter: vary information density and layout per task; let content shape layout.
- **Decoration-first thinking** — adding gradients to fix blandness. Counter: fix hierarchy and contrast first; add ≤1 expressive element per screen.

## Quality Checklist

- [ ] Design tokens defined before components
- [ ] Hardest screen built first
- [ ] ai-slop checklist scored ≥90%
- [ ] All states designed (loading/empty/error)
- [ ] Accessibility AA contrast + focus states

## Examples

- Premium SaaS shell: fixed sidebar (icon+label, collapsible), top bar with command palette (⌘K), content max-width ~1200px, data tables with sticky headers, toasts bottom-right. Reference principle set in `knowledge/ui-ux/`.

## Anti-Patterns

- 5 fonts "for variety"
- Color-coding by section until the app looks like a carnival
- Skeleton screens that flash (threshold: only show after ~300ms delay)
- Icon+text duplication on every button

## References

- `knowledge/ui-ux/what-makes-ui-professional.md` (primary)
- `patterns/ui/`, `patterns/animation/`
- `repositories/frontend/` records (versions verified 2026-09-20)

## Related Skills

frontend-implementation, ai-slop-detection, accessibility-audit, performance-audit, website-quality-reviewer

## Evaluation Criteria

Output passes when: tokens exist and are respected; three screenshots (mobile/tablet/desktop) reviewed; slop checklist ≥90%; contrast AA; states designed; one reviewer could rebuild a missing screen using only the token sheet.
