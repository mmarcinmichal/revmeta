"""Offline, unregistered W3ID redirect draft. No HTTP calls or registration."""
from __future__ import annotations

import re

from rdflib import Graph, RDF
from rdflib.namespace import SKOS

BASE = "https://w3id.org/revmeta/"
PAGES_BASE = "https://mmarcinmichal.github.io/revmeta/"

def render_w3id_draft(graph: Graph) -> str:
    """Generate a bounded Apache draft for 102 concepts, 14 facets and scheme.

    The rest of the internal RDF subject identifiers, including Codebook
    guidance, require a separate URI coverage decision before publication.
    """
    concepts = sorted(str(c)[len(BASE):] for c in graph.subjects(RDF.type, SKOS.Concept))
    facets = sorted(str(f)[len(BASE + "facet/"):] for f in graph.subjects(RDF.type, SKOS.Collection))
    if len(concepts) != 102 or len(facets) != 14 or any(
            not re.fullmatch(r"[A-Za-z][A-Za-z0-9_.-]*", x) for x in concepts + facets):
        raise ValueError("Unexpected URI local names")
    terms = "(" + "|".join(re.escape(x) for x in concepts) + ")"
    facet_names = "(" + "|".join(re.escape(x) for x in facets) + ")"
    known = "(?:scheme|" + terms + "|facet/" + facet_names + ")"
    return "\n".join([
        "# DRAFT ONLY: do not register until public HTTPS endpoint is live",
        "# RevMeta https://w3id.org/revmeta/; maintainer GitHub: mmarcinmichal",
        "RewriteEngine on",
        "",
        "# Base identifier, with RDF representations ahead of HTML fallback.",
        "RewriteCond %{HTTP_ACCEPT} text/turtle [NC]",
        f"RewriteRule ^$ {PAGES_BASE}vocabulary.ttl [R=303,L]",
        "RewriteCond %{HTTP_ACCEPT} application/ld\\+json [NC]",
        f"RewriteRule ^$ {PAGES_BASE}vocabulary.jsonld [R=303,L]",
        f"RewriteRule ^$ {PAGES_BASE}index.html [R=303,L]",
        "",
        "# Explicit RDF representation URLs.",
        f"RewriteRule ^(vocabulary\\.ttl|vocabulary\\.jsonld)$ {PAGES_BASE}$1 [R=303,L]",
        "",
        "# Only known concept/facet/scheme identifiers, no open-ended catch-all.",
        "RewriteCond %{HTTP_ACCEPT} text/turtle [NC]",
        f"RewriteRule ^{known}$ {PAGES_BASE}vocabulary.ttl [R=303,L]",
        "RewriteCond %{HTTP_ACCEPT} application/ld\\+json [NC]",
        f"RewriteRule ^{known}$ {PAGES_BASE}vocabulary.jsonld [R=303,L]",
        f"RewriteRule ^facet/{facet_names}$ {PAGES_BASE}index.html#facet-$1 [R=303,L,NE]",
        f"RewriteRule ^{terms}$ {PAGES_BASE}index.html#concept-$1 [R=303,L,NE]",
        f"RewriteRule ^scheme$ {PAGES_BASE}index.html [R=303,L]",
        "",
    ])
