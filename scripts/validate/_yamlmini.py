#!/usr/bin/env python3
"""Minimal YAML subset parser (stdlib-only).

Supports the record shapes used in this repository:
- flat `key: value` scalars (quoted or plain)
- block lists (`key:` + `  - item`)
- one-level nested block maps (`key:` + indented `k: v`)
- flow lists `[a, b]` and flow maps `{a: 1, b: 2}`
- comments starting with `#`
Not a general YAML implementation — intentional (see AGENTS.md: stdlib-only).
"""
from __future__ import annotations


def _scalar(s: str):
    s = s.strip()
    if s == "" or s == "~" or s == "null":
        return None
    if s == "true":
        return True
    if s == "false":
        return False
    if len(s) >= 2 and s[0] == s[-1] and s[0] in ('"', "'"):
        return s[1:-1]
    try:
        return int(s)
    except ValueError:
        pass
    try:
        return float(s)
    except ValueError:
        pass
    return s


def _flow(s: str):
    """Parse flow collections [..] / {..} (no nested flow inside flow)."""
    s = s.strip()
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        if not inner:
            return []
        parts, buf, q = [], "", None
        for ch in inner:
            if q:
                buf += ch
                if ch == q:
                    q = None
            elif ch in ('"', "'"):
                q = ch
                buf += ch
            elif ch == ",":
                parts.append(buf)
                buf = ""
            else:
                buf += ch
        if buf.strip():
            parts.append(buf)
        return [_scalar(p) for p in parts]
    if s.startswith("{") and s.endswith("}"):
        inner = s[1:-1].strip()
        out = {}
        if not inner:
            return out
        parts, buf, q = [], "", None
        for ch in inner:
            if q:
                buf += ch
                if ch == q:
                    q = None
            elif ch in ('"', "'"):
                q = ch
                buf += ch
            elif ch == ",":
                parts.append(buf)
                buf = ""
            else:
                buf += ch
        if buf.strip():
            parts.append(buf)
        for p in parts:
            if ":" in p:
                k, v = p.split(":", 1)
                out[_scalar(k)] = _scalar(v)
        return out
    return _scalar(s)


def parse(text: str) -> dict:
    """Parse a YAML document into a dict (subset grammar)."""
    root: dict = {}
    stack = [(-1, root)]  # (indent, container)
    lines = text.splitlines()
    i, n = 0, len(lines)
    while i < n:
        raw = lines[i]
        i += 1
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.lstrip().startswith("---") or raw.lstrip().startswith("..."):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        line = raw.strip()
        if ":" not in line:
            continue
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()

        while stack and indent < stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]

        if rest == "":
            # look ahead: list items or nested map
            if i < n:
                nxt = lines[i]
                nxt_indent = len(nxt) - len(nxt.lstrip(" "))
                nxt_stripped = nxt.strip()
                if nxt_indent > indent and nxt_stripped.startswith("- "):
                    lst = []
                    while i < n:
                        l2 = lines[i]
                        ind2 = len(l2) - len(l2.lstrip(" "))
                        s2 = l2.strip()
                        if not s2 or s2.startswith("#"):
                            i += 1
                            continue
                        if ind2 == nxt_indent and s2.startswith("- "):
                            lst.append(_scalar(s2[2:]))
                            i += 1
                        else:
                            break
                    parent[key] = lst
                    continue
                if nxt_indent > indent:
                    sub = {}
                    parent[key] = sub
                    stack.append((nxt_indent, sub))
                    continue
            parent[key] = None
            continue

        # scalar or flow on same line
        parent[key] = _flow(rest) if rest[:1] in "[{" else _scalar(rest)
    return root


def parse_frontmatter(text: str):
    """Extract frontmatter dict + body from a markdown file. Returns (dict|None, body)."""
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm = parse(text[3:end])
    body = text[end + 4:]
    return fm, body
