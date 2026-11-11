"""Machine-readable fidelity of all 691 frozen Codebook statements in RDF."""
from __future__ import annotations

from copy import deepcopy
from dataclasses import replace
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, SKOS, XSD

from revmeta.build.codebook import (
    SECTION_PREDICATES, EXPECTED_COUNTS, check_registry_parity, parse_codebook,
)
from revmeta.build.html_docs import write_html
from revmeta.build.vocabulary import BASE, LICENSE_URI, build, registry_graph

ROOT = Path(__file__).resolve().parents[2]
CODEBOOK_PATH = ROOT / "resources/inputs/vocabulary/codebook.md"
REGISTRY_PATH = ROOT / "resources/inputs/vocabulary/registry.json"
REV = Namespace(BASE)


class MachineReadableCodebookTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.source_text = CODEBOOK_PATH.read_text(encoding="utf-8")
        cls.lines = cls.source_text.splitlines()
        cls.registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
        cls.guide = parse_codebook(CODEBOOK_PATH)
        cls.graph = registry_graph(cls.registry, codebook=cls.guide)

    def test_parser_counts_and_parity(self):
        self.assertEqual(len(self.guide.facets), 14)
        self.assertEqual(len(self.guide.terms), 102)
        self.assertEqual(self.guide.rule_counts, EXPECTED_COUNTS)
        self.assertEqual(sum(self.guide.rule_counts.values()), 691)
        check_registry_parity(self.guide, self.registry)
        for term in self.guide.terms.values():
            self.assertEqual(len(term.observed_sections), 5)
            for entries in term.sections.values():
                for n, item in enumerate(entries, start=1):
                    self.assertEqual(item.ordinal, n)
                    self.assertEqual(self.lines[item.source_line - 1], "- " + item.text)

    def test_every_source_item_is_exactly_recovered_from_graph(self):
        graph = self.graph
        self.assertEqual(len(set(graph.subjects(RDF.type, SKOS.Concept))), 102)
        self.assertEqual(len(set(graph.subjects(RDF.type, SKOS.Collection))), 14)
        self.assertEqual(len(set(graph.subjects(RDF.type, REV.CodingGuidanceItem))), 691)
        self.assertEqual(len(list(graph.triples((None, SKOS.broader, None)))), 0)
        self.assertEqual(len(list(graph.subjects(RDF.type, OWL.ObjectProperty))), 0)
        observed = {role: 0 for _, role in SECTION_PREDICATES}
        for identifier, guide in self.guide.terms.items():
            concept = REV[identifier[len("revmeta:"):]]
            for heading, role in SECTION_PREDICATES:
                nodes = list(graph.objects(concept, REV[role]))
                actual = []
                for node in nodes:
                    self.assertIn((node, RDF.type, REV.CodingGuidanceItem), graph)
                    text = list(graph.objects(node, RDF.value))
                    indexes = list(graph.objects(node, REV.itemIndex))
                    lines = list(graph.objects(node, REV.sourceLine))
                    self.assertEqual(len(text), 1, (identifier, heading))
                    self.assertEqual(len(indexes), 1)
                    self.assertEqual(len(lines), 1)
                    self.assertEqual(text[0].language, "en")
                    self.assertEqual(indexes[0].datatype, XSD.integer)
                    self.assertEqual(lines[0].datatype, XSD.integer)
                    position = int(indexes[0])
                    source_line = int(lines[0])
                    actual.append((position, str(text[0]), source_line))
                    self.assertEqual(self.lines[source_line - 1], "- " + str(text[0]))
                expected = [(x.ordinal, x.text, x.source_line)
                            for x in guide.sections[role]]
                self.assertEqual(sorted(actual), expected, (identifier, role))
                self.assertEqual(len(actual), len(set(actual)))
                observed[role] += len(actual)
        self.assertEqual(observed, EXPECTED_COUNTS)

    def test_all_facet_labels_definitions_boundaries_are_verbatim(self):
        graph = self.graph
        for name, facet in self.guide.facets.items():
            collection = REV["facet/" + name[len("revmeta:"):]]
            self.assertIn((collection, SKOS.prefLabel, Literal(facet.label, lang="en")), graph)
            self.assertIn((collection, SKOS.definition,
                           Literal(facet.definition, lang="en")), graph)
            self.assertIn((collection, SKOS.scopeNote,
                           Literal(facet.boundary, lang="en")), graph)
            self.assertIn((collection, SKOS.notation, Literal(name)), graph)
            self.assertIn((collection, REV.facetTier, Literal(facet.tier)), graph)
            self.assertNotIn((collection, RDF.type, RDF.Property), graph)

    def test_rdf_metadata_stable_source_digests_and_version(self):
        with tempfile.TemporaryDirectory() as d:
            ttl, jsonld = build(REGISTRY_PATH, Path(d))
            rdf = Graph().parse(ttl, format="turtle")
            other = Graph().parse(jsonld, format="json-ld")
            self.assertTrue(rdf.isomorphic(other))
            self.assertEqual(len(set(rdf.subjects(RDF.type, REV.CodingGuidanceItem))), 691)
            self.assertIn((REV.scheme, DCTERMS.hasVersion, Literal("1.0.0")), rdf)
            self.assertIn((REV.scheme, DCTERMS.license, URIRef(LICENSE_URI)), rdf)
            for filename in ("registry.json", "codebook.md", "mappings.xlsx"):
                source = ROOT / "resources/inputs/vocabulary" / filename
                node = REV["source/" + source.stem]
                self.assertIn((REV.scheme, DCTERMS.source, node), rdf)
                self.assertIn((node, DCTERMS.identifier, Literal(Path(filename).stem)), rdf)
                sha = hashlib.sha256(source.read_bytes()).hexdigest()
                self.assertIn((node, REV.sha256, Literal(sha)), rdf)

    def test_parser_rejects_content_loss_and_source_drift(self):
        with self.assertRaises(ValueError):
            parse_codebook(self.source_text.replace("- ", "", 1))
        with self.assertRaisesRegex(ValueError, "Unrecognized Codebook content"):
            parse_codebook(self.source_text + "\nUNACCOUNTED SOURCE CONTENT\n")
        with self.assertRaisesRegex(ValueError, "Duplicate Codebook term"):
            term = next(iter(self.guide.terms.values()))
            heading = "### \x60" + term.identifier + "\x60 — " + term.label
            code = self.source_text.replace(heading, heading + "\n" + heading, 1)
            parse_codebook(code)
        broken = deepcopy(self.guide)
        first = next(iter(broken.terms.values()))
        first.definition += " SPURIOUS"
        with self.assertRaisesRegex(ValueError, "definition mismatch"):
            check_registry_parity(broken, self.registry)

    def test_escaped_html_contains_all_original_rule_values(self):
        with tempfile.TemporaryDirectory() as d:
            path = Path(d)
            ttl, _ = build(REGISTRY_PATH, path)
            target = write_html(ttl, path / "index.html")
            document = target.read_text(encoding="utf-8")
            self.assertEqual(document.count('<div class="guidance"'), 102)
            self.assertEqual(document.count("<li>"), 691 + 14)
            self.assertIn("Facet boundary:", document)
            self.assertIn("CODE WHEN", document)
            self.assertIn("DO NOT CODE WHEN", document)
            self.assertIn("Positive examples", document)
            self.assertIn("Negative examples", document)
            self.assertNotIn("RSP Annotator Term Quick Reference", document)


if __name__ == "__main__":
    unittest.main()
