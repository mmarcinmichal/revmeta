"""SSSOM/RDF projection contract: all records, metadata and no direct edges."""
import json
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS
from revmeta.build.alignments import build_alignment_graph, expand_curie
from revmeta.build.mappings import (
    MAPPING_SET_DESCRIPTION, MAPPING_SET_ID, MAPPING_SET_TITLE, MAPPING_SET_LICENSE,
    SSSOM_COLUMNS, load_mapping_rows,
)
from revmeta.build.sssom_rdf import SSSOM, build_sssom_rdf_graph, write_sssom_rdf

ROOT = Path(__file__).resolve().parents[2]
WORKBOOK = ROOT / "resources/inputs/vocabulary/mappings.xlsx"


class SssomRdfTests(unittest.TestCase):
    def synthetic_rows(self):
        common = {
            "subject_id": "revmeta:hasReviewDesign.SystematicReviewDesign",
            "subject_label": "Systematic review design",
            "predicate_id": "skos:relatedMatch",
            "mapping_justification": "semapv:ManualMappingCuration",
            "mapping_tool": "manual review",
            "reviewer_label": "Curator A",
            "comment": "Review note\nwith newline",
        }
        return [
            dict(common, object_id="sssom:NoTermFound", object_label=""),
            dict(common, object_id="fabio:ReviewArticle", object_label="Review article"),
        ]

    def check_graph(self, rows):
        graph = build_sssom_rdf_graph(rows)
        set_iri = URIRef(MAPPING_SET_ID)
        self.assertIn((set_iri, RDF.type, SSSOM.MappingSet), graph)
        self.assertIn((set_iri, DCTERMS.title, Literal(MAPPING_SET_TITLE)), graph)
        self.assertIn((set_iri, DCTERMS.description, Literal(MAPPING_SET_DESCRIPTION)), graph)
        self.assertIn((set_iri, DCTERMS.license, URIRef(MAPPING_SET_LICENSE)), graph)
        nodes = list(graph.objects(set_iri, SSSOM.mappings))
        self.assertEqual(len(nodes), len(rows))
        self.assertEqual(len(set(nodes)), len(rows))
        observed = []
        for node in nodes:
            self.assertIn((node, RDF.type, OWL.Axiom), graph)
            record = {
                "subject_id": next(iter(graph.objects(node, OWL.annotatedSource)), None),
                "predicate_id": next(iter(graph.objects(node, OWL.annotatedProperty)), None),
                "object_id": next(iter(graph.objects(node, OWL.annotatedTarget)), None),
            }
            for field in ("subject_id", "predicate_id", "object_id"):
                self.assertIsNotNone(record[field])
            for field in SSSOM_COLUMNS:
                if field in record:
                    continue
                predicate = RDFS.comment if field == 'comment' else SSSOM[field]
                values = list(graph.objects(node, predicate))
                record[field] = "|".join(sorted(str(v) for v in values)) if field == "reviewer_label" else (
                    str(values[0]) if values else ""
                )
            record["mapping_justification"] = next(iter(
                graph.objects(node, SSSOM.mapping_justification)), None)
            self.assertIsNotNone(record["mapping_justification"])
            observed.append(record)

        def normalise(record):
            out = {}
            for field in SSSOM_COLUMNS:
                value = record[field]
                if field in ("subject_id", "predicate_id", "object_id", "mapping_justification"):
                    value = str(value) if isinstance(value, URIRef) else str(expand_curie(value))
                out[field] = value
            return tuple(out[field] for field in SSSOM_COLUMNS)
        self.assertCountEqual([normalise(row) for row in rows],
                              [normalise(row) for row in observed])
        self.assertFalse(any(graph.triples((None, SSSOM.comment, None))))
        self.assertEqual(sum(1 for row in rows if row['comment']),
                         len(list(graph.triples((None, RDFS.comment, None)))))
        for row in rows:
            triple = tuple(expand_curie(row[key]) for key in
                           ("subject_id", "predicate_id", "object_id"))
            self.assertNotIn(triple, graph)
        return graph

    def test_fixture_preserves_no_match_and_provenance(self):
        rows = self.synthetic_rows()
        expected = self.check_graph(rows)
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "mappings.sssom.ttl"
            write_sssom_rdf(rows, path)
            original = path.read_bytes()
            write_sssom_rdf(rows, path)
            self.assertEqual(original, path.read_bytes())
            self.assertTrue(Graph().parse(path, format="turtle").isomorphic(expected))

    @unittest.skipUnless(WORKBOOK.is_file(), "Source workbook unavailable")
    def test_frozen_source_complete_and_alignment_separation(self):
        registry = json.loads((ROOT / "resources/inputs/vocabulary/registry.json").read_text(encoding="utf-8"))
        rows = load_mapping_rows(WORKBOOK, registry)
        self.assertEqual(len(rows), 141)
        graph = self.check_graph(rows)
        self.assertEqual(sum(1 for row in rows if row['comment']), 90)
        self.assertEqual(len(list(graph.triples((None, RDFS.comment, None)))), 90)
        self.assertEqual(sum(1 for n in graph.subjects(RDF.type, OWL.Axiom)
                             if (n, OWL.annotatedTarget,
                                 expand_curie("sssom:NoTermFound")) in graph), 34)
        alignments = build_alignment_graph(rows)
        self.assertEqual(len(alignments), 107)
        self.assertEqual(len(set(graph.objects(URIRef(MAPPING_SET_ID), SSSOM.mappings))),
                         141)


if __name__ == "__main__":
    unittest.main()
