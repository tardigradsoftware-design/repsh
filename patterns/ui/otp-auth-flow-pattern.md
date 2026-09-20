---
title: Auth & OTP Flow Pattern
category: ui
confidence: high
updated: 2026-09-20
tags: [auth, ui, ux, security]
---

# Auth & OTP Flow UX

- Email/password: inline validation AFTER blur (not on keystroke), show requirements met progressively, one error style everywhere
- OTP: 6 boxes auto-advance, paste-friendly (splits digits), auto-submit on complete, resend with countdown + changed-channel option, expiry message distinguishes expired vs wrong code
- Never reveal which of email/password was wrong ("invalid credentials")
- Magic-link flows: "check your inbox" state with resend + change-email escapes
- Session: redirect intent preserved through login (deep-link back)
- All states keyboard-first; password managers honored (proper form semantics)
