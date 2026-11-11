"""Fail-closed SSSOM TSV export from the frozen, single-sheet XLSX workbook.

Uses Python's standard OOXML (ZIP/XML) facilities; no external service.
The approved SSSOM mapping relationships and external targets are NEVER inferred.
"""
from __future__ import annotations

import csv
import hashlib
import io
import posixpath
import re
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

from .vocabulary import BASE, LICENSE_URI

NS = {'s': 'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}
SOURCE_COLUMNS = ['row_id', 'subject_id', 'subject_label', 'predicate_id', 'object_id',
                  'object_label', 'mapping_justification', 'mapping_tool', 'reviewer_label',
                  'comment', 'target_check']
SSSOM_COLUMNS = ['subject_id', 'subject_label', 'predicate_id', 'object_id', 'object_label',
                 'mapping_justification', 'mapping_tool', 'reviewer_label', 'comment']
MAPPING_SET_ID = 'https://w3id.org/revmeta/mappings'
MAPPING_SET_TITLE = 'RevMeta reviewed terminology mappings'
MAPPING_SET_DESCRIPTION = 'Frozen source mappings with 34 NoTermFound placeholders.'
MAPPING_SET_LICENSE = LICENSE_URI
PREDICATES = {'skos:broadMatch', 'skos:narrowMatch', 'skos:closeMatch', 'skos:relatedMatch'}
CURIE_MAP = {
    'COAR_RT': 'http://purl.org/coar/resource_type/',
    'MESH': 'http://id.nlm.nih.gov/mesh/',
    'STATO': 'http://purl.obolibrary.org/obo/STATO_',
    'dcat': 'http://www.w3.org/ns/dcat#',
    'fabio': 'http://purl.org/spar/fabio/',
    'mls': 'http://www.w3.org/ns/mls#',
    'prov': 'http://www.w3.org/ns/prov#',
    'revmeta': BASE,
    'semapv': 'https://w3id.org/semapv/vocab/',
    'skos': 'http://www.w3.org/2004/02/skos/core#',
    'sssom': 'https://w3id.org/sssom/',
}


def _column_index(cell_ref: str) -> int:
    match = re.fullmatch(r'([A-Z]+)[0-9]+', cell_ref)
    if not match:
        raise ValueError(f'Unsupported cell reference: {cell_ref}')
    idx = 0
    for letter in match.group(1):
        idx = idx * 26 + ord(letter) - ord('A') + 1
    return idx - 1


def _read_xlsx(path: Path) -> list[list[str]]:
    with ZipFile(path) as archive:
        workbook = ET.fromstring(archive.read('xl/workbook.xml'))
        sheets = workbook.findall('.//s:sheets/s:sheet', NS)
        if len(sheets) != 1 or sheets[0].get('name') != 'mappings':
            raise ValueError('Expected exactly one sheet named mappings')
        shared = []
        if 'xl/sharedStrings.xml' in archive.namelist():
            node = ET.fromstring(archive.read('xl/sharedStrings.xml'))
            shared = [''.join(t.text or '' for t in n.findall('.//s:t', NS))
                      for n in node.findall('s:si', NS)]
        # Resolve the visible sheet using OOXML relationships, never sheet1.xml.
        rel_id = sheets[0].get(
            '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
        if sheets[0].get('state', 'visible') != 'visible' or not rel_id:
            raise ValueError('Mapping sheet must be visible and have a relationship id')
        rels = ET.fromstring(archive.read('xl/_rels/workbook.xml.rels'))
        matches = [r for r in rels
                   if r.get('Id') == rel_id and
                   r.tag == '{http://schemas.openxmlformats.org/package/2006/relationships}Relationship']
        if len(matches) != 1 or matches[0].get('TargetMode') == 'External':
            raise ValueError('Invalid worksheet relationship')
        relation = matches[0]
        if not relation.get('Type', '').endswith('/worksheet'):
            raise ValueError('Mapping relationship is not a worksheet')
        target = relation.get('Target', '')
        if not target or '\\' in target or '?' in target or '#' in target:
            raise ValueError('Invalid worksheet target')
        part = (posixpath.normpath(target.lstrip('/')) if target.startswith('/')
                else posixpath.normpath(posixpath.join('xl', target)))
        worksheet_parts = {n for n in archive.namelist()
                           if n.startswith('xl/worksheets/') and n.endswith('.xml')}
        if part not in worksheet_parts or worksheet_parts != {part}:
            raise ValueError('Missing or unreferenced worksheet XML part')
        sheet = ET.fromstring(archive.read(part))
        matrix = []
        for row in sheet.findall('.//s:sheetData/s:row', NS):
            fields = [''] * len(SOURCE_COLUMNS)
            for cell in row.findall('s:c', NS):
                index = _column_index(cell.get('r', ''))
                if index >= len(fields):
                    raise ValueError('Unexpected spreadsheet column')
                if cell.find('s:f', NS) is not None:
                    raise ValueError('Formulas are forbidden in frozen source workbook')
                kind = cell.get('t')
                if kind == 'inlineStr':
                    value = ''.join(t.text or '' for t in cell.findall('.//s:is//s:t', NS))
                else:
                    node = cell.find('s:v', NS)
                    value = node.text or '' if node is not None else ''
                    if kind == 's':
                        value = shared[int(value)]
                    elif kind not in (None, 'n', 'str'):
                        raise ValueError(f'Unsupported XLSX type: {kind}')
                fields[index] = value
            matrix.append(fields)
    return matrix


def load_mapping_rows(path: Path, registry: dict,
                      expected_sha256: str | None = None) -> list[dict[str, str]]:
    if not path.is_file():
        raise ValueError('Canonical mapping workbook does not exist')
    # A caller may pin a released canonical checksum. The predecessor workbook
    # checksum must NEVER be used against the normalized RevMeta workbook.
    if expected_sha256 is not None:
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected_sha256:
            raise ValueError('Canonical mapping workbook SHA-256 mismatch')
    # The private historical-source migration gate compares every cell of
    # canonical sources/mappings.xlsx to the archived unchanged predecessor XLSX.
    matrix = _read_xlsx(path)
    if not matrix or matrix[0] != SOURCE_COLUMNS or len(matrix) != 142:
        raise ValueError('Unexpected mapping workbook schema or row count')
    registry_terms = {term['term'] for term in registry['terms']}
    row_ids, used_subjects, records = set(), set(), []
    for data in matrix[1:]:
        record = dict(zip(SOURCE_COLUMNS, data))
        rid = record['row_id']
        if not rid or rid in row_ids:
            raise ValueError(f'Invalid or repeated row identifier {rid}')
        row_ids.add(rid)
        subject = record['subject_id']
        if not subject.startswith('revmeta:'):
            raise ValueError(f'Canonical mapping subject must use revmeta: at row {rid}: {subject}')
        if subject not in registry_terms:
            raise ValueError(f'Unknown RevMeta subject at row {rid}: {subject}')
        record['subject_id'] = subject
        used_subjects.add(subject)
        if record['predicate_id'] not in PREDICATES:
            raise ValueError(f'Unapproved SKOS mapping predicate at row {rid}')
        target = record['object_id']
        if ':' not in target or target.split(':', 1)[0] not in CURIE_MAP:
            raise ValueError(f'Unknown mapping target prefix at row {rid}')
        if record['mapping_justification'] != 'semapv:ManualMappingCuration':
            raise ValueError(f'Unexpected mapping justification at row {rid}')
        if not record['reviewer_label'] or not record['mapping_tool'] or not record['target_check'].startswith('OK'):
            raise ValueError(f'Missing mapping provenance or target validation at row {rid}')
        records.append(record)
    if used_subjects != registry_terms:
        raise ValueError('The mapping set does not cover all 102 registry subjects')
    if sum(row['object_id'] == 'sssom:NoTermFound' for row in records) != 34:
        raise ValueError('Expected exactly 34 NoTermFound records')
    if sum(row['object_id'] != 'sssom:NoTermFound' for row in records) != 107:
        raise ValueError('Expected exactly 107 concrete mapping targets')
    return records


def export_sssom(rows: list[dict[str, str]], output: Path) -> None:
    """Exclude source-only row_id and target_check; preserve sentinel rows in TSV."""
    header = ['# curie_map:'] + [f'#   {prefix}: {iri}' for prefix, iri in sorted(CURIE_MAP.items())]
    header += [
        f'# mapping_set_id: {MAPPING_SET_ID}',
        f'# mapping_set_title: {MAPPING_SET_TITLE}',
        f'# mapping_set_description: {MAPPING_SET_DESCRIPTION}',
        f'# license: {MAPPING_SET_LICENSE}',
    ]
    stream = io.StringIO(newline='')
    stream.write('\n'.join(header) + '\n')
    writer = csv.DictWriter(stream, fieldnames=SSSOM_COLUMNS, delimiter='\t',
                            lineterminator='\n', extrasaction='ignore')
    writer.writeheader()
    writer.writerows(rows)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(stream.getvalue(), encoding='utf-8')
