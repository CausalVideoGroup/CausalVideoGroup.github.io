#!/usr/bin/env python3
"""Validate CausalVideoGroup website content before publication."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

try:
    from .build_site import load_discussions
    from .new_discussion import SLUG_PATTERN, load_leaders
except ImportError:  # Direct execution
    from build_site import load_discussions
    from new_discussion import SLUG_PATTERN, load_leaders


REQUIRED_FILES = {
    "metadata.yaml",
    "index.html",
    "summary.html",
    "references.md",
    "meeting-note.md",
    "action-items.md",
}
VALID_STATUSES = {"planned", "before-meeting", "after-meeting", "archived"}
QUALITY_LABELS = (
    "Central claim:",
    "Hidden assumption:",
    "Failure boundary:",
    "Connection:",
    "Concrete experiment:",
    "Discussion seed:",
)
MEDIA_SUFFIXES = {".mp4", ".webm", ".mov", ".avi", ".mkv"}
MAX_MEDIA_BYTES = 10 * 1024 * 1024


@dataclass(frozen=True)
class Finding:
    level: str
    path: str
    message: str


class LinkCollector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attributes: list[tuple[str, str | None]]) -> None:
        for key, value in attributes:
            if key in {"href", "src"} and value:
                self.links.append(value)


def validate_local_links(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for page in root.rglob("*.html"):
        if ".git" in page.parts or "templates" in page.parts:
            continue
        collector = LinkCollector()
        collector.feed(page.read_text(encoding="utf-8"))
        for link in collector.links:
            if link.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target_text = link.split("#", 1)[0].split("?", 1)[0]
            target = (page.parent / target_text).resolve()
            if link.endswith("/"):
                target = target / "index.html"
            if not target.exists():
                findings.append(Finding("ERROR", str(page.relative_to(root)), f"broken local link: {link}"))
    return findings


def validate(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    leaders = load_leaders(root / "data" / "people.yaml")
    try:
        discussions = load_discussions(root)
    except ValueError as exc:
        return [Finding("ERROR", "discussions", str(exc))]

    for item in discussions:
        folder = root / "discussions" / item.directory
        expected = f"{item.date}-{item.leader_short_name}-{item.topic_slug}"
        if item.directory != expected:
            findings.append(Finding("ERROR", str(folder.relative_to(root)), f"directory must be named {expected}"))
        if item.leader_short_name not in leaders:
            findings.append(Finding("ERROR", str(folder.relative_to(root)), "leader is not in data/people.yaml"))
        elif leaders[item.leader_short_name].name != item.leader_name:
            findings.append(Finding("ERROR", str(folder.relative_to(root)), "leader full name does not match registry"))
        if item.status not in VALID_STATUSES:
            findings.append(Finding("ERROR", str(folder.relative_to(root)), f"unsupported status: {item.status}"))
        if not item.tags or any(not SLUG_PATTERN.fullmatch(tag) for tag in item.tags):
            findings.append(Finding("ERROR", str(folder.relative_to(root)), "tags must be non-empty lowercase slugs"))
        for filename in sorted(REQUIRED_FILES):
            if not (folder / filename).is_file():
                findings.append(Finding("ERROR", str(folder.relative_to(root)), f"missing required file: {filename}"))

        summary_path = folder / "summary.html"
        if summary_path.is_file():
            summary = summary_path.read_text(encoding="utf-8")
            for label in QUALITY_LABELS:
                if label not in summary:
                    findings.append(Finding("ERROR", str(summary_path.relative_to(root)), f"missing research field: {label}"))
            question_count = len(re.findall(r"<li>.*?</li>", summary, re.DOTALL))
            if question_count < 5:
                findings.append(Finding("ERROR", str(summary_path.relative_to(root)), "include at least five open questions"))

        references_path = folder / "references.md"
        if references_path.is_file():
            references = references_path.read_text(encoding="utf-8")
            if len(re.findall(r"^##\s+\d+\.", references, re.MULTILINE)) < 3:
                findings.append(Finding("ERROR", str(references_path.relative_to(root)), "include at least three references"))

        metadata_text = (folder / "metadata.yaml").read_text(encoding="utf-8")
        for raw_url in re.findall(r"^\s+url:\s+(\S+)", metadata_text, re.MULTILINE):
            parsed = urlparse(raw_url)
            if parsed.scheme not in {"http", "https"} or not parsed.netloc:
                findings.append(Finding("ERROR", str((folder / 'metadata.yaml').relative_to(root)), f"malformed URL: {raw_url}"))

    for media in root.rglob("*"):
        if media.is_file() and media.suffix.lower() in MEDIA_SUFFIXES and media.stat().st_size > MAX_MEDIA_BYTES:
            findings.append(Finding("ERROR", str(media.relative_to(root)), "preview video exceeds 10 MiB; use external storage"))

    findings.extend(validate_local_links(root))
    return findings


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    findings = validate(root)
    for finding in findings:
        print(f"{finding.level}: {finding.path}: {finding.message}")
    errors = sum(finding.level == "ERROR" for finding in findings)
    if errors:
        print(f"Validation failed with {errors} error(s).", file=sys.stderr)
        return 1
    print(f"Validation passed for {len(load_discussions(root))} discussion(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
