"""Current portable sources use only RevMeta identity, not archived names."""
import hashlib
import json
import re
import unittest
from pathlib import Path

from revmeta.build.mappings import load_mapping_rows
from revmeta.build.codebook import parse_codebook, EXPECTED_COUNTS

ROOT = Path(__file__).resolve().parents[2]
OBSOLETE = re.compile(r"\bRSP\b|rsp[-_:]|RSP_")


class RevMetaSourceIdentityTests(unittest.TestCase):
    def test_current_registry_and_codebook_have_no_obsolete_identity(self):
        registry_file = ROOT / "resources/inputs/vocabulary/registry.json"
        codebook_file = ROOT / "resources/inputs/vocabulary/codebook.md"
        registry_text = registry_file.read_text(encoding="utf-8")
        codebook_text = codebook_file.read_text(encoding="utf-8")
        self.assertIsNone(OBSOLETE.search(registry_text))
        self.assertIsNone(OBSOLETE.search(codebook_text))
        registry = json.loads(registry_text)
        self.assertEqual(registry["registry_id"], "revmeta-102-terms-source-v2")
        self.assertEqual(registry["source_reference_filename"], "codebook.md")
        self.assertEqual(registry["source_reference_sha256"],
                         hashlib.sha256(codebook_file.read_bytes()).hexdigest())
        self.assertEqual(parse_codebook(codebook_file).rule_counts, EXPECTED_COUNTS)

    def test_mapping_comments_have_no_predecessor_branding(self):
        registry = json.loads((ROOT / "resources/inputs/vocabulary/registry.json").read_text(encoding="utf-8"))
        records = load_mapping_rows(ROOT / "resources/inputs/vocabulary/mappings.xlsx", registry)
        self.assertEqual(len(records), 141)
        self.assertEqual(sum(x["object_id"] == "sssom:NoTermFound" for x in records), 34)
        self.assertEqual(sum(bool(x["comment"]) for x in records), 90)
        for row in records:
            with self.subTest(row=row["row_id"]):
                self.assertIsNone(OBSOLETE.search(row["comment"]))

    def test_user_guide_has_only_current_identity_and_source_hashes(self):
        guide = (ROOT / "docs/user/README.md").read_text(encoding="utf-8")
        self.assertIsNone(OBSOLETE.search(guide))
        self.assertIn("0008_revmeta_2", guide)
        for name in ("registry.json", "codebook.md", "mappings.xlsx"):
            digest = hashlib.sha256((ROOT / "resources/inputs/vocabulary" / name).read_bytes()).hexdigest()
            self.assertIn(digest, guide)


if __name__ == "__main__":
    unittest.main()
