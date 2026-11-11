"""Frozen mapping invariants; full integration runs when resources/inputs/vocabulary/mappings.xlsx is present."""
import csv
import io
import json
import tempfile
import unittest
from pathlib import Path
from revmeta.build.mappings import CURIE_MAP, SOURCE_COLUMNS, SSSOM_COLUMNS, MAPPING_SET_LICENSE, export_sssom, load_mapping_rows

ROOT = Path(__file__).resolve().parents[2]
WORKBOOK = ROOT / 'resources/inputs/vocabulary/mappings.xlsx'


class MappingContractTests(unittest.TestCase):
    def test_sssom_serialization_does_not_export_internal_columns(self):
        row = {x: '' for x in SOURCE_COLUMNS}
        row.update({
            'row_id': 'sample', 'subject_id': 'revmeta:hasReviewDesign.SystematicReviewDesign',
            'subject_label': 'Systematic review design', 'predicate_id': 'skos:relatedMatch',
            'object_id': 'sssom:NoTermFound',
            'mapping_justification': 'semapv:ManualMappingCuration',
            'mapping_tool': 'manual review', 'reviewer_label': 'Reviewer',
            'comment': 'No match found', 'target_check': 'OK: sentinel'
        })
        with tempfile.TemporaryDirectory() as tmp:
            destination = Path(tmp) / 'mappings.sssom.tsv'
            export_sssom([row], destination)
            text = destination.read_text(encoding='utf-8')
            header_lines = [line for line in text.splitlines() if line.startswith('#')]
            self.assertIn('# curie_map:', header_lines)
            self.assertIn(f'# license: {MAPPING_SET_LICENSE}', header_lines)
            self.assertIn('#   sssom: https://w3id.org/sssom/', header_lines)
            lines = [line for line in text.splitlines() if not line.startswith('#')]
            data = list(csv.DictReader(io.StringIO('\n'.join(lines)), delimiter='\t'))
            self.assertEqual(set(data[0].keys()), set(SSSOM_COLUMNS))
            self.assertEqual(data[0]['object_id'], 'sssom:NoTermFound')
            self.assertNotIn('target_check', data[0])
            self.assertNotIn('row_id', data[0])

    @unittest.skipUnless(WORKBOOK.is_file(), 'M0 pending: source workbook not yet in GitHub')
    def test_frozen_workbook_exact_counts(self):
        registry = json.loads((ROOT / 'resources/inputs/vocabulary/registry.json').read_text(encoding='utf-8'))
        rows = load_mapping_rows(WORKBOOK, registry)
        self.assertEqual(len(rows), 141)
        self.assertEqual(len({x['subject_id'] for x in rows}), 102)
        self.assertEqual(sum(x['object_id'] != 'sssom:NoTermFound' for x in rows), 107)
        self.assertEqual(sum(x['object_id'] == 'sssom:NoTermFound' for x in rows), 34)


if __name__ == '__main__':
    unittest.main()
