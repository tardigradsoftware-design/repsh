---
title: Systematic Debugging Method
category: debugging
confidence: high
content_type: RECOMMENDATION
updated: 2026-09-20
verified_at: 2026-09-20
tags: [debugging, method]
---

# Systematic Debugging Method

1. **Reproduce** — reliably, minimally. No repro = instrument first, hypothesize never.
2. **Read the error** — actually read it; past the first line. Check KB `anti-patterns/known-bugs.md`.
3. **Bound the change** — what changed recently (diff, deploy, data, dependency, environment)?
4. **Bisect** — code history (git bisect), data subsets, environment diffs.
5. **Hypotheses ≥2** — write competing explanations + the observation that would decide between them, BEFORE fixing.
6. **Discriminate** — run the decisive observation; let evidence pick.
7. **Fix cause** — smallest correct change at the right layer.
8. **Prove** — regression test fails-before/passes-after; siblings audited for the same class.
9. **Record** — novel gotcha → anti-patterns candidate (experimental pipeline).

## Cognitive traps
Anchoring on the first plausible cause · fixing the symptom (it WILL return) · shotgun changes destroying the evidence.
