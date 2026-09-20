---
title: Safe Tool Exposure Pattern (MCP)
category: mcp
confidence: high
updated: 2026-09-20
tags: [mcp, security, agents]
---

# Safe Tool Exposure

1. Least toolset: enable only tools the task needs (feature-flag destructive groups — supabase-mcp model)
2. Scoped credentials per server (fine-grained PAT, read-only DB role)
3. Sandbox: container + filesystem roots + egress rules
4. Human gates on external side effects (post/delete/migrate/deploy)
5. Full call logging (tool, args, result size) for audit
6. Re-assess per version bump; pin versions

Reference assessments: knowledge/mcp/registry/ (each entry has permissions + risk grades).
