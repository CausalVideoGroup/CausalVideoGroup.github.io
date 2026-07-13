#!/usr/bin/env python3
"""Generate website indexes from discussion metadata using the standard library."""

from __future__ import annotations

import html
import re
from dataclasses import dataclass
from pathlib import Path

try:
    from .new_discussion import load_leaders
except ImportError:  # Direct execution: python3 scripts/build_site.py
    from new_discussion import load_leaders


START = "<!-- GENERATED:{name}:START -->"
END = "<!-- GENERATED:{name}:END -->"


@dataclass(frozen=True)
class Discussion:
    directory: str
    title: str
    date: str
    topic_slug: str
    leader_name: str
    leader_short_name: str
    status: str
    summary: str
    tags: tuple[str, ...]
    related_projects: tuple[str, ...]


def unquote(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return value


def read_discussion_metadata(path: Path) -> Discussion:
    """Read the documented metadata fields without requiring a YAML package."""
    lines = path.read_text(encoding="utf-8").splitlines()
    scalar: dict[str, str] = {}
    leader: dict[str, str] = {}
    lists: dict[str, list[str]] = {"tags": [], "related_projects": []}
    index = 0

    while index < len(lines):
        line = lines[index]
        top = re.fullmatch(r"([a-z_]+):(?:\s*(.*))?", line)
        if not top:
            index += 1
            continue
        key, raw_value = top.group(1), (top.group(2) or "")
        if key == "leader":
            index += 1
            while index < len(lines):
                nested = re.fullmatch(r"  ([a-z_]+):\s*(.+)", lines[index])
                if not nested:
                    break
                leader[nested.group(1)] = unquote(nested.group(2))
                index += 1
            continue
        if key in lists:
            index += 1
            while index < len(lines):
                item = re.fullmatch(r"  -\s+(.+)", lines[index])
                if not item:
                    break
                lists[key].append(unquote(item.group(1)))
                index += 1
            continue
        if raw_value in (">", ">-", "|", "|-"):
            index += 1
            parts: list[str] = []
            while index < len(lines) and (not lines[index] or lines[index].startswith("  ")):
                parts.append(lines[index].strip())
                index += 1
            scalar[key] = " ".join(part for part in parts if part)
            continue
        scalar[key] = unquote(raw_value)
        index += 1

    required = ("title", "date", "topic_slug", "status", "summary")
    missing = [key for key in required if not scalar.get(key)]
    missing.extend(key for key in ("name", "short_name") if not leader.get(key))
    if missing:
        raise ValueError(f"{path}: missing metadata fields: {', '.join(missing)}")
    return Discussion(
        directory=path.parent.name,
        title=scalar["title"],
        date=scalar["date"],
        topic_slug=scalar["topic_slug"],
        leader_name=leader["name"],
        leader_short_name=leader["short_name"],
        status=scalar["status"],
        summary=scalar["summary"],
        tags=tuple(lists["tags"]),
        related_projects=tuple(lists["related_projects"]),
    )


def load_discussions(root: Path) -> list[Discussion]:
    discussions = [
        read_discussion_metadata(path)
        for path in (root / "discussions").glob("*/metadata.yaml")
    ]
    return sorted(discussions, key=lambda item: (item.date, item.directory), reverse=True)


def replace_region(source: str, name: str, content: str) -> str:
    start, end = START.format(name=name), END.format(name=name)
    pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
    if not pattern.search(source):
        raise ValueError(f"generated region {name!r} not found")
    return pattern.sub(f"{start}\n{content.rstrip()}\n{end}", source, count=1)


def tags_html(tags: tuple[str, ...]) -> str:
    return " ".join(f'<span class="tag">{html.escape(tag)}</span>' for tag in tags)


def discussion_card(item: Discussion, prefix: str) -> str:
    url = f"{prefix}discussions/{html.escape(item.directory)}/"
    return (
        '<article class="card">'
        f'<p class="meta">{html.escape(item.date)} · {html.escape(item.leader_name)}</p>'
        f'<h3>{html.escape(item.title)}</h3>'
        f'<p>{html.escape(item.summary)}</p>'
        f'<p><span class="tag">{html.escape(item.status)}</span> {tags_html(item.tags)}</p>'
        f'<a class="card-link" href="{url}">Read discussion →</a>'
        '</article>'
    )


def write_region(path: Path, name: str, content: str) -> None:
    source = path.read_text(encoding="utf-8")
    rendered = replace_region(source, name, content)
    path.write_text(rendered, encoding="utf-8")


def build(root: Path) -> None:
    discussions = load_discussions(root)
    leaders = load_leaders(root / "data" / "people.yaml")

    recent = discussions[:3]
    home_content = (
        '<div class="grid">'
        + "\n".join(discussion_card(item, "") for item in recent)
        + "</div>"
        if recent
        else '<div class="empty-state">No discussions have been published yet.</div>'
    )
    write_region(root / "index.html", "recent-discussions", home_content)

    archive_content = (
        '<div class="grid">'
        + "\n".join(discussion_card(item, "../") for item in discussions)
        + "</div>"
        if discussions
        else '<div class="empty-state">No discussions have been published yet.</div>'
    )
    write_region(root / "discussions" / "index.html", "discussion-archive", archive_content)

    people_cards = []
    for short_name, leader in leaders.items():
        led = [item for item in discussions if item.leader_short_name == short_name]
        links = "".join(
            f'<li><a href="../discussions/{html.escape(item.directory)}/">{html.escape(item.date)} · {html.escape(item.title)}</a></li>'
            for item in led
        )
        detail = f"<ul>{links}</ul>" if links else "<p>No published discussions yet.</p>"
        people_cards.append(
            f'<article class="card"><p class="meta">Discussion leader · {html.escape(short_name)}</p>'
            f'<h3>{html.escape(leader.name)}</h3>{detail}</article>'
        )
    write_region(root / "people" / "index.html", "people-list", '<div class="grid">' + "\n".join(people_cards) + "</div>")

    tag_map: dict[str, list[Discussion]] = {}
    for item in discussions:
        for tag in item.tags:
            tag_map.setdefault(tag, []).append(item)
    tag_cards = []
    for tag, items in sorted(tag_map.items()):
        links = "".join(
            f'<li><a href="../discussions/{html.escape(item.directory)}/">{html.escape(item.title)}</a></li>'
            for item in items
        )
        tag_cards.append(
            f'<article class="card"><p class="meta">{len(items)} discussion(s)</p>'
            f'<h3>{html.escape(tag)}</h3><ul>{links}</ul></article>'
        )
    tag_content = (
        '<div class="grid">' + "\n".join(tag_cards) + "</div>"
        if tag_cards
        else '<div class="empty-state">No tags have been published yet.</div>'
    )
    write_region(root / "tags" / "index.html", "tag-list", tag_content)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    build(root)
    print(f"Generated indexes for {len(load_discussions(root))} discussion(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
