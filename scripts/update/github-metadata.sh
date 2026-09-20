#!/usr/bin/env python3
"""Placeholder guards for crawl/update scripts that need network + tokens.

Real refresh flow (run in CI weekly):
  1. gh api repos/<owner>/<repo> for each record → metadata/raw/github-<date>.jsonl
  2. python3 scripts/update/repositories.py  (regenerates YAML records)
  3. python3 scripts/update/links.py         (URL liveness, retries, allowlist)
  4. python3 scripts/generate-index/all.py
"""
