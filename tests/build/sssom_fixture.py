"""Create a synthetic SSSOM mapping row to validate the exporter against sssom-py."""
from pathlib import Path
from revmeta.build.mappings import export_sssom

row = {
    'subject_id': 'revmeta:hasReviewDesign.SystematicReviewDesign',
    'subject_label': 'Systematic review design',
    'predicate_id': 'skos:relatedMatch',
    'object_id': 'sssom:NoTermFound',
    'object_label': '',
    'mapping_justification': 'semapv:ManualMappingCuration',
    'mapping_tool': 'manual validation fixture',
    'reviewer_label': 'Test reviewer',
    'comment': 'Synthetic NoTermFound row for schema validation only',
}
export_sssom([row], Path('/tmp/revmeta-sssom-fixture.tsv'))
