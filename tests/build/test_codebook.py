"""Portable Codebook source checks; independent from private source history."""
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


class CanonicalCodebookTests(unittest.TestCase):
    def test_current_codebook_covers_all_102_terms(self):
        registry = json.loads((ROOT / "resources/inputs/vocabulary/registry.json").read_text(encoding="utf-8"))
        guide = (ROOT / "resources/inputs/vocabulary/codebook.md").read_text(encoding="utf-8")
        self.assertEqual(len(registry["terms"]), 102)
        self.assertEqual(guide.count("**CODE WHEN**"), 102)
        self.assertEqual(guide.count("**DO NOT CODE WHEN**"), 102)
        for term in registry["terms"]:
            with self.subTest(term=term["term"]):
                self.assertIn(f"`{term['term']}`", guide)


if __name__ == "__main__":
    unittest.main()
