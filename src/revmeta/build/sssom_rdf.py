"""Deterministic SSSOM/RDF mapping-set projection (without direct SKOS triples).

A mapping record is an owl:Axiom linked from the SSSOM MappingSet. Stable,
source-order blank-node identifiers preserve duplicate rows and reproducibility.
The only authority is the same vetted list read from sources/mappings.xlsx.
"""
from __future__ import annotations

from pathlib import Path

from rdflib import BNode, Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDF, RDFS

from .alignments import expand_curie
from .mappings import (
    MAPPING_SET_DESCRIPTION, MAPPING_SET_ID, MAPPING_SET_TITLE, MAPPING_SET_LICENSE, SSSOM_COLUMNS,
)

SSSOM = Namespace("https://w3id.org/sssom/")
IDENTIFIERS = {
    "subject_id": OWL.annotatedSource,
    "predicate_id": OWL.annotatedProperty,
    "object_id": OWL.annotatedTarget,
}


def build_sssom_rdf_graph(rows: list[dict[str, str]]) -> Graph:
    """Keep *all* mapping records, including NoTermFound, as annotated axioms."""
    graph = Graph()
    mapping_set = URIRef(MAPPING_SET_ID)
    graph.add((mapping_set, RDF.type, SSSOM.MappingSet))
    graph.add((mapping_set, DCTERMS.title, Literal(MAPPING_SET_TITLE)))
    graph.add((mapping_set, DCTERMS.description, Literal(MAPPING_SET_DESCRIPTION)))
    graph.add((mapping_set, DCTERMS.license, URIRef(MAPPING_SET_LICENSE)))

    for number, row in enumerate(rows, start=1):
        node = BNode(f"revmeta_mapping_{number:04d}")
        graph.add((mapping_set, SSSOM.mappings, node))
        graph.add((node, RDF.type, OWL.Axiom))
        for field in SSSOM_COLUMNS:
            value = row.get(field, "")
            if not value:
                continue
            if field in IDENTIFIERS:
                predicate = IDENTIFIERS[field]
                obj = expand_curie(value)
            elif field == 'comment':
                # SSSOM LinkML slot_uri is rdfs:comment, NOT sssom:comment.
                predicate = RDFS.comment
                obj = Literal(value)
            elif field == "mapping_justification":
                predicate = SSSOM.mapping_justification
                obj = expand_curie(value)
            elif field == "reviewer_label":
                # SSSOM reviewer_label is a multivalued slot, pipe-separated in TSV.
                for reviewer in value.split("|"):
                    if reviewer:
                        graph.add((node, SSSOM.reviewer_label, Literal(reviewer)))
                continue
            else:
                predicate = SSSOM[field]
                obj = Literal(value)
            graph.add((node, predicate, obj))

    if len(set(graph.objects(mapping_set, SSSOM.mappings))) != len(rows):
        raise AssertionError("SSSOM/RDF lost a mapping record")
    # owl:annotatedSource/Property/Target describe a mapping; they are not
    # license to assert a direct (subject, predicate, object) triple.
    for row in rows:
        direct = tuple(expand_curie(row[key]) for key in
                       ("subject_id", "predicate_id", "object_id"))
        if direct in graph:
            raise AssertionError("SSSOM/RDF unexpectedly asserts a direct mapping")
    return graph


def write_sssom_rdf(rows: list[dict[str, str]], output: Path) -> Path:
    graph = build_sssom_rdf_graph(rows)
    output.parent.mkdir(parents=True, exist_ok=True)
    # N-Triples syntax is valid Turtle. Explicit stable BNode labels plus sorted
    # statements avoid serializer-order dependence and ensure byte stability.
    triples = sorted(f"{s.n3()} {p.n3()} {o.n3()} ." for s, p, o in graph)
    output.write_text(
        "# RevMeta SSSOM/RDF mapping records; no direct SKOS mapping triples.\n"
        + "\n".join(triples) + "\n", encoding="utf-8"
    )
    if not Graph().parse(output, format="turtle").isomorphic(graph):
        raise AssertionError("SSSOM/RDF round-trip changed the graph")
    return output
