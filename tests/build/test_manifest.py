"""Tests for deterministic, fail-closed development build manifests."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from revmeta.build.manifest import write_manifest


class ManifestTests(unittest.TestCase):
    def test_manifest_hashes_are_stable_and_missing_inputs_block_completeness(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'registry.json'
            source.write_text('{"terms":[]}', encoding='utf-8')
            generated = root / 'vocabulary.ttl'
            generated.write_text('<urn:example:a> <urn:example:p> <urn:example:b> .\n', encoding='utf-8')
            missing = root / 'annotator-guide.md'
            version = root / 'VERSION'
            version.write_text('1.0.0\n', encoding='utf-8')
            manifest = root / 'manifest.json'
            write_manifest({"registry": source, "codebook": missing}, [generated], manifest, version)
            first = manifest.read_bytes()
            write_manifest({'registry': source, 'codebook': missing}, [generated], manifest, version)
            self.assertEqual(first, manifest.read_bytes())
            record = json.loads(first)
            self.assertFalse(record['inputs_complete'])
            self.assertEqual(record['status'], 'build-output')
            self.assertNotIn('publication_authorized', record)
            self.assertEqual(record['version'], '1.0.0')
            self.assertEqual(record['output_sha256']['vocabulary.ttl'],
                             hashlib.sha256(generated.read_bytes()).hexdigest())


if __name__ == '__main__':
    unittest.main()
