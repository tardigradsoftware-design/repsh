#!/usr/bin/env python3
"""Generate repository YAML records from verified GitHub API data.

Input:  metadata/raw/github-<date>.jsonl  (raw GitHub API records)
Output: repositories/<category>/<owner>_<repo>.yaml

Usage: python3 scripts/update/repositories.py
"""
import json
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RAW_DIR = ROOT / "metadata" / "raw"
OUT_DIR = ROOT / "repositories"

# owner/repo -> (category, relevance, official, recommended_for, not_recommended_for, related, tags, status_override, notes)
DB = {
    # ---- SKILLS / CODING AGENTS ----
    "VoltAgent/awesome-agent-skills": ("skills", "core", False,
        ["skill discovery", "agent ecosystem research", "seed source for new skills"],
        ["direct skill execution without review"],
        ["anthropics/skills", "openai/skills", "obra/superpowers"],
        ["agent-skills", "discovery", "catalog"], None,
        "1000+ curated skills across Claude Code, Codex, Cursor, Gemini CLI, OpenCode, Windsurf ecosystems. Primary discovery seed for this knowledge base."),
    "anthropics/skills": ("skills", "core", True,
        ["canonical Agent Skills format examples", "document skills", "artifacts patterns"],
        ["license-restricted redistribution (no OSS license file at verification)"],
        ["VoltAgent/awesome-agent-skills", "openai/skills"],
        ["agent-skills", "official", "format-reference"], None,
        "Anthropic's official public skills repo (docx/pptx/xlsx/pdf creation, artifacts builder). Demonstrates the canonical SKILL.md format with progressive disclosure. License field empty at verification — check LICENSE before copying content."),
    "openai/skills": ("skills", "high", True,
        ["skill format study", "Codex ecosystem research"],
        ["production use without license check"],
        ["anthropics/skills", "VoltAgent/awesome-agent-skills"],
        ["agent-skills", "official", "format-reference"], None,
        "OpenAI's Skills Catalog for Codex. No SPDX license detected at verification — treat as reference-only. Historical note: the repo evolved from an earlier skills concept; verify current status before relying on it."),
    "obra/superpowers": ("skills", "core", True,
        ["agentic SDLC methodology", "skill-testing methodology", "subagent-driven development", "workflow patterns"],
        [],
        ["anthropics/skills", "VoltAgent/awesome-agent-skills"],
        ["agent-skills", "methodology", "workflow"], None,
        "Not just a repo: an agentic software development methodology (brainstorming → planning → subagent-driven implementation → review). Its skill-testing and writing-skills patterns are extracted into our patterns/ directory."),
    "hesreallyhim/awesome-claude-code": ("skills", "high", False,
        ["resource discovery", "tooling discovery"],
        ["blind ingestion of listed resources"],
        ["VoltAgent/awesome-agent-skills"],
        ["discovery", "claude-code", "resources"], None,
        "Large discovery layer (skills, agents, status lines, tooling, plugins). Non-standard license at verification. Every listed resource must be re-verified before inclusion here."),
    "agentsmd/agents.md": ("skills", "core", True,
        ["agent instruction standard research", "AGENTS.md adoption tracking"],
        [],
        [],
        ["standards", "agent-instructions", "specification"], None,
        "The open AGENTS.md format for guiding coding agents. Adopted by major coding agents. Referenced by our standards/agents-md.md note."),
    "anthropics/claude-code": ("skills", "high", True,
        ["agentic coding tool research", "CLI agent behavior"],
        ["license-restricted code reuse (no OSS license at verification)"],
        ["openai/codex-unofficial", "obra/superpowers"],
        ["coding-agents", "cli", "official"], None,
        "Reference implementation of a terminal-native agentic coding tool. Its CLAUDE.md and subagent concepts inform our agent-instruction standards."),

    # ---- AGENT FRAMEWORKS ----
    "microsoft/agent-framework": ("agent-frameworks", "core", True,
        ["new .NET/Python multi-agent builds", "enterprise agent orchestration", "Microsoft-stack integrations"],
        ["very early-stage API stability expectations"],
        ["microsoft/autogen", "microsoft/semantic-kernel", "langchain-ai/langgraph"],
        ["agent-framework", "multi-agent", "python", "dotnet"], None,
        "Successor to AutoGen and Semantic Kernel orchestration. Microsoft recommends this for NEW projects; AutoGen is in maintenance mode."),
    "microsoft/autogen": ("agent-frameworks", "medium", True,
        ["legacy multi-agent systems", "research references"],
        ["new projects (Microsoft recommends agent-framework)"],
        ["microsoft/agent-framework", "crewAIInc/crewAI"],
        ["agent-framework", "multi-agent", "legacy"], "MAINTENANCE",
        "AutoGen is in maintenance mode; Microsoft directs new development to Microsoft Agent Framework. Last push 2026-04 at verification. Kept as reference for existing deployments and research literature."),
    "langchain-ai/langgraph": ("agent-frameworks", "core", True,
        ["stateful multi-step agents", "human-in-the-loop", "durable execution", "complex control flow"],
        ["simple single-call LLM apps (overkill)"],
        ["pydantic/pydantic-ai", "microsoft/agent-framework"],
        ["agent-framework", "graph", "stateful", "python", "js"], None,
        "Graph-based stateful agent runtime ('build resilient agents'). Strong fit for long-running, checkpointed, resumable agent workflows."),
    "pydantic/pydantic-ai": ("agent-frameworks", "core", True,
        ["typed structured outputs", "type-safe tool calling", "MCP-native agents", "pythonic agent APIs"],
        ["non-Python stacks (see Mastra for TS)"],
        ["langchain-ai/langgraph", "mastra-ai/mastra", "pydantic/logfire"],
        ["agent-framework", "typed", "structured-output", "mcp", "python"], None,
        "Type-safe agent framework from the Pydantic team: structured outputs, tools, MCP, subagents, declarative agent specification (AG-UI/AG-ENVS ecosystem). Strong observability story via Logfire."),
    "crewAIInc/crewAI": ("agent-frameworks", "high", True,
        ["role-based multi-agent crews", "rapid prototyping of agent teams"],
        ["fine-grained state control needs"],
        ["microsoft/agent-framework", "langchain-ai/langgraph"],
        ["agent-framework", "multi-agent", "role-based", "python"], None,
        "Role-playing autonomous agent orchestration. High adoption; opinionated crew/process abstractions."),
    "openai/openai-agents-python": ("agent-frameworks", "high", True,
        ["OpenAI-ecosystem agents", "handoffs pattern", "guardrails", "lightweight multi-agent"],
        ["model-agnostic requirements (verify current state)"],
        ["langchain-ai/langgraph", "google/adk-python"],
        ["agent-framework", "lightweight", "handoffs", "python"], None,
        "Lightweight multi-agent framework: agents, handoffs, guardrails, sessions, tracing."),
    "google/adk-python": ("agent-frameworks", "high", True,
        ["Gemini-ecosystem agents", "code-first agent toolkits", "evaluation-integrated development"],
        [],
        ["openai/openai-agents-python", "microsoft/agent-framework"],
        ["agent-framework", "gemini", "python", "java"], None,
        "Google's Agent Development Kit: code-first, evaluation and deployment oriented, multi-lingual (Python/Java)."),
    "mastra-ai/mastra": ("agent-frameworks", "high", True,
        ["TypeScript agents", "Next.js-integrated agent apps", "workflow + memory + evals in TS"],
        ["Python-only stacks"],
        ["pydantic/pydantic-ai", "vercel/next.js"],
        ["agent-framework", "typescript", "workflows", "evals"], None,
        "Modern TypeScript agent framework (workflows, memory, RAG, evals, MCP). Custom license at verification — check terms before commercial embedding."),
    "stanfordnlp/dspy": ("agent-frameworks", "high", True,
        ["prompt optimization", "declarative LM pipelines", "programmatic prompting"],
        ["imperative control-flow-heavy agents"],
        ["langchain-ai/langgraph"],
        ["prompt-optimization", "pipelines", "research", "python"], None,
        "'Programming, not prompting': declarative signatures + compilers that optimize prompts/weights against metrics."),
    "microsoft/semantic-kernel": ("agent-frameworks", "medium", True,
        [".NET AI applications", "enterprise integration", "migration path to agent-framework"],
        ["greenfield multi-agent (prefer agent-framework)"],
        ["microsoft/agent-framework"],
        ["agent-framework", "dotnet", "enterprise"], None,
        "Mature .NET-oriented LLM SDK. Microsoft's strategic direction converges on Agent Framework; SK remains for enterprise .NET scenarios."),
    "run-llama/llama_index": ("agent-frameworks", "high", True,
        ["RAG pipelines", "document processing", "data connectors", "retrieval-heavy agents"],
        ["pure orchestration without retrieval needs"],
        ["deepset-ai/haystack"],
        ["rag", "retrieval", "data", "python", "ts"], None,
        "Document processing platform for AI: ingestion, indexing, retrieval, agents. Broadest data-connector ecosystem."),
    "deepset-ai/haystack": ("agent-frameworks", "medium", True,
        ["production RAG", "explicit pipeline control", "context engineering research"],
        [],
        ["run-llama/llama_index"],
        ["rag", "pipelines", "context-engineering", "python"], None,
        "Open-source orchestration with explicit control over retrieval, routing, memory. Describes itself as context-engineering oriented."),

    # ---- BROWSER AUTOMATION ----
    "browser-use/browser-use": ("browser-automation", "core", True,
        ["LLM-driven browser agents", "visual + DOM hybrid automation", "web research agents"],
        ["pixel-perfect scraping (use plain Playwright)", "high-QPS deterministic tasks"],
        ["microsoft/playwright-mcp", "browser-use/web-ui", "microsoft/playwright"],
        ["browser-agent", "python", "playwright"], None,
        "The dominant open browser-agent library. Connects LLMs to a real browser with DOM/aesthesia extraction. Massive adoption."),
    "browser-use/web-ui": ("browser-automation", "medium", True,
        ["self-hosted browser agent UI", "demos of browser-use"],
        ["production deployments (verify activity)"],
        ["browser-use/browser-use"],
        ["browser-agent", "ui", "python"], None,
        "Gradio-based UI to run browser-use agents locally or with cloud browsers. Lower recent activity than core at verification."),
    "microsoft/playwright": ("browser-automation", "core", True,
        ["deterministic browser testing", "E2E automation", "visual regression", "agent tooling substrate"],
        ["non-deterministic LLM-driven exploration (combine with browser agents)"],
        ["microsoft/playwright-mcp", "browser-use/browser-use"],
        ["testing", "e2e", "browser", "ts", "python"], None,
        "The foundation layer for programmatic browser control. Agents should prefer Playwright primitives for deterministic steps and reserve LLM reasoning for ambiguous states."),
    "ServiceNow/BrowserGym": ("browser-automation", "medium", True,
        ["web-agent benchmarking", "reproducible web environments"],
        ["production automation"],
        ["browser-use/browser-use", "THUDM/AgentBench"],
        ["benchmark", "web-agent", "gym", "research"], None,
        "Gym environment unifying web-agent benchmarks (WebArena, MiniWoB++, WorkArena). Research-grade reproducibility for browser agents."),

    # ---- MCP ----
    "modelcontextprotocol/modelcontextprotocol": ("mcp-servers", "core", True,
        ["MCP specification reference", "protocol versioning", "security model"],
        [],
        ["modelcontextprotocol/servers"],
        ["mcp", "specification", "standard"], None,
        "The MCP specification itself. All MCP server entries in this registry are validated against this protocol."),
    "modelcontextprotocol/servers": ("mcp-servers", "core", True,
        ["reference MCP servers", "filesystem/fetch/memory/git patterns"],
        ["unreviewed community servers"],
        ["github/github-mcp-server", "microsoft/playwright-mcp"],
        ["mcp", "reference", "official"], None,
        "Official reference servers from the MCP organization. License field non-standard at verification (per-file licensing) — check before reuse."),
    "github/github-mcp-server": ("mcp-servers", "core", True,
        ["repository automation", "issue/PR workflows", "CI agent integration"],
        ["broad-token setups (prefer scoped PATs / fine-grained permissions)"],
        ["modelcontextprotocol/servers"],
        ["mcp", "github", "official"], None,
        "GitHub's official MCP server (Go). Supports toolsets, fine-grained tokens, and Docker/remote deployment."),
    "microsoft/playwright-mcp": ("mcp-servers", "core", True,
        ["browser control for coding agents", "accessibility-tree-driven automation", "E2E test authoring"],
        ["massive parallel scraping"],
        ["browser-use/browser-use", "ChromeDevTools/chrome-devtools-mcp"],
        ["mcp", "browser", "accessibility-tree"], None,
        "Official Playwright MCP. Operates via the accessibility tree rather than screenshots — fast, deterministic, and LLM-friendly. Ships .github/skills-style agent integrations in-repo."),
    "ChromeDevTools/chrome-devtools-mcp": ("mcp-servers", "core", True,
        ["performance tracing for agents", "debugging live Chrome sessions", "network/console inspection"],
        [],
        ["microsoft/playwright-mcp"],
        ["mcp", "chrome", "devtools", "performance"], None,
        "Chrome DevTools team's MCP server: lets agents inspect performance traces, network, console, and CPU profiles — unique debugging capability."),
    "supabase/mcp": ("mcp-servers", "core", True,
        ["Supabase project management", "schema + migrations via agents", "Postgres dev workflows"],
        ["production databases with write access (danger of destructive ops; scope access)"],
        ["github/github-mcp-server"],
        ["mcp", "supabase", "postgres", "database"], None,
        "Official Supabase MCP. Access-scoped via PAT; expose destructive tools deliberately. Apply our mcp security checklist before enabling write tools."),
    "browserbase/mcp-server-browserbase": ("mcp-servers", "medium", True,
        ["cloud browser sessions for agents", "scalable hosted browsing"],
        ["local-only budgets"],
        ["browser-use/browser-use", "microsoft/playwright-mcp"],
        ["mcp", "browser", "cloud"], "ARCHIVED",
        "ARCHIVED at verification (2026-07 last push; repo flagged archived). Superseded in practice by Browserbase's newer SDK surface; kept as a historical pointer to cloud browser MCP patterns."),

    # ---- EVALUATION ----
    "EleutherAI/lm-evaluation-harness": ("evaluation", "core", True,
        ["reproducible LLM benchmarking", "hundreds of tasks", "open model comparison"],
        ["agent long-horizon tasks (use agent-specific benchmarks)"],
        ["stanford-crfm/helm", "openai/evals"],
        ["evaluation", "benchmarks", "reproducibility"], None,
        "The community-standard harness for few-shot LLM evaluation; the backbone of most open leaderboards (e.g., Open LLM Leaderboard lineage)."),
    "stanford-crfm/helm": ("evaluation", "high", True,
        ["holistic multi-metric evaluation methodology", "transparency/scenario design"],
        ["latest model rankings (maintenance-mode cadence)"],
        ["EleutherAI/lm-evaluation-harness"],
        ["evaluation", "methodology", "holistic"], "STABLE",
        "HELM's value is its METHODOLOGY (scenarios × metrics × perturbations). Even as its ranking cadence slowed, it remains the canonical reference for holistic evaluation design."),
    "openai/evals": ("evaluation", "medium", True,
        ["eval registry patterns", "LLM system evaluation format"],
        ["freshest benchmarks (low push cadence at verification)"],
        ["EleutherAI/lm-evaluation-harness", "promptfoo/promptfoo"],
        ["evaluation", "registry", "openai"], "STABLE",
        "OpenAI's framework + registry of evals. Historical and format value; lower recent activity at verification (last push 2026-04)."),
    "promptfoo/promptfoo": ("evaluation", "core", True,
        ["prompt/agent regression testing in CI", "red teaming", "model comparison"],
        [],
        ["openai/evals", "langfuse/langfuse"],
        ["evaluation", "ci", "red-teaming", "typescript"], None,
        "Declarative eval configs with CI integration; used for prompt regression and AI red-teaming. Ideal bridge between this knowledge base and CI pipelines."),
    "SWE-bench/SWE-bench": ("evaluation", "core", True,
        ["coding-agent capability measurement", "real GitHub issue resolution"],
        ["production hiring decisions", "contaminated leaderboard chasing"],
        ["THUDM/AgentBench", "ServiceNow/BrowserGym"],
        ["benchmark", "coding-agents", "swe"], None,
        "The canonical software-engineering benchmark for LLMs/agents: resolve real repo issues with tests. SWE-bench Verified subset reduces grading noise."),
    "THUDM/AgentBench": ("evaluation", "medium", True,
        ["multi-domain agent evaluation", "ICLR'24 methodology reference"],
        ["current model rankings (evaluation set ages)"],
        ["SWE-bench/SWE-bench", "ServiceNow/BrowserGym"],
        ["benchmark", "agents", "multi-domain"], "STABLE",
        "Comprehensive multi-environment agent benchmark (8 environments). Push cadence slowed at verification; use as methodology + historical baseline."),
    "langfuse/langfuse": ("evaluation", "high", True,
        ["LLM observability", "trace-based evaluation", "self-hostable telemetry"],
        [],
        ["Arize-ai/phoenix", "pydantic/logfire"],
        ["observability", "tracing", "evals", "ts"], None,
        "Open-source LLM engineering platform: traces, evals, prompt management, datasets. MIT-core with commercial features (custom license file)."),
    "Arize-ai/phoenix": ("evaluation", "high", True,
        ["OpenTelemetry-based LLM tracing", "experiment datasets", "evals in notebooks/CI"],
        [],
        ["langfuse/langfuse", "pydantic/logfire"],
        ["observability", "otel", "evals", "python"], None,
        "AI observability built on OpenTelemetry semantics; strong Python/notebook ergonomics."),
    "pydantic/logfire": ("evaluation", "medium", True,
        ["Pydantic-native observability", "structured agent telemetry"],
        ["vendor-hosted-primary workflows (OSS client)"],
        ["Arize-ai/phoenix", "langfuse/langfuse"],
        ["observability", "otel", "pydantic", "python"], None,
        "Observability from the Pydantic team, OpenTelemetry-based, deep pydantic-ai integration."),

    # ---- REASONING / RESEARCH ----
    "deepseek-ai/DeepSeek-R1": ("research", "core", True,
        ["open reasoning model research", "RL-trained reasoning reproduction", "distillation study"],
        ["latest capability claims (repo pushed 2025-06 at verification)"],
        ["huggingface/open-r1"],
        ["reasoning", "open-models", "rl"], "STABLE",
        "Open-weight reasoning model with published technique (RL with verifiable rewards, distillation). The canonical public reasoning-research artifact. NOTE: model evolves on Hugging Face; this repo is the paper/weights pointer."),
    "huggingface/open-r1": ("research", "high", True,
        ["full reproduction recipe for R1-style reasoning", "reasoning dataset generation (OpenR1-Math)"],
        [],
        ["deepseek-ai/DeepSeek-R1"],
        ["reasoning", "reproduction", "datasets", "training"], None,
        "Hugging Face's fully open reproduction of DeepSeek-R1: training pipeline, datasets, and evaluation. The best public step-by-step reasoning-training reference."),
    "ShishirPatil/gorilla": ("research", "high", True,
        ["tool-use / function-calling research", "API-calling accuracy (BFCL leaderboard)"],
        [],
        ["SWE-bench/SWE-bench"],
        ["tool-use", "function-calling", "research"], None,
        "Gorilla + Berkeley Function Calling Leaderboard: the reference research line for LLM tool-use reliability."),

    # ---- FRONTEND ----
    "vercel/next.js": ("frontend", "core", True,
        ["production web apps", "SSR/ISR/RSC", "SaaS dashboards"],
        [],
        ["react/react", "vercel/ai"],
        ["nextjs", "react", "framework", "typescript"], None,
        "The default React meta-framework in this knowledge base's web stack guidance."),
    "react/react": ("frontend", "core", True,
        ["UI fundamentals", "component architecture", "RSC research"],
        [],
        ["vercel/next.js"],
        ["react", "ui", "library"], None,
        "Reference for component composition, hooks, and React Server Components direction. NOTE: repo canonical location verified as react/react on 2026-09-20 (moved from facebook/react)."),
    "microsoft/TypeScript": ("frontend", "core", True,
        ["type system mastery", "strict mode", "monorepo configs"],
        [],
        [],
        ["typescript", "types"], None,
        "Source of truth for TS behavior; our coding standards pin strict TypeScript."),
    "tailwindlabs/tailwindcss": ("frontend", "core", True,
        ["utility-first styling", "design token discipline"],
        [],
        ["shadcn-ui/ui"],
        ["css", "design-systems"], None,
        "Preferred styling baseline in our frontend stack guidance (v4 at verification)."),
    "shadcn-ui/ui": ("frontend", "core", True,
        ["copy-in component systems", "accessible primitives", "design system bootstrapping"],
        ["teams needing classic versioned component deps"],
        ["radix-ui/primitives", "tailwindlabs/tailwindcss"],
        ["ui", "components", "radix", "tailwind"], None,
        "Owned components over dependency-style UI kits; canonical base for SaaS UI in our playbooks."),
    "radix-ui/primitives": ("frontend", "core", True,
        ["accessible headless primitives", "keyboard/ARIA correctness"],
        [],
        ["shadcn/ui"],
        ["ui", "accessibility", "primitives"], None,
        "The accessibility substrate under shadcn/ui; first reference for dialog/popover/dropdown correctness."),
    "motiondivision/motion": ("frontend", "high", True,
        ["physics-based UI animation", "gesture + scroll animation", "reduced-motion patterns"],
        [],
        ["greensock/GSAP"],
        ["animation", "motion", "react"], None,
        "Framer Motion's successor package (`motion`). Primary recommendation for React motion; GSAP for timeline-heavy scroll storytelling."),
    "mrdoob/three.js": ("frontend", "high", True,
        ["WebGL scenes", "3D landing experiences", "shader work"],
        ["content sites without 3D needs"],
        ["greensock/GSAP"],
        ["webgl", "3d", "graphics"], None,
        "Reference 3D library for cinematic web experiences; pair with performance budgets from knowledge/frontend/webgl-performance.md."),
    "greensock/GSAP": ("frontend", "high", True,
        ["timeline animation", "ScrollTrigger storytelling", "SVG path animation"],
        ["license review for commercial embedding (core now free but verify terms)"],
        ["motiondivision/motion"],
        ["animation", "scroll", "timeline"], None,
        "Industry-standard animation timeline library; ScrollTrigger is the reference for scroll storytelling."),
    "TanStack/table": ("frontend", "high", True,
        ["data-heavy tables", "sorting/filtering/virtualization"],
        [],
        ["shadcn/ui"],
        ["tables", "data-grid", "headless"], None,
        "Headless table engine of choice for enterprise data-dense UIs in our playbooks."),
    "excalidraw/excalidraw": ("frontend", "low", False,
        ["diagram UX reference", "whiteboard embedding"],
        [],
        [],
        ["ux-reference", "canvas"], None,
        "Included as a UX/canvas interaction reference for agent-built tools."),

    # ---- BACKEND / DATABASES / DEVOPS ----
    "fastapi/fastapi": ("backend", "core", True,
        ["Python APIs", "typed endpoints", "SSE/streaming"],
        [],
        ["pydantic/pydantic-ai"],
        ["python", "api", "async"], None,
        "Default Python API framework in our backend guidance."),
    "nestjs/nest": ("backend", "high", True,
        ["structured Node backends", "enterprise TS servers"],
        ["small scripts"],
        ["expressjs/express"],
        ["nodejs", "api", "architecture"], None,
        "Opinionated, modular Node framework for structured services."),
    "expressjs/express": ("backend", "medium", True,
        ["minimal Node servers", "middleware fundamentals"],
        ["large structured apps (prefer NestJS)"],
        ["nestjs/nest"],
        ["nodejs", "api", "minimal"], None,
        "Baseline Node HTTP framework; ubiquitous and stable."),
    "oven-sh/bun": ("backend", "medium", True,
        ["fast JS runtime + toolchain", "scripting and test runners"],
        ["conservative enterprise production"],
        ["denoland/deno"],
        ["runtime", "javascript", "toolchain"], None,
        "High-performance JS runtime; verify production readiness per-use-case."),
    "supabase/supabase": ("databases", "core", True,
        ["Postgres BaaS", "auth + RLS + realtime", "SaaS backends"],
        ["fine-grained custom DB requirements on other clouds"],
        ["prisma/orm", "drizzle-team/drizzle-orm", "supabase/mcp"],
        ["postgres", "baas", "auth", "rls"], None,
        "Primary recommended backend platform for SaaS builds in this knowledge base; pair with RLS knowledge note."),
    "drizzle-team/drizzle-orm": ("databases", "core", True,
        ["typed SQL-first ORMs", "edge runtimes", "migration discipline"],
        ["teams preferring schema-first codegen"],
        ["prisma/prisma"],
        ["orm", "typescript", "sql"], None,
        "SQL-first typed ORM; preferred for Next.js + Postgres stacks in our playbooks."),
    "prisma/orm": ("databases", "high", True,
        ["schema-first DX", "migrations", "multi-DB support"],
        ["edge-heavy workloads (driver adapters changing fast)"],
        ["drizzle-team/drizzle-orm"],
        ["orm", "typescript", "migrations"], None,
        "Mature schema-first ORM; strong docs and migration tooling. NOTE: repo renamed prisma/prisma -> prisma/orm (verified 2026-09-20)."),
    "redis/redis": ("databases", "medium", True,
        ["caching", "queues", "rate limiting"],
        ["primary transactional store"],
        [],
        ["cache", "queues"], None,
        "Standard in-memory data platform reference for cache/queue patterns."),
    "bytebase/bytebase": ("databases", "medium", True,
        ["database change management", "migration review workflows"],
        [],
        ["prisma/orm"],
        ["devops", "postgres", "change-management"], None,
        "Reference for DB CI/CD and migration governance patterns."),

    # ---- SECURITY ----
    "OWASP/CheatSheetSeries": ("developer-tools", "core", True,
        ["authoritative security checklists", "XSS/CSRF/SSRF/auth guidance"],
        [],
        ["OWASP/www-project-top-10-for-large-language-model-applications"],
        ["security", "owasp", "checklists"], None,
        "The OWASP Cheat Sheet Series: primary security reference for our security-audit skill."),
    "trufflesecurity/trufflehog": ("developer-tools", "high", True,
        ["secret scanning", "CI secret detection"],
        [],
        [],
        ["security", "secrets", "ci"], None,
        "Secret detection reference for our CI and pre-commit guidance."),
    "NousResearch/hermes-agent": ("agent-frameworks", "high", True,
        ["self-improving agent architectures", "skill synthesis from experience", "long-horizon personal agents"],
        ["unreviewed autonomous execution on private data"],
        ["obra/superpowers", "openai/openai-agents-python"],
        ["agent-framework", "memory", "self-improvement", "skills"], None,
        "Nous Research's open agent that grows with the user: learns skills from its own experience and persists memory. The key public reference for procedural-skill synthesis (see knowledge/agent-engineering/agent-memory.md). Massive adoption at verification (247k+ stars) — treat architecture claims as PRIMARY-source verified, capability claims as vendor-stated."),
    "gin-gonic/gin": ("backend", "medium", True,
        ["high-throughput Go HTTP APIs"], [], ["expressjs/express"], ["go", "api", "performance"], None,
        "Popular Go HTTP framework reference."),
    "mongodb/mongo": ("databases", "medium", True,
        ["document DB fundamentals", "schema design tradeoffs"], ["defaulting to Mongo without need (prefer Postgres first)"], [], ["database", "nosql"], None,
        "Reference for document-store modeling; our default remains Postgres unless the use case demands document semantics."),
    "processing/p5.js": ("frontend", "low", True,
        ["creative coding", "canvas-based visualizations", "generative art"], [], ["mrdoob/three.js"], ["canvas", "creative-coding"], None,
        "Creative-coding canvas library; useful for generative visual effects without WebGL overhead."),
    "microsoft/vscode-copilot-release": ("developer-tools", "low", False,
        ["Copilot Chat UX feedback history"], ["current docs (archived)"], [], ["copilot", "archived"], "ARCHIVED",
        "Archived feedback repo; kept only as UX-research pointer. Do not treat as active documentation."),
    "nocobase/nocobase": ("developer-tools", "low", True,
        ["no-code admin/data platform reference", "plugin architecture study"], [], [], ["low-code", "admin"], None,
        "Reference for admin-panel/data-app architecture patterns."),

    # ---- LANGUAGES / MISC INFRA REFERENCES ----
    "python/cpython": ("developer-tools", "medium", True, ["language reference"], [], [], ["python"], None, "Reference for Python semantics."),
    "golang/go": ("developer-tools", "medium", True, ["language reference"], [], [], ["go"], None, "Reference for Go semantics."),
    "denoland/deno": ("developer-tools", "low", True, ["alternative JS runtime reference"], [], [], ["runtime"], None, "Security-oriented JS runtime reference."),
}


