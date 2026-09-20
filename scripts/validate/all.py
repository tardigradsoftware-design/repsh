#!/usr/bin/env python3
"""Master validator — runs every check. Exit code 0 = all pass.

Checks:
 1. JSON files parse
 2. JSON Schema files valid JSON with required fields
 3. YAML records parse (repositories/, knowledge/mcp/registry/, prompts/)
 4. MCP records conform to schemas/mcp.schema.json
 5. Skill SKILL.md: frontmatter valid + canonical section order + quality block
 6. AGENT.md files have frontmatter
 7. Duplicate resource detection (same URL in two records)
 8. Internal link/file reference check
 9. Secret-pattern scan
10. Repository record status vocabulary check
11. Generated index freshness (indexes match current records)
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import _yamlmini as ym  # noqa: E402
import _schemamini as sm  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
ERRORS: list[str] = []
WARNINGS: list[str] = []


def err(msg):
    ERRORS.append(msg)


def warn(msg):
    WARNINGS.append(msg)


def check_json_files():
    for p in ROOT.rglob("*.json"):
        if ".git" in p.parts:
            continue
        try:
            json.loads(p.read_text())
        except Exception as e:
            err(f"JSON parse failed: {p.relative_to(ROOT)} — {e}")


def check_schemas():
    for p in sorted((ROOT / "schemas").glob("*.json")):
        try:
            s = json.loads(p.read_text())
        except Exception as e:
            err(f"schema invalid: {p.name} — {e}")
            continue
        for field in ("$id", "title", "type", "properties"):
            if field not in s:
                err(f"schema {p.name} missing '{field}'")


def check_yaml_records():
    for d in ("repositories", "knowledge/mcp/registry", "prompts"):
        base = ROOT / d
        if not base.exists():
            continue
        for p in base.rglob("*.yaml"):
            try:
                data = ym.parse(p.read_text())
            except Exception as e:
                err(f"YAML parse failed: {p.relative_to(ROOT)} — {e}")
                continue
            if not isinstance(data, dict) or not data:
                err(f"YAML empty/invalid: {p.relative_to(ROOT)}")


def check_mcp_schema():
    schema = sm.load_schema(ROOT / "schemas" / "mcp.schema.json")
    for p in sorted((ROOT / "knowledge" / "mcp" / "registry").glob("*.yaml")):
        data = ym.parse(p.read_text())
        for e in sm.validate(data, schema):
            ERRORS.append(f"MCP schema: {p.name} — {e.split(': ', 1)[-1]}")


SKILL_SECTIONS = [
    "Purpose", "When to Use", "When NOT to Use", "Inputs", "Required Context",
    "Workflow", "Research Phase", "Planning Phase", "Implementation Phase",
    "Validation Phase", "Failure Modes", "Quality Checklist", "Examples",
    "Anti-Patterns", "References", "Related Skills", "Evaluation Criteria",
]


def check_skills():
    skills_dir = ROOT / "skills"
    names = {p.parent.name for p in skills_dir.glob("*/SKILL.md")}
    for p in sorted(skills_dir.glob("*/SKILL.md")):
        text = p.read_text()
        fm, body = ym.parse_frontmatter(text)
        rel = p.relative_to(ROOT)
        if fm is None:
            err(f"skill frontmatter missing: {rel}")
            continue
        # required frontmatter fields
        for field in ("name", "version", "description", "category", "status",
                      "confidence", "source_type", "updated"):
            if field not in fm:
                err(f"skill {rel}: frontmatter missing '{field}'")
        if fm.get("name") != p.parent.name:
            err(f"skill {rel}: frontmatter name != directory name")
        if not re.match(r"^\d+\.\d+\.\d+$", str(fm.get("version", ""))):
            err(f"skill {rel}: bad version")
        # quality block
        q = fm.get("quality")
        if not isinstance(q, dict) or len(q) < 7:
            err(f"skill {rel}: quality block incomplete (7 dims required)")
        else:
            for k, v in q.items():
                if not isinstance(v, (int, float)) or v < 0 or v > 10:
                    err(f"skill {rel}: quality.{k} out of range")
        # section order (only check the ones present, in canonical order)
        positions = []
        for sec in SKILL_SECTIONS:
            idx = body.find(f"## {sec}")
            if idx != -1:
                positions.append((idx, sec))
        secs_in_order = [s for _, s in positions]
        canonical = [s for s in SKILL_SECTIONS if s in secs_in_order]
        if secs_in_order != canonical:
            err(f"skill {rel}: section order violates canonical order: {secs_in_order}")
        # requires point to real skills
        for req in fm.get("requires", []) or []:
            if req not in names:
                err(f"skill {rel}: requires unknown skill '{req}'")
    # each skill dir has SKILL.md
    for d in sorted(skills_dir.iterdir()):
        if d.is_dir() and not (d / "SKILL.md").exists():
            err(f"skill directory missing SKILL.md: {d.relative_to(ROOT)}")


def check_agents():
    for p in sorted((ROOT / "agents").glob("*/AGENT.md")):
        fm, _ = ym.parse_frontmatter(p.read_text())
        if fm is None:
            err(f"agent frontmatter missing: {p.relative_to(ROOT)}")
        else:
            for field in ("name", "role", "goal", "version"):
                if field not in fm:
                    err(f"agent {p.parent.name}: missing '{field}'")


def check_repository_status_vocab():
    vocab = {"ACTIVE", "STABLE", "MAINTENANCE", "ARCHIVED", "EXPERIMENTAL", "ABANDONED", "UNKNOWN"}
    conf = {"VERY HIGH", "HIGH", "MEDIUM", "LOW", "UNVERIFIED", "CONFLICTING"}
    for p in (ROOT / "repositories").rglob("*.yaml"):
        data = ym.parse(p.read_text())
        if data.get("status") not in vocab:
            err(f"{p.relative_to(ROOT)}: bad status '{data.get('status')}'")
        if data.get("confidence") not in conf:
            err(f"{p.relative_to(ROOT)}: bad confidence '{data.get('confidence')}'")
        if "stars_checked_at" not in data:
            err(f"{p.relative_to(ROOT)}: missing stars_checked_at")
        if "license" not in data:
            err(f"{p.relative_to(ROOT)}: missing license field")


def check_duplicates():
    url_owner: dict[str, str] = {}
    for base in ("repositories", "knowledge/mcp/registry"):
        for p in (ROOT / base).rglob("*.yaml"):
            data = ym.parse(p.read_text())
            url = data.get("url") or data.get("repository")
            if isinstance(url, str) and url.startswith("http"):
                canon = url.rstrip("/").lower()
                # registry entries intentionally repeat upstream repo — group by name too
                key = (canon, data.get("name", p.stem))
                if canon in url_owner and url_owner[canon] != p.name:
                    # allowed: repository record + mcp registry entry for same project
                    if not (base.endswith("registry") or "/registry/" in str(url_owner_path[canon])):
                        warn(f"duplicate URL: {canon} in {p.relative_to(ROOT)} and {url_owner[canon]}")
                url_owner[canon] = p.name
                url_owner_path[canon] = p


url_owner_path: dict = {}


def check_internal_links():
    # markdown links to repo-relative files must exist
    link_re = re.compile(r"\[[^\]]*\]\(([^)#]+?)\)")
    md_files = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
    for p in md_files:
        text = p.read_text()
        for m in link_re.finditer(text):
            target = m.group(1).strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (p.parent / target).resolve()
            if not resolved.exists():
                err(f"broken internal link in {p.relative_to(ROOT)}: '{target}'")


SECRET_PATTERNS = [
    (r"sk-[A-Za-z0-9]{20,}", "OpenAI-style key"),
    (r"ghp_[A-Za-z0-9]{30,}", "GitHub PAT"),
    (r"github_pat_[A-Za-z0-9_]{30,}", "GitHub fine-grained PAT"),
    (r"xox[baprs]-[A-Za-z0-9-]{10,}", "Slack token"),
    (r"-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----", "private key"),
    (r"eyJ[A-Za-z0-9_-]{30,}\.[A-Za-z0-9_-]{20,}", "JWT-shaped secret"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key"),
    (r"sbp_[A-Za-z0-9]{30,}", "Supabase service key shape"),
]


def check_secrets():
    allow_docs = ("docs about tokens",)
    for p in ROOT.rglob("*"):
        if ".git" in p.parts or p.is_dir():
            continue
        if p.suffix not in {".md", ".yaml", ".json", ".py", ".yml", ".toml"}:
            continue
        text = p.read_text(errors="ignore")
        for pat, label in SECRET_PATTERNS:
            m = re.search(pat, text)
            if m:
                # the SECURITY.md documents patterns themselves — that's fine
                if p.name == "SECURITY.md" or "SECURITY_PATTERNS" in text:
                    continue
                err(f"possible secret ({label}) in {p.relative_to(ROOT)}: {m.group(0)[:12]}…")


def check_index_freshness():
    idx = ROOT / "indexes"
    if not (idx / "skills.md").exists():
        err("indexes/skills.md missing (run scripts/generate-index/all.py)")
        return
    n_skills = len(list((ROOT / "skills").glob("*/SKILL.md")))
    idx_text = (idx / "skills.md").read_text()
    if f"({n_skills} skills)" not in idx_text:
        warn("indexes/skills.md count stale — regenerate")


def main() -> int:
    check_json_files()
    check_schemas()
    check_yaml_records()
    check_mcp_schema()
    check_skills()
    check_agents()
    check_repository_status_vocab()
    url_owner_path.clear()
    check_duplicates()
    check_internal_links()
    check_secrets()
    check_index_freshness()

    if WARNINGS:
        print("WARNINGS:")
        for w in WARNINGS:
            print(f"  ⚠ {w}")
    if ERRORS:
        print(f"ERRORS ({len(ERRORS)}):")
        for e in ERRORS:
            print(f"  ✗ {e}")
        return 1
    print("✓ All validation checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
