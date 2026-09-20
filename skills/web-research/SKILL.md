---
name: web-research
version: 1.0.0
description: Multi-source web research with search, cross-checking, extraction, citation, and ranking — never decide on a single source
category: research
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [research, web, core]
requires: [source-validation]
quality:
  authority: 8
  evidence: 8
  recency: 9
  adoption: 8
  reproducibility: 9
  practical_value: 10
  maintenance: 9
---

# Web Research

## Purpose
Answer questions with ranked, cross-checked, cited evidence instead of the first search hit.

## When to Use
- Any factual question where your training data may be stale
- Technology selection, "what's the current best approach", error investigation
- Pre-coding research phase (feeds research-before-code)

## When NOT to Use
- Questions answerable definitively from stable specs/docs you already verified

## Inputs
Question(s); optionally constraints (recency window, source-type preferences).

## Required Context
skills/source-validation; discovery terms in `standards/discovery-terms.md`.

## Workflow
INPUT (question) → PROCESS (search → open → compare → cross-check → extract → cite → rank → summarize) → OUTPUT (evidence-backed answer) → VALIDATION (≥2 sources or UNVERIFIED)

## Research Phase
1. Decompose the question into independent sub-questions.
2. Search per sub-question; vary phrasing; include year qualifier when freshness matters.
3. Prefer: official docs > official repos > papers > maintainer blogs > community.
4. OPEN the top candidates (don't trust snippets).
5. CROSS-CHECK load-bearing facts across ≥2 independent origins.

## Planning Phase
Rank evidence: authority × recency × independence. Note conflicts explicitly.

## Implementation Phase
Answer format:
```markdown
**Answer:** …
**Evidence:** [1] official docs (verified 2026-09-20) · [2] …
**Confidence:** HIGH/MEDIUM/LOW
**Conflicts:** Source 1 says X, Source 2 says Y — likely because …
**Stale risk:** re-verify by <date>
```

## Validation Phase
- [ ] No claim from a single low-grade source
- [ ] Dates on volatile facts
- [ ] Answer states what would change the conclusion

## Failure Modes
- Snippet trust (answering from search-result preview)
- SEO capture (content farms outranking truth) — counter with source-priority discipline
- Answer drift beyond the question scope

## Quality Checklist
- [ ] ≥2 sources or labeled UNVERIFIED · [ ] citations resolve · [ ] confidence + stale-risk stated

## Examples
"Does Next.js 16 need X config for Y?" → official Next docs → GitHub release notes → verified answer with doc citation + version pin.

## Anti-Patterns
Treating one popular blog as consensus. Forgetting that docs.rank ≠ truth.rank.

## References
skills/source-validation · standards/discovery-terms.md · knowledge/research/

## Related Skills
research-before-code, evidence-validation, competitive-analysis, research-synthesis

## Evaluation Criteria
Given a question with deliberately misleading top results, the skill reaches the correct answer via lower-ranked authoritative sources and flags the conflict.
