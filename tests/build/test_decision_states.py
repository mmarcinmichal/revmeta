"""Primary decision states are disjoint from the 102-term registry."""
import json
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph, Literal, Namespace
from rdflib.namespace import RDF, SKOS

from revmeta.build.decision_states import (
    PRIMARY_DECISION_STATES,
    TWO_VALUED_VIEW_NOTE, decision_states_graph, write_decision_states,
)
from revmeta.build.vocabulary import BASE, registry_graph

ROOT = Path(__file__).resolve().parents[2]
REV = Namespace(BASE)
EXPECTED = {
    "SATISFIED", "NOT_ESTABLISHED", "NEGATIVE_VERIFIED", "AMBIGUOUS",
    "INSUFFICIENT_ACCESS", "VOCABULARY_GAP", "NOT_IN_SCOPE",
}


class DecisionStateTests(unittest.TestCase):
    def test_separate_scheme_has_exactly_seven_primary_values(self):
        g = decision_states_graph()
        scheme = REV.decisionStates
        concepts = set(g.subjects(RDF.type, SKOS.Concept))
        self.assertEqual(len(concepts), 7)
        self.assertEqual({str(x) for x in g.objects(None, SKOS.notation)}, EXPECTED)
        self.assertEqual(len(PRIMARY_DECISION_STATES), 7)
        self.assertIn((scheme, RDF.type, SKOS.ConceptScheme), g)
        self.assertIn((scheme, SKOS.scopeNote, Literal(TWO_VALUED_VIEW_NOTE, lang="en")), g)
        for c in concepts:
            self.assertIn((c, SKOS.inScheme, scheme), g)
            self.assertIn((c, SKOS.topConceptOf, scheme), g)
            for p in (SKOS.definition, SKOS.scopeNote, SKOS.prefLabel, SKOS.notation):
                self.assertEqual(len(list(g.objects(c, p))), 1)
            self.assertTrue(str(c).startswith(BASE + "state/"))
        self.assertEqual(str(next(g.objects(REV["state/NOT_IN_SCOPE"], SKOS.definition))),
                         "The term is excluded from routine coding in the current release of the vocabulary.")
        self.assertEqual(str(next(g.objects(REV["state/NOT_IN_SCOPE"], SKOS.scopeNote))),
                         "Applies only to terms with registry depth REVIEW.")
        self.assertEqual(str(next(g.objects(REV["state/VOCABULARY_GAP"], SKOS.scopeNote))),
                         "Requires the feature, at least one anchored excerpt, and the closest terms considered. No new term is created.")
        self.assertNotIn("CORE_ONLY", str(next(g.objects(REV["state/NOT_IN_SCOPE"],
                                                      SKOS.scopeNote))))

    def test_human_coding_guide_matches_machine_definitions(self):
        """Human guidance must not silently drift from the seven RDF meanings."""
        guide = (ROOT / "docs/user/README.md").read_text(encoding="utf-8")
        for code, label, definition, evidence in PRIMARY_DECISION_STATES:
            with self.subTest(code=code):
                self.assertIn("`" + code + "`", guide)
                self.assertIn(definition, guide)
        self.assertIn("closest terms considered", guide)
        self.assertIn("Applies only to terms with registry depth `REVIEW`.", guide)
        self.assertNotIn("CORE_ONLY", guide)

    def test_no_pollution_of_frozen_vocabulary(self):
        data = json.loads((ROOT / "resources/inputs/vocabulary/registry.json").read_text(encoding="utf-8"))
        original = registry_graph(data)
        statuses = decision_states_graph()
        self.assertEqual(len(set(original.subjects(RDF.type, SKOS.Concept))), 102)
        self.assertEqual(len(set(original.subjects(RDF.type, SKOS.Collection))), 14)
        self.assertTrue(set(original.subjects(RDF.type, SKOS.Concept)).isdisjoint(
            set(statuses.subjects(RDF.type, SKOS.Concept))))
        self.assertNotIn((REV.scheme, RDF.type, SKOS.ConceptScheme), statuses)

    def test_bytes_and_rdf_graph_are_deterministic(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "decision-states.ttl"
            write_decision_states(path)
            original = path.read_bytes()
            write_decision_states(path)
            self.assertEqual(original, path.read_bytes())
            self.assertTrue(Graph().parse(path, format="turtle")
                            .isomorphic(decision_states_graph()))


if __name__ == "__main__":
    unittest.main()
