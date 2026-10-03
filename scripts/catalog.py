#!/usr/bin/env python3
"""Validate and render the catalog defined in data/tools.yaml.

Subcommands:
  validate        Check structure, unique group/tool ids, required fields,
                  and repository URL prefix.
  readme --check  Fail if the generated README catalog block is stale.
  readme --write  Rewrite the generated README catalog block in place.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
TOOLS_FILE = REPO_ROOT / "data" / "tools.yaml"
README_FILE = REPO_ROOT / "README.md"

START_MARKER = "<!-- catalog:start -->"
END_MARKER = "<!-- catalog:end -->"
REQUIRED_TOOL_FIELDS = ("name", "id", "description", "command", "repo")
REPO_PREFIX = "https://github.com/Midtown-Technology-Group/"
ID_PATTERN = re.compile(r"[a-z0-9.-]+")


def die(message: str) -> None:
    """Print an error to stderr and exit non-zero."""
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def load_catalog() -> dict:
    """Load data/tools.yaml and confirm it has a top-level groups list."""
    try:
        data = yaml.safe_load(TOOLS_FILE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        die(f"missing catalog file: {TOOLS_FILE}")
    except yaml.YAMLError as exc:
        die(f"invalid YAML in {TOOLS_FILE}: {exc}")
    if not isinstance(data, dict) or not isinstance(data.get("groups"), list):
        die("catalog must have a top-level 'groups' list")
    return data


def validate() -> None:
    """Validate catalog fields and uniqueness, then print a summary."""
    data = load_catalog()
    group_ids: set[str] = set()
    tool_ids: set[str] = set()
    for group in data["groups"]:
        for field in ("name", "id", "summary", "tools"):
            if not group.get(field):
                die(f"group {group.get('name')!r} is missing '{field}'")
        group_id = group["id"]
        if group_id in group_ids:
            die(f"duplicate group id: {group_id}")
        group_ids.add(group_id)
        for tool in group["tools"]:
            name = tool.get("name", "<unnamed>")
            for field in REQUIRED_TOOL_FIELDS:
                if not tool.get(field):
                    die(f"tool {name!r} is missing '{field}'")
            if not isinstance(tool.get("tags"), list) or not tool["tags"]:
                die(f"tool {name!r} must have a non-empty 'tags' list")
            tool_id = tool["id"]
            if not ID_PATTERN.fullmatch(tool_id):
                die(f"tool {name!r} has invalid id {tool_id!r}; expected [a-z0-9.-]+")
            if tool_id in tool_ids:
                die(f"duplicate tool id: {tool_id}")
            tool_ids.add(tool_id)
            if not tool["repo"].startswith(REPO_PREFIX):
                die(f"tool {name!r} repo must start with {REPO_PREFIX}")
    print(f"catalog ok: {len(tool_ids)} tools in {len(group_ids)} groups")


def cell(value: object) -> str:
    """Collapse whitespace and escape pipes so a value cannot break the table."""
    return " ".join(str(value).split()).replace("|", "\\|")


def render_readme_block() -> str:
    """Render the catalog table placed between the README markers."""
    data = load_catalog()
    lines = ["| Tool | Group | Description |", "| --- | --- | --- |"]
    for group in data["groups"]:
        for tool in group["tools"]:
            lines.append(f"| {cell(tool['name'])} | {cell(group['name'])} | {cell(tool['description'])} |")
    return "\n".join(lines)


def readme(mode: str) -> None:
    """Regenerate the README catalog block, or fail when it is stale."""
    raw = README_FILE.read_bytes()
    crlf = b"\r\n" in raw
    text = raw.decode("utf-8").replace("\r\n", "\n")
    if START_MARKER not in text or END_MARKER not in text:
        die(f"README.md must contain {START_MARKER} and {END_MARKER}")
    before, rest = text.split(START_MARKER, 1)
    _, after = rest.split(END_MARKER, 1)
    updated = f"{before}{START_MARKER}\n{render_readme_block()}\n{END_MARKER}{after}"
    if mode == "write":
        payload = updated.replace("\n", "\r\n") if crlf else updated
        README_FILE.write_bytes(payload.encode("utf-8"))
        print("README.md catalog block regenerated")
        return
    if updated != text:
        die("README.md catalog block is stale; run 'python scripts/catalog.py readme --write'")
    print("README.md catalog block is current")


def main() -> None:
    """Parse arguments and dispatch to a subcommand."""
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate", help="validate data/tools.yaml")
    readme_parser = sub.add_parser("readme", help="render or check the README catalog table")
    group = readme_parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--check", action="store_true", help="fail when the table is stale")
    group.add_argument("--write", action="store_true", help="rewrite the table in place")
    args = parser.parse_args()

    if args.command == "validate":
        validate()
    elif args.command == "readme":
        readme("write" if args.write else "check")


if __name__ == "__main__":
    main()
