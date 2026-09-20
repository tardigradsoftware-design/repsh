---
name: competitive-analysis
version: 1.0.0
description: Analyze competitor products/sites for feature, UX, and positioning insight — extract principles, never copy
category: research
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-03-20
content_type: RECOMMENDATION
tags: [research, product, ux, business]
requires: [web-research]
quality: { authority: 7, evidence: 7, recency: 8, adoption: 7, reproducibility: 8, practical_value: 8, maintenance: 8 }
---

# Competitive Analysis

## Purpose
Learn what works in a product space: feature parity maps, UX patterns worth adopting, gaps worth exploiting — ethically (public info, no scraping of private data, no design theft).

## When to Use
Before building a product/feature in an existing market; positioning work; onboarding-flow design.

## When NOT to Use
Copying UI pixel-for-pixel (that's theft, and produces incoherent design anyway).

## Inputs
Competitor list, target user profile, our current product state.

## Required Context
`skills/web-research`, `knowledge/ui-ux/visual-design-research.md` (principle extraction discipline).

## Workflow
INPUT (competitors) → PROCESS (survey → feature map → UX principles → gaps → recommend) → OUTPUT (analysis) → VALIDATION (observations from LIVE verified pages, dated)

## Research Phase
Use each competitor's LIVE site/docs/changelogs/pricing pages today; screenshot + date everything (sites change weekly). Note: verification date mandatory per our visual-design-research standard.

## Planning Phase
Feature map: parity / better / worse / missing. UX principle extraction: what do the good ones DO (layout logic, onboarding steps, pricing anchoring) — described as principles, not pixels.

## Implementation Phase
Output: per-competitor summary + cross-cutting table + "adopt / avoid / exploit-gap" recommendations each tied to OUR product goals.

## Validation Phase
- [ ] All observations dated + from live pages
- [ ] Recommendations tied to user needs (not fashion)
- [ ] No copyrighted content copied

## Failure Modes
Analysis paralysis (analyzing 15 competitors instead of deciding). Survivorship mimicry (copying success without the reasons). Stale screenshots presented as current.

## Quality Checklist
- [ ] Live-page dated evidence · [ ] principles not pixels · [ ] decision-oriented output

## Examples
Scheduling-tool analysis: all leaders do "try without signup"; two hide pricing (signal); gap: none handle timezone-dense teams well → our wedge.

## Anti-Patterns
Feature-list cargo cult. Scraping login-walled content. Treating a competitor's marketing claims as capabilities.

## References
knowledge/ui-ux/visual-design-research.md · skills/web-research

## Related Skills
research-synthesis, project-planning, frontend-design

## Evaluation Criteria
Output changes a concrete product decision (feature prioritized/deprioritized) with dated evidence per claim.
