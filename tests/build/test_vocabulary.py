"""Frozen registry SKOS graph tests. No unapproved OWL inferences."""
import json
import tempfile
import unittest
from pathlib import Path
from rdflib import RDF
from rdflib.namespace import SKOS, OWL
from revmeta.build.vocabulary import REV, SCHEME, build, registry_graph

ROOT = Path(__file__).resolve().parents[2]


class VocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.registry = json.loads((ROOT / 'resources/inputs/vocabulary/registry.json').read_text(encoding='utf-8'))
        cls.graph = registry_graph(cls.registry)

    def test_graph_scope_and_concept_count(self):
        g = self.graph
        self.assertEqual(len(set(g.subjects(RDF.type, SKOS.Concept))), 102)
        self.assertEqual(len(set(g.subjects(RDF.type, SKOS.Collection))), 14)
        self.assertIn((SCHEME, RDF.type, SKOS.ConceptScheme), g)
        self.assertEqual(len(set(g.subjects(RDF.type, OWL.ObjectProperty))), 0)
        self.assertEqual(len(set(g.triples((None, SKOS.broader, None)))), 0)
        self.assertEqual(len(set(g.triples((None, SKOS.relatedMatch, None)))), 0)

    def test_definitions_are_verbatim(self):
        for term in self.registry['terms']:
            concept = REV[term['term'][len('revmeta:'):]]
            self.assertEqual([str(x) for x in self.graph.objects(concept, SKOS.definition)], [term['definition']])
            self.assertEqual([str(x) for x in self.graph.objects(concept, SKOS.prefLabel)], [term['label']])

    def test_repeated_build_is_byte_identical(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            a = build(ROOT / 'resources/inputs/vocabulary/registry.json', root / 'a')
            b = build(ROOT / 'resources/inputs/vocabulary/registry.json', root / 'b')
            for x, y in zip(a, b):
                self.assertEqual(x.read_bytes(), y.read_bytes())


if __name__ == '__main__':
    unittest.main()
