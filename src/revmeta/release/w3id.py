"""Offline W3ID .htaccess draft from verified RDF graphs; no registration or HTTP."""
from __future__ import annotations

import re

from rdflib import Graph, RDF, URIRef
from rdflib.namespace import SKOS

BASE = "https://w3id.org/revmeta/"
PAGES_BASE = "https://mmarcinmichal.github.io/revmeta/"
GUIDANCE_KINDS = frozenset({
    "boundaryNote", "codeWhen", "doNotCodeWhen",
    "negativeExample", "positiveExample",
})
STATES = frozenset({
    "AMBIGUOUS", "INSUFFICIENT_ACCESS", "NEGATIVE_VERIFIED",
    "NOT_ESTABLISHED", "NOT_IN_SCOPE", "SATISFIED", "VOCABULARY_GAP",
})


def _local_iris(graph: Graph) -> set[str]:
    """All RevMeta URIRefs used anywhere in the RDF graph, including predicates."""
    return {
        str(node)[len(BASE):]
        for triple in graph
        for node in triple
        if isinstance(node, URIRef) and str(node).startswith(BASE)
    }


def _alternatives(values: set[str]) -> str:
    if not values or any(not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]*", v) for v in values):
        raise ValueError("Unexpected RevMeta URI local names")
    return "(?:" + "|".join(re.escape(v) for v in sorted(values)) + ")"


def render_w3id_draft(vocabulary: Graph, states: Graph, mappings: Graph) -> str:
    """Produce 303 redirects for the existing IRIs, without minting new RDF IDs.

    Known concepts/facets have HTML anchors. Guidance, metadata predicates and
    sources exist only in vocabulary RDF. Decision states and the mapping set
    have separate Turtle documents; JSON-LD is NOT claimed for those graphs.
    """
    concepts = {
        str(term)[len(BASE):] for term in vocabulary.subjects(RDF.type, SKOS.Concept)
        if str(term).startswith(BASE)
    }
    facets = {
        str(term)[len(BASE + "facet/"):]
        for term in vocabulary.subjects(RDF.type, SKOS.Collection)
        if str(term).startswith(BASE + "facet/")
    }
    all_vocabulary = _local_iris(vocabulary)
    guidance = {p for p in all_vocabulary if p.startswith("guidance/")}
    sources = {p[len("source/"):] for p in all_vocabulary if p.startswith("source/")}
    top = {
        p for p in all_vocabulary
        if "/" not in p and "." not in p
    }
    counts = (len(concepts), len(facets), len(guidance), len(sources), len(top))
    if counts != (102, 14, 691, 3, 12):
        raise ValueError(f"Unexpected RevMeta identifier family cardinality: {counts}")

    term_regex = _alternatives(concepts)
    facet_regex = _alternatives(facets)
    source_regex = _alternatives(sources)
    top_regex = _alternatives(top)
    kinds_regex = _alternatives(set(GUIDANCE_KINDS))
    guidance_regex = rf"guidance/[A-Za-z][A-Za-z0-9_-]*\.[A-Za-z][A-Za-z0-9_-]*/{kinds_regex}/[0-9]{{3}}"

    for path in guidance:
        fields = path.split("/")
        if (len(fields) != 4 or fields[1] not in concepts or
                fields[2] not in GUIDANCE_KINDS or
                not re.fullmatch(r"[0-9]{3}", fields[3])):
            raise ValueError(f"Unexpected guidance IRI: {path}")
    expected_vocabulary = (
        concepts | {"facet/" + name for name in facets}
        | {"source/" + name for name in sources} | top | guidance
    )
    if all_vocabulary != expected_vocabulary or "scheme" not in top:
        raise ValueError("Unclassified vocabulary IRIs")

    state_paths = _local_iris(states)
    expected_states = {"decisionStates"} | {"state/" + name for name in STATES}
    if state_paths != expected_states:
        raise ValueError("Unexpected decision-state IRIs")
    mapping_paths = _local_iris(mappings)
    if mapping_paths != concepts | {"mappings"}:
        raise ValueError("Unexpected mapping-set IRIs")

    # A bounded guidance path shape avoids Apache's long-line limits; the
    # verified graphs (and regression tests) enumerate the 691 actual IRIs.
    # A syntactically valid but unminted guidance URL may redirect to the RDF
    # document without asserting that it identifies a described resource.
    vocab_known = (
        rf"(?:{term_regex}|facet/{facet_regex}|{top_regex}|"
        rf"source/{source_regex}|{guidance_regex})"
    )
    state_regex = _alternatives(set(STATES))
    files = (
        r"(vocabulary\.(?:ttl|jsonld)|decision-states\.ttl|"
        r"mappings\.sssom\.(?:ttl|tsv)|alignments\.ttl)"
    )
    return "\n".join([
        "# # /revmeta/",
        "# Identifier: " + BASE,
        "# Provisional RevMeta identifier redirects; DO NOT REGISTER without owner approval.",
        "# Owner-controlled target: " + PAGES_BASE,
        "# ## Contact",
        "# Maintainer: Marcin Michał Mirończuk",
        "# GitHub username: mmarcinmichal",
        "# https://github.com/mmarcinmichal",
        "RewriteEngine on",
        "",
        "# Direct representation URLs, all present in the approved Pages site.",
        f"RewriteRule ^{files}$ {PAGES_BASE}$1 [R=303,L]",
        "",
        "# Mapping set and coding states are separate RDF graphs (Turtle only).",
        f"RewriteRule ^mappings$ {PAGES_BASE}mappings.sssom.ttl [R=303,L]",
        f"RewriteRule ^(?:decisionStates|state/{state_regex})$ "
        f"{PAGES_BASE}decision-states.ttl [R=303,L]",
        "",
        "# Base vocabulary IRI: RDF on Accept, otherwise documentation.",
        "RewriteCond %{HTTP_ACCEPT} text/turtle [NC]",
        f"RewriteRule ^$ {PAGES_BASE}vocabulary.ttl [R=303,L]",
        r"RewriteCond %{HTTP_ACCEPT} application/ld\+json [NC]",
        f"RewriteRule ^$ {PAGES_BASE}vocabulary.jsonld [R=303,L]",
        f"RewriteRule ^$ {PAGES_BASE}index.html [R=303,L]",
        "",
        "# Vocabulary resources: serve the representation containing each IRI.",
        "RewriteCond %{HTTP_ACCEPT} text/turtle [NC]",
        f"RewriteRule ^{vocab_known}$ {PAGES_BASE}vocabulary.ttl [R=303,L]",
        r"RewriteCond %{HTTP_ACCEPT} application/ld\+json [NC]",
        f"RewriteRule ^{vocab_known}$ {PAGES_BASE}vocabulary.jsonld [R=303,L]",
        "",
        "# Existing HTML fragment identifiers for concepts, facets and scheme.",
        f"RewriteRule ^facet/({facet_regex})$ {PAGES_BASE}index.html#facet-$1 [R=303,L,NE]",
        f"RewriteRule ^({term_regex})$ {PAGES_BASE}index.html#concept-$1 [R=303,L,NE]",
        f"RewriteRule ^scheme$ {PAGES_BASE}index.html [R=303,L]",
        "",
        "# Guidance, metadata properties and source records have no HTML anchors.",
        f"RewriteRule ^{vocab_known}$ {PAGES_BASE}vocabulary.ttl [R=303,L]",
        "",
    ])
