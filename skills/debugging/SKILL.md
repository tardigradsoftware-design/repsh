---
name: debugging
version: 1.0.0
description: Systematic bug investigation — reproduce, isolate, hypothesize, verify, fix with regression proof
category: debugging
status: active
confidence: high
source_type: original
updated: 2026-09-20
verified_at: 2026-09-20
expires_at: 2027-09-20
content_type: RECOMMENDATION
tags: [debugging, core, quality]
requires: []
quality: { authority: 8, evidence: 8, recency: 8, adoption: 9, reproducibility: 9, practical_value: 10, maintenance: 8 }
---

# Debugging

## Purpose
Replace random fix-trying with a causal investigation that ends in a verified root cause + regression test.

## When to Use
Any bug, flaky test, or "works on my machine" report. Especially before ANY fix attempt.

## When NOT to Use
Explicitly time-boxed experiments (still log findings).

## Inputs
Symptom report, environment, error output, recent changes (`git log/diff`).

## Required Context
`knowledge/debugging/systematic-method.md`; `anti-patterns/known-bugs.md` (known gotchas for the stack).

## Workflow
INPUT (symptom) → PROCESS (reproduce → isolate → hypothesize → verify → fix) → OUTPUT (fix + regression test) → VALIDATION (fails-before/passes-after)

## Research Phase
1. REPRODUCE reliably (deterministic repro or minimal repro; if you can't reproduce, you're guessing).
2. Read the actual error; search this KB's `anti-patterns/` for the exact class (hydration mismatch, RLS bypass, serverless timeout…).
3. Bisect: recent diff? data-dependent? environment-dependent?

## Planning Phase
Form ≥2 competing hypotheses BEFORE fixing; state what evidence would distinguish them.

## Implementation Phase
Fix the cause, not the symptom. Smallest change that addresses root cause. If the "fix" needs 3 hacks stacked — wrong layer.

## Validation Phase
- [ ] Test that FAILS before the fix, PASSES after
- [ ] Similar code paths checked for the same bug class
- [ ] Root cause written in one sentence that a reviewer accepts

## Failure Modes
Shotgun patching. Fixing the repro instead of the cause. Logs removed with the fix (keep diagnostics).

## Quality Checklist
- [ ] Repro exists · [ ] hypotheses stated before fix · [ ] regression test · [ ] sibling paths audited

## Examples
Intermittent 500 in prod route → not reproducible locally → structured logs show DB pool exhaustion at traffic peaks → missing connection-limit config under serverless (known gotcha #23) → fix + load test.

## Anti-Patterns
`try/catch` swallowing to "fix" errors. Redeploy-and-pray. Changing multiple variables at once.

## References
knowledge/debugging/ · anti-patterns/known-bugs.md · agents/ (fact-checker for error-class research)

## Related Skills
browser-testing, security-audit, performance-audit

## Evaluation Criteria
A reviewer can follow: repro → evidence → hypothesis discrimination → minimal fix → regression test.
