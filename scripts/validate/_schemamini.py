#!/usr/bin/env python3
"""Minimal JSON Schema validator (stdlib-only).

Supports the subset used by schemas/*.schema.json:
type (object/string/integer/number/boolean/array/null + union lists),
required, properties, enum, pattern, format:date, minimum, maximum, items.
"""
from __future__ import annotations

import json
import re
from datetime import date


def _check_type(value, typ) -> bool:
    types = typ if isinstance(typ, list) else [typ]
    for t in types:
        if t == "object" and isinstance(value, dict):
            return True
        if t == "string" and isinstance(value, str):
            return True
        if t == "integer" and isinstance(value, int) and not isinstance(value, bool):
            return True
        if t == "number" and isinstance(value, (int, float)) and not isinstance(value, bool):
            return True
        if t == "boolean" and isinstance(value, bool):
            return True
        if t == "array" and isinstance(value, list):
            return True
        if t == "null" and value is None:
            return True
    return False


def validate(instance, schema: dict, path="$") -> list[str]:
    errors: list[str] = []

    def err(msg):
        errors.append(f"{path}: {msg}")

    if "type" in schema and not _check_type(instance, schema["type"]):
        err(f"expected type {schema['type']}, got {type(instance).__name__}")
        return errors

    if isinstance(instance, dict):
        for req in schema.get("required", []):
            if req not in instance:
                err(f"missing required property '{req}'")
        for prop, sub in schema.get("properties", {}).items():
            if prop in instance:
                errors.extend(validate(instance[prop], sub, f"{path}.{prop}"))
        return errors

    if isinstance(instance, list):
        if "items" in schema:
            for idx, item in enumerate(instance):
                errors.extend(validate(item, schema["items"], f"{path}[{idx}]"))
        return errors

    if isinstance(instance, str):
        if "enum" in schema and instance not in schema["enum"]:
            err(f"'{instance}' not in enum {schema['enum']}")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            err(f"'{instance}' does not match pattern {schema['pattern']}")
        if schema.get("format") == "date":
            try:
                date.fromisoformat(instance)
            except ValueError:
                err(f"'{instance}' is not a valid ISO date")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            err(f"length {len(instance)} exceeds maxLength {schema['maxLength']}")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            err(f"{instance} < minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            err(f"{instance} > maximum {schema['maximum']}")

    return errors


def load_schema(path) -> dict:
    with open(path) as f:
        return json.load(f)
