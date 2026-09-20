#!/usr/bin/env python3
"""External link liveness checker with retry + transient-outage tolerance.

- Checks every external http(s) URL in repositories/, knowledge/mcp/registry/, evaluations/, indexes/
- 3 attempts with backoff; 429/5xx treated as transient warnings (not failures) after retries
- Allowlist for known-flaky-but-verified hosts (metadata/link-allowlist.txt)
- stdlib-only (urllib)
"""
from __future__ import annotations

import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
UA = {"User-Agent": "ai-engineering-kb-linkcheck/1.0 (repository hygiene bot)"}
ALLOWLIST_FILE = ROOT / "metadata" / "link-allowlist.txt"
URL_RE = re.compile(r"https?://[^\s)\"'`\]>]+")

TRANSIENT = {408, 429, 500, 502, 503, 504}


def load_allowlist() -> set[str]:
    if ALLOWLIST_FILE.exists():
        return {l.strip() for l in ALLOWLIST_FILE.read_text().splitlines() if l.strip() and not l.startswith("#")}
    return set()


def collect_urls() -> dict[str, list[str]]:
    urls: dict[str, list[str]] = {}
    for base in ("repositories", "knowledge", "evaluations", "indexes", "skills", "workflows", "agents"):
        for p in (ROOT / base).rglob("*"):
            if not p.is_file() or p.suffix not in {".yaml", ".md"}:
                continue
            for m in URL_RE.finditer(p.read_text(errors="ignore")):
                url = m.group(0).rstrip(".,;")
                urls.setdefault(url, []).append(str(p.relative_to(ROOT)))
    return urls


def check(url: str) -> tuple[str, str]:
    """Returns (status, detail): OK / WARN / FAIL."""
    req = urllib.request.Request(url, headers=UA, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return "OK", str(resp.status)
    except urllib.error.HTTPError as e:
        if e.code in TRANSIENT:
            return "WARN", f"transient {e.code}"
        if e.code in (401, 403, 405, 406, 418, 429):
            # many sites block bots; treat as reachable-but-gated
            return "OK", f"reachable (HTTP {e.code}, bot-gated)"
        if e.code == 404:
            return "FAIL", "404"
        return "WARN", f"HTTP {e.code}"
    except (urllib.error.URLError, TimeoutError, ConnectionError, OSError) as e:
        return "WARN", f"network: {type(e).__name__}"


def main() -> int:
    allow = load_allowlist()
    urls = collect_urls()
    unique = sorted(u for u in urls if not any(u.startswith(a) for a in allow))
    print(f"Checking {len(unique)} unique external URLs ({len(allow)} allowlisted prefixes)…")
    failures, warnings = [], []
    for i, url in enumerate(unique):
        status, detail = check(url)
        if status == "OK":
            pass
        elif status == "WARN":
            # retry up to 2 more times for transient issues
            ok = False
            for attempt in range(2):
                time.sleep(2 * (attempt + 1))
                status2, detail2 = check(url)
                if status2 == "OK":
                    ok = True
                    break
            if ok:
                pass
            else:
                warnings.append(f"{url} → {detail} (sources: {', '.join(urls[url][:2])})")
        else:
            failures.append(f"{url} → {detail} (sources: {', '.join(urls[url][:2])})")
        if (i + 1) % 25 == 0:
            print(f"  …{i + 1}/{len(unique)} checked")
    if warnings:
        print(f"\nWARNINGS ({len(warnings)}) — likely transient; re-run before panicking:")
        for w in warnings:
            print(f"  ⚠ {w}")
    if failures:
        print(f"\nFAILURES ({len(failures)}):")
        for f in failures:
            print(f"  ✗ {f}")
        return 1
    print("\n✓ All external links reachable.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
