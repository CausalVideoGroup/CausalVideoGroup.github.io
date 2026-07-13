from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.new_project import create_project


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent


class NewProjectTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary_directory = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary_directory.name)
        shutil.copytree(REPOSITORY_ROOT / "templates", self.root / "templates")
        shutil.copytree(REPOSITORY_ROOT / "data", self.root / "data")
        (self.root / "projects").mkdir()

    def tearDown(self) -> None:
        self.temporary_directory.cleanup()

    def test_creates_project_page(self) -> None:
        destination = create_project(
            self.root, "example-project", "Example Project", "yifan"
        )
        self.assertEqual(destination.name, "example-project")
        self.assertTrue((destination / "index.html").is_file())
        self.assertTrue((destination / "metadata.yaml").is_file())
        metadata = (destination / "metadata.yaml").read_text(encoding="utf-8")
        self.assertIn('name: "Yifan Shen"', metadata)

    def test_rejects_unknown_leader(self) -> None:
        with self.assertRaisesRegex(ValueError, "unknown leader"):
            create_project(self.root, "example", "Example", "unknown")

    def test_refuses_to_overwrite(self) -> None:
        create_project(self.root, "example", "Example", "yifan")
        with self.assertRaises(FileExistsError):
            create_project(self.root, "example", "Example", "yifan")


if __name__ == "__main__":
    unittest.main()
