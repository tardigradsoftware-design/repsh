#!/usr/bin/env python3
"""Generate all indexes/ + metadata/index.json from current records.

Progressive disclosure entry points for agents: summary tables with counts,
tiers, status, and links. Always regenerate after adding records.
"""
from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "validate"))
import _yamlmini as ym  # noqa: E402
sys.path.insert(0, str(Path(__file__).parent.parent / "score"))
from sources import score_record  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
TODAY = date(2026, 9, 20).isoformat()


def load_repos() -> list[dict]:
    out = []
    for p in sorted((ROOT / "repositories").rglob("*.yaml")):
        d = ym.parse(p.read_text())
        d["_path"] = str(p.relative_to(ROOT))
        score, tier, _ = score_record(d)
        d["_score"], d["_tier"] = score, tier
        out.append(d)
    return out


def load_skills() -> list[dict]:
    out = []
    for p in sorted((ROOT / "skills").glob("*/SKILL.md")):
        fm, _ = ym.parse_frontmatter(p.read_text())
        if not fm:
            continue
        fm["_path"] = str(p.relative_to(ROOT))
        score, tier, _ = score_record(fm)
        fm["_score"], fm["_tier"] = score, tier
        out.append(fm)
    return out


def load_mcp() -> list[dict]:
    out = []
    for p in sorted((ROOT / "knowledge" / "mcp" / "registry").glob("*.yaml")):
        d = ym.parse(p.read_text())
        d["_path"] = str(p.relative_to(ROOT))
        out.append(d)
    return out


def load_agents() -> list[dict]:
    out = []
    for p in sorted((ROOT / "agents").glob("*/AGENT.md")):
        fm, _ = ym.parse_frontmatter(p.read_text())
        if fm:
            fm["_path"] = str(p.relative_to(ROOT))
            out.append(fm)
    return out


def load_workflows() -> list[dict]:
    out = []
    for p in sorted((ROOT / "workflows").glob("*/WORKFLOW.md")):
        fm, _ = ym.parse_frontmatter(p.read_text())
        if fm:
            fm["_path"] = str(p.relative_to(ROOT))
            out.append(fm)
    return out


def fmt_status(s: str) -> str:
    flag = {"ARCHIVED": "🗄", "MAINTENANCE": "⏸", "ABANDONED": "✖"}.get(s, "")
    return f"{s}{flag}" if flag else s


def gen_repositories(repos) -> str:
    lines = [
        "# Repository Index",
        f"Auto-generated {TODAY} — do not edit by hand; run `python3 scripts/generate-index/all.py`.",
        f"{len(repos)} verified records. Scores from scripts/score/sources.py weights.",
        "",
        "| Resource | Category | Status | Tier | Score | Confidence | Record |",
        "|---|---|---|---|---|---|---|",
    ]
    for d in sorted(repos, key=lambda x: -x["_score"]):
        lines.append(
            f"| **{d.get('owner')}/{d.get('name')}** | {d.get('category')} | "
            f"{fmt_status(d.get('status', '?'))} | {d['_tier']} | {d['_score']} | "
            f"{d.get('confidence')} | [`{d['_path']}`](../{d['_path']}) |"
        )
    return "\n".join(lines) + "\n"


def gen_skills(skills) -> str:
    lines = [
        "# Skills Index",
        f"Auto-generated {TODAY}. {len(skills)} skills.",
        "",
        "Retrieval order: this index → SKILL.md frontmatter → relevant section → references.",
        "",
        "| Skill | Category | Status | Tier | Score | Requires |",
        "|---|---|---|---|---|---|",
    ]
    for s in sorted(skills, key=lambda x: -x["_score"]):
        req = ", ".join(s.get("requires", []) or []) or "—"
        lines.append(
            f"| [`{s.get('name')}`](../{s['_path']}) | {s.get('category')} | "
            f"{s.get('status')} | {s['_tier']} | {s['_score']} | {req} |"
        )
    lines.append("")
    lines.append("## By category")
    cats: dict[str, list] = {}
    for s in skills:
        cats.setdefault(s.get("category", "misc"), []).append(s.get("name"))
    for c in sorted(cats):
        lines.append(f"- **{c}**: {', '.join(sorted(cats[c]))}")
    return "\n".join(lines) + f"\n\n({len(skills)} skills)\n"


def gen_mcp(mcps) -> str:
    lines = [
        "# MCP Index",
        f"Auto-generated {TODAY}. {len(mcps)} assessed servers.",
        "",
        "| Server | Official | Risk | Exfil | Injection | Setup | Record |",
        "|---|---|---|---|---|---|---|",
    ]
    for m in mcps:
        lines.append(
            f"| {m.get('name')} | {'✓' if m.get('official') else '✗'} | "
            f"{m.get('security_risk')} | {m.get('data_exfiltration_risk')} | "
            f"{m.get('prompt_injection_surface')} | {m.get('setup_complexity')} | "
            f"[`{m['_path']}`](../{m['_path']}) |"
        )
    lines.append("")
    lines.append("Enablement rules: `knowledge/security/mcp-security.md`.")
    return "\n".join(lines) + "\n"


def gen_agents(agents) -> str:
    lines = ["# Agents Index", f"Auto-generated {TODAY}. {len(agents)} role definitions.", "",
             "| Agent | Role | Skills used |", "|---|---|---|"]
    for a in agents:
        lines.append(f"| [`{a.get('name')}`](../{a['_path']}) | {a.get('role')} | {', '.join(a.get('skills_used', []) or []) or '—'} |")
    return "\n".join(lines) + "\n"


