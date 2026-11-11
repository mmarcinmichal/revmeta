"""Deterministic, offline HTML documentation projected from generated SKOS RDF.

The RDF graph, rather than a duplicated term list, is authoritative for this
display. It identifies licensed project-owned content without asserting
registered namespace redirects, public-release approval or scientific certification.
"""
from __future__ import annotations

from html import escape
from pathlib import Path
import re

from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import DCTERMS, SKOS

from .codebook import SECTION_PREDICATES


def _one_literal(graph: Graph, subject: URIRef, predicate: URIRef,
                 lang: str | None = None) -> str:
    values = list(graph.objects(subject, predicate))
    if len(values) != 1 or not isinstance(values[0], Literal):
        raise ValueError(f'Expected one literal for {subject} {predicate}')
    if lang is not None and values[0].language != lang:
        raise ValueError(f'Expected @{lang} literal for {subject} {predicate}')
    return str(values[0])


def _anchor(prefix: str, local: str) -> str:
    # Source CURIE local names are used directly for legible, stable anchors.
    if not re.fullmatch(r'[A-Za-z0-9_.-]+', local):
        raise ValueError(f'Unsafe or unsupported HTML anchor local name: {local!r}')
    return prefix + '-' + local


def write_html(vocabulary_ttl: Path, destination: Path) -> Path:
    graph = Graph().parse(vocabulary_ttl, format='turtle')
    schemes = set(graph.subjects(RDF.type, SKOS.ConceptScheme))
    concepts = set(graph.subjects(RDF.type, SKOS.Concept))
    collections = set(graph.subjects(RDF.type, SKOS.Collection))
    if len(schemes) != 1 or len(concepts) != 102 or len(collections) != 14:
        raise ValueError('Unexpected SKOS scheme, concept or facet cardinality')
    scheme = next(iter(schemes))
    version = (_one_literal(graph, scheme, DCTERMS.hasVersion)
               if list(graph.objects(scheme, DCTERMS.hasVersion)) else None)
    if not str(scheme).endswith('/scheme'):
        raise ValueError('Unexpected concept scheme IRI')
    base = str(scheme)[:-len('scheme')]
    depth_predicate = URIRef(base + 'annotationDepth')
    memberships: dict[URIRef, URIRef] = {}
    facets = []
    for collection in collections:
        label = _one_literal(graph, collection, SKOS.prefLabel, 'en')
        local = str(collection)
        if not local.startswith(base + 'facet/'):
            raise ValueError('Unexpected facet IRI')
        local = local[len(base + 'facet/'):]
        anchor = _anchor('facet', local)
        members = set(graph.objects(collection, SKOS.member))
        if not members or not members <= concepts:
            raise ValueError('Facet has zero or unknown member concepts')
        for concept in members:
            if concept in memberships:
                raise ValueError('A concept belongs to multiple facet collections')
            memberships[concept] = collection
        facets.append((label, local, anchor, collection))
    if set(memberships) != concepts:
        raise ValueError('Facet membership does not cover all concepts')
    facets.sort(key=lambda item: (item[0].casefold(), item[1]))
    details = {}
    identifiers = set()
    for concept in concepts:
        notation = _one_literal(graph, concept, SKOS.notation)
        if not notation.startswith('revmeta:'):
            raise ValueError('Unexpected notation CURIE')
        local = notation[len('revmeta:'):]
        if str(concept) != base + local:
            raise ValueError('Concept IRI does not match its notation')
        anchor = _anchor('concept', local)
        if anchor in identifiers:
            raise ValueError('Duplicate HTML concept anchor')
        identifiers.add(anchor)
        if set(graph.objects(concept, SKOS.inScheme)) != {scheme}:
            raise ValueError('Concept missing unique scheme membership')
        label = _one_literal(graph, concept, SKOS.prefLabel, 'en')
        definition = _one_literal(graph, concept, SKOS.definition, 'en')
        depth = _one_literal(graph, concept, depth_predicate)
        if depth not in {'CORE_FACET', 'OPTIONAL_DETAIL', 'REVIEW'}:
            raise ValueError('Unknown source annotation depth')
        guides = []
        for heading, role in SECTION_PREDICATES:
            entries = []
            for item in graph.objects(concept, URIRef(base + role)):
                index = int(_one_literal(graph, item, URIRef(base + 'itemIndex')))
                line_number = int(_one_literal(graph, item, URIRef(base + 'sourceLine')))
                content = _one_literal(graph, item, RDF.value, 'en')
                entries.append((index, content, line_number))
            if entries:
                entries.sort()
                if [entry[0] for entry in entries] != list(range(1, len(entries) + 1)):
                    raise ValueError(f'Nonconsecutive Codebook item order for {notation} {role}')
            guides.append((heading, entries))
        if any(entries for _, entries in guides) and not all(entries for _, entries in guides):
            raise ValueError(f'Incomplete Codebook RDF guidance for {notation}')
        details[concept] = (label, notation, definition, depth, anchor, guides)

    stylesheet = (
        'html{scroll-behavior:smooth}body{font:16px/1.6 system-ui,Arial,sans-serif;'
        'max-width:1100px;margin:auto;padding:1.5rem;color:#202735;background:#fff}'
        'a{color:#175a8e}a:focus-visible{outline:3px solid #e3a328;outline-offset:3px}'
        'header{border-bottom:2px solid #d9e2eb;margin-bottom:1.5rem}'
        '.notice{background:#fff4dd;padding:.8rem 1rem;border-left:4px solid #9b6700}'
        '.guidance{margin-top:1rem;padding-left:1rem;border-left:2px solid #e0e5eb}'
        '.guidance h4{margin:.8rem 0 .2rem}.guidance ol{margin-top:.2rem}'
        'nav ol{columns:2;column-gap:2rem;padding-left:1.5rem}'
        'section{margin:2.5rem 0}article{border-top:1px solid #d9e2eb;padding:1rem 0}'
        'article h3{margin:0}.meta{color:#4d5665;font-size:.94rem}'
        'code{overflow-wrap:anywhere}p{max-width:85ch}'
        '@media(max-width:650px){nav ol{columns:1}body{padding:1rem}}'
    )
    out = [
        '<!doctype html>', '<html lang="en">', '<head>', '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<title>RevMeta — SKOS vocabulary</title>',
        '<style>' + stylesheet + '</style>', '</head>', '<body>',
        '<header><h1>RevMeta — Review Metadata</h1>',
        ('<p class="meta">Resource version: <code>' + escape(version) + '</code></p>'
         if version is not None else ''),
        '<p>SKOS vocabulary: 102 concepts in 14 facet collections, '
        'with source-derived coding instructions.</p>',
        '<p class="notice"><strong>License and identifiers.</strong> '
        'RevMeta project-owned content is licensed under Apache-2.0. '
        'Publication status and persistent identifier resolution are determined by the '
        'public repository release and registered redirects, not by this generated page. '
        'No independent scientific validation is implied.</p>',
        '<p>Files: <a href="vocabulary.ttl">Turtle</a> · '
        '<a href="vocabulary.jsonld">JSON-LD</a> · '
        '<a href="mappings.sssom.tsv">SSSOM mappings</a> · '
        '<a href="mappings.sssom.ttl">SSSOM/RDF records</a> · '
        '<a href="decision-states.ttl">Decision states</a> · '
        '<a href="alignments.ttl">RDF alignments</a> · '
        '<a href="manifest.json">Build manifest</a></p></header>',
        '<nav aria-label="Facet navigation"><h2>Facets</h2><ol>',
    ]
    for label, _, anchor, collection in facets:
        count = len(set(graph.objects(collection, SKOS.member)))
        out.append(f'<li><a href="#{anchor}">{escape(label)}</a> ({count})</li>')
    out.extend(['</ol></nav>', '<main id="main">'])
    for label, _, anchor, collection in facets:
        out.append(f'<section id="{anchor}" aria-labelledby="{anchor}-title">')
        out.append(f'<h2 id="{anchor}-title">{escape(label)}</h2>')
        facet_definition = list(graph.objects(collection, SKOS.definition))
        facet_boundary = list(graph.objects(collection, SKOS.scopeNote))
        if facet_definition:
            if len(facet_definition) != 1 or len(facet_boundary) != 1:
                raise ValueError(f'Incomplete RDF facet guidance for {label}')
            out.append(f'<p>{escape(str(facet_definition[0]))}</p>')
            out.append(f'<p><strong>Facet boundary:</strong> '
                       f'{escape(str(facet_boundary[0]))}</p>')
        members = sorted(set(graph.objects(collection, SKOS.member)),
                         key=lambda term: (details[term][0].casefold(), details[term][1]))
        for concept in members:
            term_label, notation, definition, depth, term_anchor, guides = details[concept]
            out.append(f'<article id="{term_anchor}">')
            out.append(f'<h3><a href="#{term_anchor}">{escape(term_label)}</a></h3>')
            out.append(f'<p class="meta"><code>{escape(notation)}</code> · '
                       f'Annotation depth: <code>{escape(depth)}</code></p>')
            out.append(f'<p>{escape(definition)}</p>')
            if any(entries for _, entries in guides):
                out.append('<div class="guidance" aria-label="Source Codebook guidance">')
                for heading, entries in guides:
                    out.append(f'<h4>{escape(heading)}</h4><ol>')
                    for _, content, _ in entries:
                        out.append(f'<li>{escape(content)}</li>')
                    out.append('</ol>')
                out.append('</div>')
            out.append('</article>')
        out.append('</section>')
    out.extend(['</main>', '<footer><p>Generated from the SKOS Turtle graph. '
                'Facet groups are SKOS collections, not inferred OWL properties.</p>'
                '</footer>', '</body>', '</html>', ''])
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text('\n'.join(out), encoding='utf-8')
    return destination
