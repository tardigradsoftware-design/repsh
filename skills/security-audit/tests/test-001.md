# Test 001 — RLS bypass detection
**Setup:** app with one `USING (true)` policy.
**Passes if:** audit finds it, grades CRITICAL, provides policy fix + role-matrix test.
