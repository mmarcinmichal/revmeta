"""Generate RevMeta's seven primary epistemic decision states as separate SKOS.

The concepts here form a source-visible auxiliary *coding guide* for
annotators and authors, NOT additional terms in the frozen 102-term vocabulary.

Definitions and evidence criteria follow the owner's approved 2026-11-08
seven-state Codebook-layer specification (SEM-0006). Historical v19 had
other statuses and scope modes, but does not constrain this current scheme.
This module does not define the separate publication-profile data model.
"""
from __future__ import annotations

from pathlib import Path
from rdflib import Graph, Literal, Namespace, URIRef
from rdflib.namespace import DCTERMS, RDF, SKOS

from .vocabulary import BASE, LICENSE_URI, canonical_turtle

# code, label, definition, operational evidence requirements
PRIMARY_DECISION_STATES = (
    (
        "SATISFIED", "Satisfied",
        "The term applies to the publication: the publication's own review provides affirmative and material evidence for it, and every gate the codebook defines for the term is met.",
        "Requires at least one exact quote with its locator and an explanation of how the passage supports the term in the publication's own review. Quotes from the reference list alone are insufficient.",
    ),
    (
        "NOT_ESTABLISHED", "Not established",
        "After appropriate inspection of the source, no sufficient affirmative evidence supports the term, but its absence has not been demonstrated.",
        "Record of the inspection performed. This is the default outcome of an unsuccessful positive check and is never read as false.",
    ),
    (
        "NEGATIVE_VERIFIED", "Negative verified",
        "A bounded full-text check, including a search for affirmative counter-evidence, establishes that the term does not apply to the publication.",
        "Requires the scope of the check, checks performed, counter-evidence considered, any missing material, and why absence can safely be established. Never inferred from a missing keyword, from the reference list alone, or from the lack of an explicit methods section.",
    ),
    (
        "AMBIGUOUS", "Ambiguous",
        "Relevant passages admit materially different interpretations under the term's definition.",
        "Requires the competing readings and at least one anchored excerpt where the source is accessible.",
    ),
    (
        "INSUFFICIENT_ACCESS", "Insufficient access",
        "Material needed for the decision, such as supplementary files, is missing or defective and could change the outcome.",
        "Requires identification of the missing or defective material.",
    ),
    (
        "VOCABULARY_GAP", "Vocabulary gap",
        "The publication documents a material methodological feature that no controlled term adequately represents.",
        "Requires the feature, at least one anchored excerpt, and the closest terms considered. No new term is created.",
    ),
    (
        "NOT_IN_SCOPE", "Not in scope",
        "The term is excluded from routine coding in the current release of the vocabulary.",
        "Applies only to terms with registry depth REVIEW.",
    ),
)

TWO_VALUED_VIEW_NOTE = (
    "In a two-valued view, SATISFIED may be read as true and "
    "NEGATIVE_VERIFIED as false; every other state is read as unknown. "
    "NOT_ESTABLISHED and AMBIGUOUS are never read as false."
)


def decision_states_graph(base: str = BASE) -> Graph:
    root = Namespace(base)
    scheme = root["decisionStates"]
    graph = Graph()
    graph.bind("revmeta", root)
    graph.bind("skos", SKOS)
    graph.add((scheme, RDF.type, SKOS.ConceptScheme))
    graph.add((scheme, SKOS.prefLabel, Literal("RevMeta decision states", lang="en")))
    graph.add((scheme, DCTERMS.license, URIRef(LICENSE_URI)))
    graph.add((scheme, SKOS.definition, Literal(
        "Outcomes of assessing whether a controlled RevMeta term applies to a publication.",
        lang="en")))
    graph.add((scheme, SKOS.scopeNote, Literal(TWO_VALUED_VIEW_NOTE, lang="en")))
    if len({row[0] for row in PRIMARY_DECISION_STATES}) != 7:
        raise AssertionError("Seven distinct primary states required")
    for code, label, definition, evidence in PRIMARY_DECISION_STATES:
        concept = root["state/" + code]
        graph.add((concept, RDF.type, SKOS.Concept))
        graph.add((concept, SKOS.inScheme, scheme))
        graph.add((concept, SKOS.topConceptOf, scheme))
        graph.add((concept, SKOS.notation, Literal(code)))
        graph.add((concept, SKOS.prefLabel, Literal(label, lang="en")))
        graph.add((concept, SKOS.definition, Literal(definition, lang="en")))
        graph.add((concept, SKOS.scopeNote, Literal(evidence, lang="en")))
    return graph


def write_decision_states(output: Path, base: str = BASE) -> Path:
    graph = decision_states_graph(base)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(canonical_turtle(graph, base), encoding="utf-8")
    actual = Graph().parse(output, format="turtle")
    if not actual.isomorphic(graph):
        raise AssertionError("State scheme Turtle does not round-trip")
    return output
