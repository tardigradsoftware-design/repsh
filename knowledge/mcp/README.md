---
title: MCP Registry
category: mcp
confidence: high
updated: 2026-09-20
tags: [mcp, registry]
---

# MCP Registry

12 assessed servers in `registry/` (schema: `schemas/mcp.schema.json`). Repo-level records in `../../repositories/mcp-servers/`.

| Server | Purpose | Risk | Official | Verified |
|---|---|---|---|---|
| playwright-mcp | browser control via a11y tree | medium | ✓ | 2026-09-20 |
| chrome-devtools-mcp | perf traces, console, network | medium | ✓ | 2026-09-20 |
| github-mcp-server | repo/PR/issue automation | medium | ✓ | 2026-09-20 |
| supabase-mcp | project/schema/SQL management | HIGH (write) | ✓ | 2026-09-20 |
| filesystem-mcp | sandboxed file access | medium | ✓ | 2026-09-20 |
| fetch-mcp | URL → markdown reading | medium (exfil/injection) | ✓ | 2026-09-20 |
| memory-mcp | knowledge-graph memory | low (poisoning caveat) | ✓ | 2026-09-20 |
| postgres-mcp | read-only SQL | medium | ✗ reference | 2026-09-20 |
| slack-mcp | messaging | medium (side effects) | ✗ | 2026-09-20 |
| context7 | live library docs retrieval | low | ✗ (Upstash) | 2026-09-20 |
| sequential-thinking | structured reasoning scaffold | low | ✓ | 2026-09-20 |
| sentry-mcp | error triage | low | ✓ | 2026-09-20 |

Rules for enabling any of these: `knowledge/security/mcp-security.md`. Protocol reference: `repositories/mcp-servers/modelcontextprotocol_servers.yaml` + the MCP spec repo record.
