#!/usr/bin/env python3
"""Duplicate detection: same resource URL recorded in multiple files.

Intentional cross-listing (MCP registry entry + repository record for the same
project) is allowed and reported as INFO, not failure.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _yamlmini as ym  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def main() -> int:
    seen: dict[str, list[str]] = {}
    for base in ("repositories", "knowledge/mcp/registry", "evaluations", "datasets"):
        for p in (ROOT / base).rglob("*"):
            if not p.is_file() or p.suffix not in {".yaml", ".md"}:
                continue
            text = p.read_text(errors="ignore")
            for line in text.splitlines():
                for field in ("url:", "repository:"):
                    if line.strip().startswith(field):
                        url = line.partition(":")[2].strip().strip('"').rstrip("/")
                        if url.startswith("http") and "registry/" in str(p.relative_to(ROOT)):
                            url = f"{url}#{p.stem}"  # registry entries may share repo URLs
                        if url.startswith("http"):
                            seen.setdefault(url, []).append(str(p.relative_to(ROOT)))
    dupes = {u: files for u, files in seen.items() if len(files) > 1 and "#" not in u}
    if dupes:
        print(f"DUPLICATES ({len(dupes)}):")
        for u, files in sorted(dupes.items()):
            joined = "\n      ".join(files)
            print(f"  ✗ {u}\n      {joined}")
        return 1
    print("✓ No unintended duplicates.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
