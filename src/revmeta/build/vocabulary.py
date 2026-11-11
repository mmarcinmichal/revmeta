"""Generate a conservative SKOS representation of the frozen RevMeta registry.

This module deliberately DOES NOT create OWL classes, OWL properties,
subclass assertions or inferred semantic relationships. Facets are SKOS
collections; concepts retain their full originally approved local names.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from rdflib import Graph, Literal, Namespace, RDF, RDFS, URIRef
from rdflib.namespace import DCTERMS, SKOS, XSD

from .codebook import Codebook, SECTION_PREDICATES, check_registry_parity, parse_codebook
from revmeta.paths import project_version

BASE = 'https://w3id.org/revmeta/'  # Proposed canonical IRI, registration pending.
LICENSE_URI = 'https://www.apache.org/licenses/LICENSE-2.0'
REV = Namespace(BASE)
SCHEME = REV['scheme']
PREFIXES = {'dcterms': str(DCTERMS), 'rdf': str(RDF), 'rdfs': str(RDFS),
            'revmeta': BASE, 'skos': str(SKOS), 'xsd': str(XSD)}
DEPTHS = {'CORE_FACET', 'OPTIONAL_DETAIL', 'REVIEW'}


def registry_graph(registry: dict, base: str = BASE, *,
                   codebook: Codebook | None = None,
                   version: str | None = None,
                   source_sha256: dict[str, str] | None = None) -> Graph:
    terms = registry.get('terms')
    if not isinstance(terms, list) or len(terms) != 102:
        raise ValueError('Expected exactly 102 RevMeta terms')
    if registry.get('inference_rules') != 'NONE: no inferred subtypes, equivalences, disjointness or closed-world negatives':
        raise ValueError('Unknown or altered frozen inference rules')
    root = Namespace(base)
    scheme = root['scheme']
    graph = Graph()
    for prefix, iri in PREFIXES.items():
        graph.bind(prefix, base if prefix == 'revmeta' else iri, override=True)
    graph.add((scheme, RDF.type, SKOS.ConceptScheme))
    graph.add((scheme, SKOS.prefLabel, Literal('RevMeta — Review Metadata', lang='en')))
    graph.add((scheme, DCTERMS.license, URIRef(LICENSE_URI)))
    if version:
        graph.add((scheme, DCTERMS.hasVersion, Literal(version)))
        graph.add((scheme, DCTERMS.description, Literal(
            'Machine-readable RevMeta methodological vocabulary and source-derived '
            'coding instructions; unpublished development preview.', lang='en')))
        graph.add((scheme, DCTERMS.provenance, Literal(
            'RevMeta source revision 2 uses current identifiers; archived predecessor '
            'materials remain in private provenance records.',
            lang='en')))
    if source_sha256:
        allowed = {'registry', 'codebook', 'mappings'}
        if not set(source_sha256) <= allowed:
            raise ValueError('Unexpected source included in vocabulary provenance')
        graph.add((root['sha256'], RDF.type, RDF.Property))
        graph.add((root['sha256'], RDFS.comment,
                   Literal('SHA-256 digest of the exact frozen source file bytes.', lang='en')))
        for logical_id, digest in sorted(source_sha256.items()):
            if len(digest) != 64 or any(c not in '0123456789abcdef' for c in digest):
                raise ValueError('Invalid source SHA-256 for ' + logical_id)
            source_id = root['source/' + logical_id]
            graph.add((scheme, DCTERMS.source, source_id))
            graph.add((source_id, DCTERMS.identifier, Literal(logical_id)))
            graph.add((source_id, root['sha256'], Literal(digest)))
    if codebook is not None:
        check_registry_parity(codebook, registry)
        graph.add((root['CodingGuidanceItem'], RDF.type, RDFS.Class))
        graph.add((root['CodingGuidanceItem'], RDFS.comment, Literal(
            'One verbatim source Codebook bullet, with role and original ordering.',
            lang='en')))
        for original_title, predicate_name in SECTION_PREDICATES:
            prop_iri = root[predicate_name]
            graph.add((prop_iri, RDF.type, RDF.Property))
            graph.add((prop_iri, RDFS.label, Literal(original_title, lang='en')))
            graph.add((prop_iri, RDFS.comment, Literal(
                'Links a RevMeta term to ordered Codebook guidance items '
                'in this exact category; not an OWL inference rule.', lang='en')))
        for p, comment in (
            ('itemIndex', '1-based position of this statement within its coding category.'),
            ('sourceLine', '1-based line number in the frozen Codebook Markdown source.'),
        ):
            graph.add((root[p], RDF.type, RDF.Property))
            graph.add((root[p], RDFS.comment, Literal(comment, lang='en')))
    graph.add((root['annotationDepth'], RDF.type, RDF.Property))
    graph.add((root['annotationDepth'], RDFS.comment,
               Literal('Source registry depth marker; not an ontology class or inference axiom.', lang='en')))
    facets = {}
    visited = set()
    for entry in terms:
        term = entry.get('term')
        prop = entry.get('property')
        label = entry.get('label')
        definition = entry.get('definition')
        depth = entry.get('depth')
        if (not isinstance(term, str) or not term.startswith('revmeta:') or
                not isinstance(prop, str) or not prop.startswith('revmeta:') or
                not term.startswith(prop + '.')):
            raise ValueError(f'Invalid term/facet CURIE: {term!r} {prop!r}')
        if not label or not definition or depth not in DEPTHS or term in visited:
            raise ValueError(f'Missing/duplicated/invalid term fields: {term!r}')
        visited.add(term)
        local = term[len('revmeta:'):]
        facet_local = prop[len('revmeta:'):]
        concept = root[local]
        coll = root['facet/' + facet_local]
        facets[prop] = coll
        graph.add((concept, RDF.type, SKOS.Concept))
        graph.add((concept, SKOS.inScheme, scheme))
        graph.add((concept, SKOS.prefLabel, Literal(label, lang='en')))
        graph.add((concept, SKOS.definition, Literal(definition, lang='en')))
        graph.add((concept, SKOS.notation, Literal(term)))
        graph.add((concept, root['annotationDepth'], Literal(depth)))
        graph.add((coll, SKOS.member, concept))
        if codebook is not None:
            guidance = codebook.terms[term]
            for _, predicate_name in SECTION_PREDICATES:
                for item in guidance.sections[predicate_name]:
                    # Stable structural IRI; no blank-node instability or lost order.
                    item_iri = root[f'guidance/{local}/{predicate_name}/{item.ordinal:03d}']
                    graph.add((concept, root[predicate_name], item_iri))
                    graph.add((item_iri, RDF.type, root['CodingGuidanceItem']))
                    graph.add((item_iri, RDF.value, Literal(item.text, lang='en')))
                    graph.add((item_iri, root['itemIndex'],
                               Literal(item.ordinal, datatype=XSD.integer)))
                    graph.add((item_iri, root['sourceLine'],
                               Literal(item.source_line, datatype=XSD.integer)))
    if len(facets) != 14:
        raise ValueError(f'Expected 14 facets, got {len(facets)}')
    for prop, coll in facets.items():
        graph.add((coll, RDF.type, SKOS.Collection))
        technical_label = prop[len('revmeta:'):]
        if codebook is not None:
            guide = codebook.facets[prop]
            graph.add((coll, SKOS.prefLabel, Literal(guide.label, lang='en')))
            graph.add((coll, SKOS.altLabel, Literal(technical_label, lang='en')))
            graph.add((coll, SKOS.notation, Literal(prop)))
            graph.add((coll, SKOS.definition, Literal(guide.definition, lang='en')))
            graph.add((coll, SKOS.scopeNote, Literal(guide.boundary, lang='en')))
            graph.add((coll, root['facetTier'], Literal(guide.tier)))
        else:
            graph.add((coll, SKOS.prefLabel, Literal(technical_label, lang='en')))
    if codebook is not None:
        graph.add((root['facetTier'], RDF.type, RDF.Property))
        graph.add((root['facetTier'], RDFS.comment, Literal(
            'Facet tier copied verbatim from the canonical Codebook.', lang='en')))
    return graph


def canonical_turtle(graph: Graph, base: str = BASE) -> str:
    """Emit deterministic valid Turtle (one triple per line)."""
    lines = [f'@prefix {p}: <{base if p == "revmeta" else iri}> .'
             for p, iri in sorted(PREFIXES.items())]
    rows = sorted(
        f'{s.n3(graph.namespace_manager)} {p.n3(graph.namespace_manager)} {o.n3(graph.namespace_manager)} .'
        for s, p, o in graph
    )
    return '\n'.join(lines + [''] + rows + [''])


def canonical_jsonld(graph: Graph) -> str:
    """Produce deterministic JSON-LD corresponding to the identical RDF graph."""
    doc = json.loads(graph.serialize(format='json-ld'))
    if not isinstance(doc, list):
        doc = [doc]
    for node in doc:
        for value in node.values():
            if isinstance(value, list):
                value.sort(key=lambda x: json.dumps(x, sort_keys=True, ensure_ascii=False))
    doc.sort(key=lambda x: x.get('@id', ''))
    return json.dumps(doc, ensure_ascii=False, indent=2, sort_keys=True) + '\n'


def build(registry_path: Path, out_dir: Path, base: str = BASE,
          codebook_path: Path | None = None,
          mappings_path: Path | None = None) -> tuple[Path, Path]:
    registry = json.loads(registry_path.read_text(encoding='utf-8'))
    source_guide = codebook_path or registry_path.with_name('codebook.md')
    if not source_guide.is_file():
        raise FileNotFoundError(f'Codebook is mandatory for complete RDF: {source_guide}')
    parsed = parse_codebook(source_guide)
    digest = hashlib.sha256(source_guide.read_bytes()).hexdigest()
    if registry.get('source_reference_sha256') != digest:
        raise ValueError('Registry does not reference the current Codebook SHA-256')
    if registry.get('source_reference_filename') != source_guide.name:
        raise ValueError('Registry Codebook filename mismatch')
    sources = (registry_path, source_guide,
               mappings_path if mappings_path is not None else registry_path.with_name('mappings.xlsx'))
    digests = {name: hashlib.sha256(path.read_bytes()).hexdigest()
               for name, path in zip(('registry', 'codebook', 'mappings'), sources)
               if path.is_file()}
    version = project_version()
    graph = registry_graph(registry, base, codebook=parsed, version=version,
                           source_sha256=digests)
    out_dir.mkdir(parents=True, exist_ok=True)
    ttl = out_dir / 'vocabulary.ttl'
    jsonld = out_dir / 'vocabulary.jsonld'
    ttl.write_text(canonical_turtle(graph, base), encoding='utf-8')
    jsonld.write_text(canonical_jsonld(graph), encoding='utf-8')
    a = Graph()
    a.parse(ttl, format='turtle')
    b = Graph()
    b.parse(jsonld, format='json-ld')
    if not graph.isomorphic(a) or not graph.isomorphic(b):
        raise AssertionError('Serialization changed RDF statements')
    return ttl, jsonld
