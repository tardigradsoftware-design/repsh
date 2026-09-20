# Test 002 — Stale-cache detection
**Setup:** task touching a dependency whose KB record `expires_at` < today.
**Passes if:** agent notices expiry and re-verifies current version/docs before coding.
