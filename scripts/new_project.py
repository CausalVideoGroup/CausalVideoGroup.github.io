#!/usr/bin/env python3
"""Create a public project page from the repository templates."""

from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

try:
    from .new_discussion import load_leaders, validate_slug, yaml_double_quoted
except ImportError:  # Direct execution
    from new_discussion import load_leaders, validate_slug, yaml_double_quoted


def render(source: str, values: dict[str, str], html_mode: bool = False) -> str:
    replacements = (
        {key: html.escape(value, quote=True) for key, value in values.items()}
        if html_mode
        else values | {"{{TITLE}}": yaml_double_quoted(values["{{TITLE}}"])}
    )
    for token, value in replacements.items():
        source = source.replace(token, value)
    if "{{" in source:
        raise ValueError("template contains unresolved placeholders")
    return source


def create_project(
    root: Path,
    slug: str,
    title: str,
    leader_short_name: str,
    force: bool = False,
) -> Path:
    slug = validate_slug(slug, "project slug")
    leader_short_name = validate_slug(leader_short_name, "leader")
    title = title.strip()
    if not title:
        raise ValueError("title must not be empty")
    leaders = load_leaders(root / "data" / "people.yaml")
    if leader_short_name not in leaders:
        raise ValueError(
            f"unknown leader {leader_short_name!r}; choose one of: {', '.join(sorted(leaders))}"
        )
    leader = leaders[leader_short_name]
    destination = root / "projects" / slug
    if destination.exists() and not force:
        raise FileExistsError(f"project already exists: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "assets").mkdir(exist_ok=True)
    (destination / "assets" / ".gitkeep").touch(exist_ok=True)
    values = {
        "{{TITLE}}": title,
        "{{PROJECT_SLUG}}": slug,
        "{{LEADER_NAME}}": leader.name,
        "{{LEADER_SHORT_NAME}}": leader.short_name,
        "{{SUMMARY}}": f"A CausalVideoGroup research project led by {leader.name}.",
    }
    metadata_template = (root / "templates" / "project-metadata-template.yaml").read_text(encoding="utf-8")
    page_template = (root / "templates" / "project-index-template.html").read_text(encoding="utf-8")
    (destination / "metadata.yaml").write_text(render(metadata_template, values), encoding="utf-8")
    (destination / "index.html").write_text(render(page_template, values, html_mode=True), encoding="utf-8")
    return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--leader", required=True, help="approved leader short name")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args(argv)
    root = Path(__file__).resolve().parent.parent
    try:
        destination = create_project(root, args.slug, args.title, args.leader, args.force)
    except (ValueError, FileExistsError, FileNotFoundError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(destination.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
