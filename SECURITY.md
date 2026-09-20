# Security Policy

## Scope

This repository is a knowledge base — it contains no runtime services. Security concerns fall into three classes:

1. **Content security** — malicious or dangerous recommendations, poisoned skill/tool entries, prompt-injection payloads embedded in referenced resources.
2. **Supply-chain security** — referenced packages, MCP servers, or scripts that could harm agents that follow this repo.
3. **Repository hygiene** — leaked secrets in history, vulnerable CI actions.

## Reporting a vulnerability

Open a **private** security advisory via GitHub → Security → "Report a vulnerability", or use a `update-or-stale-report` issue marked non-sensitive if it's pure content correction. Do not post exploit details publicly.

**Response target:** acknowledgment within 72h, assessment within 7 days.

## Content security rules (enforced on every PR)

- **No prompt-injection surfaces:** skills must not instruct agents to exfiltrate secrets, ignore operator instructions, or phone home.
- **MCP entries require a security assessment:** permissions (filesystem/network/credentials/database/code-execution), `data_exfiltration_risk`, `prompt_injection_surface`, `tool_poisoning_risk` per `schemas/mcp.schema.json`. Write-capable servers must state scoping guidance.
- **No credential-shaped data:** API keys, tokens, cookies, or session material are never stored here, even as "examples" (CI scans for patterns).
- **Supply-chain notes:** tools recommended here must have a verifiable upstream (official org or audited maintainer); typosquat-prone package names get an explicit disambiguation note.
- **License scan:** no-license content is linked, never vendored.

## What this repo will never contain

Private chain-of-thought, stolen model internals, leaked proprietary system prompts, credentials, hacked datasets, personal data, or private enterprise information. Public reasoning research only (open weights, published papers, reproducible implementations).

## CI enforcement

`.github/workflows/validate.yml` runs: YAML/JSON/schema validation, frontmatter lint, duplicate detection, link checking (with retry + allowlist for transient outages), secret-pattern scanning, and referenced-file existence checks.
