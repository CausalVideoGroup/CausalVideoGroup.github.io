from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts.build_site import read_discussion_metadata, replace_region


class BuildSiteTests(unittest.TestCase):
    def test_reads_required_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            folder = Path(temporary_directory) / "2026-07-18-peiyuan-topic"
            folder.mkdir()
            path = folder / "metadata.yaml"
            path.write_text(
                'title: "A Topic"\n'
                "date: 2026-07-18\n"
                "topic_slug: topic\n"
                "leader:\n"
                '  name: "Peiyuan Zhu"\n'
                "  short_name: peiyuan\n"
                "status: before-meeting\n"
                "summary: >-\n"
                "  First line\n"
                "  second line.\n"
                "tags:\n"
                "  - video-generation\n",
                encoding="utf-8",
            )
            item = read_discussion_metadata(path)
            self.assertEqual(item.leader_short_name, "peiyuan")
            self.assertEqual(item.topic_slug, "topic")
            self.assertEqual(item.summary, "First line second line.")
            self.assertEqual(item.tags, ("video-generation",))

    def test_replaces_only_named_region(self) -> None:
        source = "before\n<!-- GENERATED:x:START -->\nold\n<!-- GENERATED:x:END -->\nafter"
        result = replace_region(source, "x", "new")
        self.assertEqual(
            result,
            "before\n<!-- GENERATED:x:START -->\nnew\n<!-- GENERATED:x:END -->\nafter",
        )

    def test_missing_region_is_an_error(self) -> None:
        with self.assertRaisesRegex(ValueError, "not found"):
            replace_region("page", "missing", "content")


if __name__ == "__main__":
    unittest.main()
