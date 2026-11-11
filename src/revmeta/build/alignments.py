"""Export only confirmed SKOS links from the reviewed SSSOM mapping rows."""
from __future__ import annotations
from pathlib import Path
from rdflib import Graph, URIRef
from .mappings import CURIE_MAP


def expand_curie(value: str) -> URIRef:
    prefix, sep, local = value.partition(':')
    if not sep or prefix not in CURIE_MAP or not local:
        raise ValueError(f'Unknown or incomplete CURIE: {value!r}')
    return URIRef(CURIE_MAP[prefix] + local)


def build_alignment_graph(rows: list[dict[str, str]]) -> Graph:
    graph = Graph()
    for row in rows:
        if row['object_id'] == 'sssom:NoTermFound':
            continue
        graph.add((expand_curie(row['subject_id']), expand_curie(row['predicate_id']),
                   expand_curie(row['object_id'])))
    if len(graph) != 107:
        raise ValueError(f'Expected 107 unique concrete alignments, got {len(graph)}')
    return graph


def write_alignments(rows: list[dict[str, str]], output: Path) -> Path:
    graph = build_alignment_graph(rows)
    output.parent.mkdir(parents=True, exist_ok=True)
    # N-Triples is valid Turtle. Sort explicitly to guarantee stable bytes.
    triples = sorted(f'<{s}> <{p}> <{o}> .' for s, p, o in graph)
    output.write_text(
        '# RevMeta reviewed concrete alignments; NoTermFound appears only in SSSOM.\n'
        + '\n'.join(triples) + '\n', encoding='utf-8'
    )
    parsed = Graph().parse(output, format='turtle')
    if not parsed.isomorphic(graph):
        raise AssertionError('Alignment RDF export changed the graph')
    return output