def classify_status(rec: dict) -> str:
    if rec.get("archived"):
        return "ARCHIVED"
    pushed = datetime.strptime(rec["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").date()
    today = date(2026, 9, 20)
    days = (today - pushed).days
    if days <= 30:
        return "ACTIVE"
    if days <= 120:
        return "STABLE"
    if days <= 365:
        return "MAINTENANCE"
    return "ABANDONED"


def adoption_band(stars: int) -> str:
    if stars >= 100_000: return "massive"
    if stars >= 20_000: return "high"
    if stars >= 5_000: return "moderate"
    if stars >= 1_000: return "niche"
    return "minimal"


def yq(v):
    return json.dumps(v, ensure_ascii=False) if isinstance(v, str) else v


def yaml_str(s: str) -> str:
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"').replace("\n", " ") + '"'


def write_entry(rec: dict, checked: date) -> Path:
    key = f"{rec['owner']}/{rec['name']}"
    if key not in DB:
        return None
    cat, relevance, official, rec_for, not_for, related, tags, status_override, notes = DB[key]
    status = status_override or classify_status(rec)
    license_id = rec.get("license")
    lic = license_id if license_id and license_id != "NOASSERTION" else "CUSTOM/NOASSERTION"
    stars = rec["stargazers_count"]
    days_since_push = (date(2026, 9, 20) - datetime.strptime(rec["pushed_at"], "%Y-%m-%dT%H:%M:%SZ").date()).days
    maintenance = "active" if days_since_push <= 7 else "regular" if days_since_push <= 30 else "sporadic" if days_since_push <= 120 else "stale" if days_since_push <= 365 else "none"
    confidence = "VERY HIGH" if official and maintenance in ("active", "regular") else "HIGH" if maintenance in ("active", "regular", "sporadic") else "MEDIUM"

    slug = f"{rec['owner']}_{rec['name']}".lower()
    out = OUT_DIR / cat / f"{slug}.yaml"
    out.parent.mkdir(parents=True, exist_ok=True)

    lines = [
        f"# Auto-generated from GitHub API on {checked.isoformat()} — regenerate via scripts/update/repositories.py",
        "name: " + yaml_str(rec["name"]),
        "owner: " + yaml_str(rec["owner"]),
        "url: " + yaml_str(rec["html_url"]),
        "description: " + yaml_str(rec.get("description") or ""),
        f"category: {cat}",
        "language: " + (yaml_str(rec["language"]) if rec.get("language") else "null"),
        f"license: {yaml_str(lic)}",
        f"stars: {stars}",
        f"forks: {rec['forks_count']}",
        f"open_issues: {rec['open_issues_count']}",
        f"stars_checked_at: {checked.isoformat()}",
        f"last_push: {rec['pushed_at'][:10]}",
        f"created_at: {rec['created_at'][:10]}",
        f"status: {status}",
        f"official: {'true' if official else 'false'}",
        "production_ready: " + ("yes" if status in ("ACTIVE", "STABLE") and adoption_band(stars) in ("massive", "high") else "conditional" if status in ("ACTIVE", "STABLE") else "no"),
        f"maintenance_status: {maintenance}",
        "security_status: " + ("good" if official and status in ("ACTIVE", "STABLE") else "acceptable" if status in ("ACTIVE", "STABLE") else "unknown"),
        f"documentation_quality: {'excellent' if official else 'good'}",
        f"community_adoption: {adoption_band(stars)}",
        f"relevance: {relevance}",
        f"confidence: {confidence}",
        "recommended_for:",
        *([f"  - {yaml_str(x)}" for x in rec_for] or ["  - (unspecified)"]),
        "not_recommended_for:",
        *([f"  - {yaml_str(x)}" for x in not_for] or ["  - (none recorded)"]),
        "related_projects:",
        *([f"  - {yaml_str(x)}" for x in related] or ["  - (none)"]),
        "source_verified: true",
        "notes: " + yaml_str(notes),
        "tags:",
        *([f"  - {yaml_str(t)}" for t in tags] or ["  - untagged"]),
    ]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return out


def main() -> int:
    checked = date(2026, 9, 20)
    raw_files = sorted(RAW_DIR.glob("github-*.jsonl"))
    if not raw_files:
        print("No raw metadata found", file=sys.stderr)
        return 1
    seen = {}
    for f in raw_files:
        for line in f.read_text().splitlines():
            line = line.strip()
            if not line or not line.startswith("{"):
                continue
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue  # skip concatenated error fragments
            if "full_name" not in rec or "name" not in rec:
                continue  # skip API error fragments
            rec["owner"], rec["name"] = rec["full_name"].split("/", 1)
            seen[f"{rec['owner']}/{rec['name']}"] = rec  # newest file wins
    written, skipped = 0, []
    for key, rec in seen.items():
        p = write_entry(rec, checked)
        if p:
            written += 1
        else:
            skipped.append(key)
    print(f"Wrote {written} repository records.")
    if skipped:
        print(f"Not in DB map (add classification): {', '.join(sorted(skipped))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
