from __future__ import annotations

import unittest
from pathlib import Path

from scripts.validate_site import validate


REPOSITORY_ROOT = Path(__file__).resolve().parent.parent


class ValidateSiteTests(unittest.TestCase):
    def test_repository_content_is_valid(self) -> None:
        findings = validate(REPOSITORY_ROOT)
        self.assertEqual([], findings)


if __name__ == "__main__":
    unittest.main()
