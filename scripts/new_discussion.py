#!/usr/bin/env python3
"""Create a discussion directory from the repository templates."""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path


SLUG_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


@dataclass(frozen=True)
class Leader:
    name: str
    short_name: str


TEMPLATE_OUTPUTS = {
    "discussion-metadata-template.yaml": "metadata.yaml",
    "discussion-index-template.html": "index.html",
    "discussion-summary-template.html": "summary.html",
    "references-template.md": "references.md",
    "meeting-note-template.md": "meeting-note.md",
    "action-items-template.md": "action-items.md",
    "idea-map-template.md": "idea-map.md",
}


def parse_date(value: str) -> str:
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("date must be a real calendar date in YYYY-MM-DD format") from exc
    if parsed.isoformat() != value:
        raise ValueError("date must use zero-padded YYYY-MM-DD format")
    return value


def validate_slug(value: str, label: str) -> str:
    if not SLUG_PATTERN.fullmatch(value):
        raise ValueError(
            f"{label} must contain lowercase letters, digits, and single hyphens only"
        )
    return value


def load_leaders(path: Path) -> dict[str, Leader]:
    """Read the intentionally small, fixed-shape people registry without PyYAML."""
    leaders: dict[str, Leader] = {}
    current_name: str | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        name_match = re.fullmatch(r"  - name: (.+)", raw_line)
        short_match = re.fullmatch(r"    short_name: ([a-z0-9-]+)", raw_line)
        if name_match:
            current_name = name_match.group(1).strip()
        elif short_match:
            if current_name is None:
                raise ValueError(f"short_name appears before name in {path}")
            short_name = validate_slug(short_match.group(1), "leader short name")
            if short_name in leaders:
                raise ValueError(f"duplicate leader short name: {short_name}")
            leaders[short_name] = Leader(current_name, short_name)
            current_name = None

    if not leaders:
        raise ValueError(f"no leaders found in {path}")
    if current_name is not None:
        raise ValueError(f"leader {current_name!r} has no short_name in {path}")
    return leaders


def yaml_double_quoted(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ")


def render_template(template_name: str, source: str, values: dict[str, str]) -> str:
    if template_name.endswith(".html"):
        replacements = {key: html.escape(value, quote=True) for key, value in values.items()}
    elif template_name.endswith(".yaml"):
        replacements = values | {"{{TITLE}}": yaml_double_quoted(values["{{TITLE}}"])}
    else:
        replacements = values

    rendered = source
    for token, replacement in replacements.items():
        rendered = rendered.replace(token, replacement)
    unresolved = sorted(set(re.findall(r"\{\{[A-Z_]+\}\}", rendered)))
    if unresolved:
        raise ValueError(f"unresolved placeholders in {template_name}: {', '.join(unresolved)}")
    return rendered


def create_discussion(
    root: Path,
    discussion_date: str,
    leader_short_name: str,
    topic_slug: str,
    title: str,
    force: bool = False,
) -> Path:
    discussion_date = parse_date(discussion_date)
    leader_short_name = validate_slug(leader_short_name, "leader")
    topic_slug = validate_slug(topic_slug, "topic")
    title = title.strip()
    if not title:
        raise ValueError("title must not be empty")

    leaders = load_leaders(root / "data" / "people.yaml")
    if leader_short_name not in leaders:
        choices = ", ".join(sorted(leaders))
        raise ValueError(f"unknown leader {leader_short_name!r}; choose one of: {choices}")
    leader = leaders[leader_short_name]

    directory_name = f"{discussion_date}-{leader.short_name}-{topic_slug}"
    destination = root / "discussions" / directory_name
    if destination.exists() and not force:
        raise FileExistsError(f"discussion already exists: {destination}")
    destination.mkdir(parents=True, exist_ok=True)
    (destination / "assets").mkdir(exist_ok=True)
    (destination / "assets" / ".gitkeep").touch(exist_ok=True)

    values = {
        "{{TITLE}}": title,
        "{{DATE}}": discussion_date,
        "{{TOPIC_SLUG}}": topic_slug,
        "{{LEADER_NAME}}": leader.name,
        "{{LEADER_SHORT_NAME}}": leader.short_name,
        "{{SUMMARY}}": f"A CausalVideoGroup discussion led by {leader.name}.",
    }

    template_dir = root / "templates"
    for template_name, output_name in TEMPLATE_OUTPUTS.items():
        template_path = template_dir / template_name
        if not template_path.is_file():
            raise FileNotFoundError(f"missing template: {template_path}")
        rendered = render_template(
            template_name, template_path.read_text(encoding="utf-8"), values
        )
        (destination / output_name).write_text(rendered, encoding="utf-8")

    return destination


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--date", required=True, help="meeting date in YYYY-MM-DD format")
    parser.add_argument("--leader", required=True, help="approved leader short name")
    parser.add_argument("--topic", required=True, help="lowercase kebab-case topic slug")
    parser.add_argument("--title", required=True, help="display title")
    parser.add_argument(
        "--force",
        action="store_true",
        help="overwrite template-managed files while preserving other files",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = Path(__file__).resolve().parent.parent
    try:
        destination = create_discussion(
            root=root,
            discussion_date=args.date,
            leader_short_name=args.leader,
            topic_slug=args.topic,
            title=args.title,
            force=args.force,
        )
    except (ValueError, FileExistsError, FileNotFoundError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(destination.relative_to(root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
