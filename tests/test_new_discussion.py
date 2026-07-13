from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.new_discussion import create_discussion


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent


class NewDiscussionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        shutil.copytree(REPOSITORY_ROOT / "templates", self.root / "templates")
        shutil.copytree(REPOSITORY_ROOT / "data", self.root / "data")
        (self.root / "discussions").mkdir()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_creates_expected_directory_and_files(self) -> None:
        destination = create_discussion(
            root=self.root,
            discussion_date="2026-07-13",
            leader_short_name="yifan",
            topic_slug="forcing-ar-video-distillation",
            title="Forcing Series: The Evolution of AR Video Distillation",
        )
        self.assertEqual(
            destination.name, "2026-07-13-yifan-forcing-ar-video-distillation"
        )
        for filename in (
            "metadata.yaml",
            "index.html",
            "summary.html",
            "references.md",
            "meeting-note.md",
            "action-items.md",
            "idea-map.md",
            "assets/.gitkeep",
        ):
            self.assertTrue((destination / filename).exists(), filename)
        metadata = (destination / "metadata.yaml").read_text(encoding="utf-8")
        self.assertIn("name: \"Yifan Shen\"", metadata)
        self.assertIn("short_name: yifan", metadata)

    def test_rejects_unknown_leader(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown leader"):
            create_discussion(
                self.root, "2026-07-18", "unknown", "topic", "Topic"
            )

    def test_rejects_invalid_calendar_date(self) -> None:
        with self.assertRaisesRegex(ValueError, "real calendar date"):
            create_discussion(
                self.root, "2026-02-30", "peiyuan", "topic", "Topic"
            )

    def test_refuses_to_overwrite_by_default(self) -> None:
        arguments = (self.root, "2026-07-18", "peiyuan", "topic", "Topic")
        create_discussion(*arguments)
        with self.assertRaises(FileExistsError):
            create_discussion(*arguments)


if __name__ == "__main__":
    unittest.main()
