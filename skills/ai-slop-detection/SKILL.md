---
name: ai-slop-detection
version: 1.0.0
description: Detect, explain, and fix generic AI-generated UI — gradients, glassmorphism abuse, fake metrics, layout monotony — and rewrite toward coherent design
category: frontend
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-03-20
content_type: RECOMMENDATION
tags: [ui, ux, frontend, quality, design]
requires: [frontend-design]
quality:
  authority: 8
  evidence: 8
  recency: 9
  adoption: 8
  reproducibility: 9
  practical_value: 10
  maintenance: 9
---

# AI Slop Detection

## Purpose

Give agents a concrete detector + repair loop for "AI-slop UI": the generic, over-decorated, inconsistent visual language that marks a site as machine-generated. Output is not a vibe judgment — it's a checklist-driven audit with rewrites.

## When to Use

- Reviewing any AI-generated landing page, dashboard, or marketing site before delivery
- User says it "looks generic", "looks AI-made", "template-y"
- Building design systems for new projects (run proactively as a lint pass)

## When NOT to Use

- Deliberately brutalist/retro art direction (the checklist would false-positive; skip aesthetics, keep consistency checks)
- Internal tools where visual polish is explicitly out of scope

## Inputs

- Rendered pages (screenshots, or live DOM via Playwright/DevTools MCP)
- Component code, design tokens (if any), Tailwind config / CSS variables

## Required Context

- `skills/frontend-design` (the positive target state)
- `knowledge/ui-ux/design-system-consistency.md`
- `patterns/ui/` (spacing/typography/motion norms)

## Workflow

```
DETECT → EXPLAIN → RECOMMEND → REWRITE → REVIEW
```

## Detection Checklist (score each 0–2, 2 = clean)

**Color & decoration**
- [ ] Meaningless gradients (gradient-on-gradient, gradient text on gradient bg)
- [ ] Glassmorphism overuse (backdrop-blur everywhere incl. dense data UI)
- [ ] Purple/indigo-to-pink default palette with no brand reason
- [ ] Glow/shadow stacking for depth theater

**Layout & structure**
- [ ] Same dashboard skeleton every screen (sidebar + 4 stat cards + chart + table)
- [ ] 3-column feature grid with icon-top-center-cards, mechanically repeated
- [ ] No typographic hierarchy (everything semibold, similar sizes)
- [ ] Inconsistent spacing (multiple unrelated values; no 4/8px scale)
- [ ] Excessive rounded corners (rounded-3xl on everything)

**Content honesty**
- [ ] Fake metrics ("10k+ users", "99.9% uptime") the product can't substantiate
- [ ] Meaningless badges ("AI-Powered", "Next-Gen", "Revolutionary")
- [ ] Same icon reused for different meanings (lucide `Sparkles` everywhere)
- [ ] Placeholder-looking copy: "Lorem-level" feature blurbs, empty taglines

**Motion**
- [ ] Random floating elements (orbs, blobs) unrelated to content
- [ ] Animations with no cause (things spinning/pulsing constantly)
- [ ] Entrance animations that replay annoyingly on every navigation

**Identity**
- [ ] Default font stack (plain Inter/system with zero typographic identity)
- [ ] No coherent accent color discipline (every section a new color)

## Explanation Format

For each violation:
```markdown
[SEV-HIGH] Fake metrics on landing page
WHY IT'S SLOP: unverifiable claims erode trust instantly with technical audiences
FIX: remove or replace with real, checkable numbers; or reframe as capability statement
```

## Recommendation Heuristics

1. **Subtract first** — remove decoration before adding.
2. **One accent, one neutral ramp** — a disciplined 2-hue system beats a rainbow.
3. **Type does the talking** — a real type scale (12/14/16/20/24/32/48) with weight contrast replaces most decoration needs.
4. **Motion only where meaning** — hover/response feedback, state transitions, one hero moment max.
5. **Real content beats lorem** — write specific copy naming the actual domain.

## Rewrite Phase

Apply fixes in component code (Tailwind: collapse spacing to scale, kill gradient utilities, replace fake stats). Then re-run the checklist. Target: every line 0–1 remaining violations, documented.

## Validation Phase

- [ ] Screenshot before/after comparison produced
- [ ] No fabricated metrics remain
- [ ] Spacing/typography derive from a token scale
- [ ] Animations justified (cause → effect) and honor `prefers-reduced-motion`
- [ ] Contrast ≥ WCAG AA for text

## Failure Modes

- Over-correcting to sterile/empty design — slop removal ≠ removing all personality; keep one strong idea.
- "Fixing" by adding MORE gradients but different ones.
- Stripping personality from a brand that intentionally uses bold gradients (distinguish intent from default).

## Quality Checklist

- [ ] All 5 checklist groups scored
- [ ] Each HIGH issue has a concrete rewrite (not "consider improving")
- [ ] Reduced-motion + contrast verified post-rewrite

## Examples

- Before: purple gradient hero + glass cards + "Trusted by 10,000+ teams" (no customers) + floating orbs. After: neutral bg, single accent, real product screenshot in browser frame, specific copy naming the workflow, one scroll-triggered reveal.

## Anti-Patterns

- Gradient-text headlines as "the fix"
- Replacing fake metrics with vaguer fake claims
- Icon soup swap (Sparkles → Rocket everywhere)

## References

- `knowledge/ui-ux/what-makes-ui-professional.md`
- `patterns/ui/spacing-typography.md`

## Related Skills

frontend-design, code-review, website-quality-reviewer (agent)

## Evaluation Criteria

Given a slop-heavy page: detector finds ≥80% of seeded violations, explanations name user-facing harm, rewrite removes violations without introducing new ones, post-audit checklist passes.