def gen_workflows(wfs) -> str:
    lines = ["# Workflows Index", f"Auto-generated {TODAY}. {len(wfs)} playbooks.", "",
             "| Workflow | Skills chained |", "|---|---|"]
    for w in wfs:
        lines.append(f"| [`{w.get('name')}`](../{w['_path']}) | {', '.join(w.get('skills', []) or []) or '—'} |")
    return "\n".join(lines) + "\n"


def gen_topics() -> str:
    areas = sorted(p.name for p in (ROOT / "knowledge").iterdir() if p.is_dir())
    notes = sum(1 for p in (ROOT / "knowledge").rglob("*.md"))
    lines = [
        "# Topics Index",
        f"Auto-generated {TODAY}. {len(areas)} knowledge areas, {notes} notes.",
        "",
        "Start here to find domain knowledge. Each area folder holds dated, confidence-labeled notes.",
        "",
    ]
    for a in areas:
        n = len(list((ROOT / "knowledge" / a).rglob("*.md")))
        lines.append(f"- **{a}** ({n} notes) — `knowledge/{a}/`")
    lines += ["", "Cross-cutting: `standards/` · `anti-patterns/` · `decision-records/` · `patterns/` · `case-studies/`"]
    return "\n".join(lines) + "\n"


def gen_research() -> str:
    lines = ["# Research Index", f"Auto-generated {TODAY}.", "",
             "Public research only (no private CoT / stolen internals — see SECURITY.md).", "",
             "| Area | Entry | Record |", "|---|---|---|"]
    entries = [
        ("Reasoning map", "CoT→PRM/ORM→test-time compute + open implementations", "knowledge/reasoning/public-reasoning-research.md"),
        ("Open reasoning models", "DeepSeek-R1 · Open-R1 (reproduction + datasets)", "repositories/research/"),
        ("Tool-use research", "Gorilla / BFCL line", "repositories/research/shishirpatil_gorilla.yaml"),
        ("Papers layer", "paper→code→dataset relations", "sources/ + repositories/research/"),
        ("Discovery", "sources + search terms", "knowledge/research/discovery-sources.md"),
    ]
    for a, b, c in entries:
        lines.append(f"| {a} | {b} | `{c}` |")
    return "\n".join(lines) + "\n"


def gen_evaluations() -> str:
    lines = ["# Evaluations Index", f"Auto-generated {TODAY}.", "",
             "| Entry | Domain |", "|---|---|",
             "| [README table](../evaluations/README.md) | benchmark library |",
             "| [KB eval suite (25 tasks)](../evaluations/agents/kb-eval-suite.md) | this repo |",
             "| [SWE-bench notes](../evaluations/coding/swe-bench-notes.md) | coding |",
             "| [Reasoning benchmarks](../evaluations/reasoning/benchmarks.md) | reasoning |",
             "| [Web-agent benchmarks](../evaluations/web/web-agent-benchmarks.md) | web |",
             "| [Agent metrics](../knowledge/evaluation/agent-evaluation-metrics.md) | methodology |"]
    return "\n".join(lines) + "\n"


def gen_machine_index(repos, skills, mcps, agents, wfs) -> dict:
    return {
        "generated_at": TODAY,
        "description": "Machine-readable index of the AI Engineering Knowledge Base",
        "counts": {"repositories": len(repos), "skills": len(skills), "mcp_servers": len(mcps),
                   "agents": len(agents), "workflows": len(wfs)},
        "skills": [{"name": s.get("name"), "category": s.get("category"), "status": s.get("status"),
                    "tier": s["_tier"], "score": s["_score"], "tags": s.get("tags", []),
                    "requires": s.get("requires", []), "path": s["_path"],
                    "summary": s.get("description")} for s in skills],
        "repositories": [{"name": d.get("name"), "owner": d.get("owner"), "url": d.get("url"),
                          "category": d.get("category"), "status": d.get("status"),
                          "license": d.get("license"), "stars": d.get("stars"),
                          "stars_checked_at": d.get("stars_checked_at"), "tier": d["_tier"],
                          "score": d["_score"], "tags": d.get("tags", []), "path": d["_path"],
                          "summary": d.get("description")} for d in repos],
        "mcp_servers": [{"name": m.get("name"), "repository": m.get("repository"),
                         "official": m.get("official"), "security_risk": m.get("security_risk"),
                         "purpose": m.get("purpose"), "path": m["_path"]} for m in mcps],
        "agents": [{"name": a.get("name"), "role": a.get("role"), "path": a["_path"]} for a in agents],
        "workflows": [{"name": w.get("name"), "skills": w.get("skills", []), "path": w["_path"]} for w in wfs],
    }


def main() -> int:
    repos, skills, mcps = load_repos(), load_skills(), load_mcp()
    agents, wfs = load_agents(), load_workflows()
    idx = ROOT / "indexes"
    idx.mkdir(exist_ok=True)
    (idx / "repositories.md").write_text(gen_repositories(repos))
    (idx / "skills.md").write_text(gen_skills(skills))
    (idx / "mcp.md").write_text(gen_mcp(mcps))
    (idx / "agents.md").write_text(gen_agents(agents))
    (idx / "workflows.md").write_text(gen_workflows(wfs))
    (idx / "topics.md").write_text(gen_topics())
    (idx / "research.md").write_text(gen_research())
    (idx / "evaluations.md").write_text(gen_evaluations())
    mi = gen_machine_index(repos, skills, mcps, agents, wfs)
    (ROOT / "metadata" / "index.json").write_text(json.dumps(mi, indent=2, ensure_ascii=False) + "\n")
    print(f"Indexes regenerated: repositories({len(repos)}) skills({len(skills)}) "
          f"mcp({len(mcps)}) agents({len(agents)}) workflows({len(wfs)}) + metadata/index.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
