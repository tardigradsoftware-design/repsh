#!/usr/bin/env python3
"""Quality scoring for resources.

Score = weighted mean of quality dimensions (0-10):
  authority 20% | maintenance 15% | adoption 15% | documentation 10%
  reproducibility 10% | security 10% | recency 10% | evidence 10%

Tiers: S ≥8.5 · A ≥7.0 · B ≥5.5 · C ≥4.0 · Experimental <4.0
For repository records (no explicit quality block) dimensions are derived from
record fields.  Writes tier into reports; never mutates curated records.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "validate"))
import _yamlmini as ym  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TODAY = date(2026, 9, 20)

WEIGHTS = {
    "authority": 0.20, "maintenance": 0.15, "adoption": 0.15,
    "documentation": 0.10, "reproducibility": 0.10, "security": 0.10,
    "recency": 0.10, "evidence": 0.10,
}


def tier_for(score: float, status: str = "") -> str:
    if status in ("ARCHIVED", "ABANDONED"):
        return "Deprecated"
    if score >= 8.5:
        return "S"
    if score >= 7.0:
        return "A"
    if score >= 5.5:
        return "B"
    if score >= 4.0:
        return "C"
    return "Experimental"


def repo_dimensions(d: dict) -> dict:
    stars = int(d.get("stars", 0) or 0)
    official = bool(d.get("official"))
    maint = d.get("maintenance_status", "none")
    push = d.get("last_push", "")
    doc = {"excellent": 9, "good": 7, "fair": 5, "poor": 3, "unknown": 3}.get(d.get("documentation_quality"), 3)
    adoption = {"massive": 10, "high": 8, "moderate": 6, "niche": 4, "minimal": 2, "unknown": 2}.get(d.get("community_adoption"), 2)
    security = {"good": 9, "acceptable": 6, "unknown": 3, "concern": 1}.get(d.get("security_status"), 3)
    authority = 9 if official else (6 if stars > 5000 else 4)
    maintenance = {"active": 10, "regular": 8, "sporadic": 5, "stale": 2, "none": 1}.get(maint, 2)
    if d.get("status") == "ARCHIVED":
        maintenance = 1
    recency = 10
    if push:
        try:
            days = (TODAY - date.fromisoformat(push)).days
            recency = 10 if days <= 30 else 8 if days <= 90 else 6 if days <= 180 else 3 if days <= 365 else 1
        except ValueError:
            recency = 3
    reproducibility = 8 if doc >= 7 else 5
    evidence = 8 if d.get("source_verified") else 4
    return {
        "authority": authority, "maintenance": maintenance, "adoption": adoption,
        "documentation": doc, "reproducibility": reproducibility,
        "security": security, "recency": recency, "evidence": evidence,
    }


def score_record(d: dict) -> tuple[float, str, dict]:
    if isinstance(d.get("quality"), dict) and len(d["quality"]) >= 7:
        dims = dict(d["quality"])
        dims.setdefault("evidence", 7)
        dims.setdefault("security", 7)
        dims.setdefault("documentation", 7)
        dims.setdefault("reproducibility", 7)
    else:
        dims = repo_dimensions(d)
    total = sum(dims.get(k, 0) * w for k, w in WEIGHTS.items())
    return round(total, 2), tier_for(total, d.get("status", "")), dims


def main() -> int:
    rows = []
    for p in sorted((ROOT / "repositories").rglob("*.yaml")):
        d = ym.parse(p.read_text())
        score, tier, dims = score_record(d)
        rows.append((score, tier, d.get("name", "?"), d.get("owner", "?"), p.relative_to(ROOT)))
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        fm, _ = ym.parse_frontmatter(p.read_text())
        if not fm:
            continue
        score, tier, dims = score_record(fm)
        rows.append((score, tier, fm.get("name", "?"), "-", p.relative_to(ROOT)))

    rows.sort(reverse=True)
    print(f"{'SCORE':>6}  {'TIER':<12} RESOURCE")
    for score, tier, name, owner, path in rows:
        print(f"{score:6.2f}  {tier:<12} {owner}/{name}  ({path})")

    out = ROOT / "metadata" / "quality-scores.tsv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w") as f:
        f.write("score\ttier\tname\towner\tpath\n")
        for score, tier, name, owner, path in rows:
            f.write(f"{score}\t{tier}\t{name}\t{owner}\t{path}\n")
    print(f"\nWrote {len(rows)} scored resources → {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
