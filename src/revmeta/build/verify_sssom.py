"""Independent checks for SSSOM TSV, mapping-set RDF and sssom-py RDF replay.

Runs after 'sssom parse -I rdf' and compares full mapping-record multisets
after CURIE expansion. Explicitly checks the mandatory license because
sssom-py 0.4.21's schema validator does not enforce it.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from pathlib import Path

from rdflib import Graph, Namespace, URIRef
from rdflib.namespace import DCTERMS, OWL, RDFS

LICENSE = "https://www.apache.org/licenses/LICENSE-2.0"
MAPPING_SET = URIRef("https://w3id.org/revmeta/mappings")
SSSOM = Namespace("https://w3id.org/sssom/")
IRI_FIELDS = ("subject_id", "predicate_id", "object_id", "mapping_justification")
PLAIN_FIELDS = ("subject_label", "object_label", "comment")
REQUIRED_COLS = set(IRI_FIELDS + PLAIN_FIELDS + ("reviewer_label",))


def read_tsv(path: Path) -> tuple[dict[str, str], dict[str, str], list[dict[str, str]]]:
    """Read standardized SSSOM metadata and all mapping rows."""
    meta: dict[str, str] = {}
    prefixes: dict[str, str] = {}
    body = []
    for line in path.read_text(encoding="utf-8").splitlines(keepends=True):
        if line.startswith("#   ") and ": " in line:
            prefix, iri = line[4:].strip().split(": ", 1)
            prefixes[prefix] = iri.strip()
        elif line.startswith("# ") and ": " in line:
            key, value = line[2:].strip().split(": ", 1)
            meta[key] = value.strip()
        elif not line.startswith("#"):
            body.append(line)
    reader = csv.DictReader(body, delimiter="\t")
    if not reader.fieldnames or not REQUIRED_COLS <= set(reader.fieldnames):
        raise ValueError(f"Missing SSSOM mapping fields in {path}")
    rows = list(reader)
    if any(None in record or any(value is None for value in record.values()) for record in rows):
        raise ValueError("Invalid SSSOM tabular row length")
    return meta, prefixes, rows


def expand(value: str, prefixes: dict[str, str]) -> str:
    if value.startswith(("http://", "https://")):
        return value
    if ":" not in value:
        raise ValueError("Missing CURIE prefix in IRI: " + value)
    prefix, local = value.split(":", 1)
    if prefix not in prefixes:
        raise ValueError("Unrecognized CURIE prefix: " + prefix)
    return prefixes[prefix] + local


def reviewers(value: str) -> tuple[str, ...]:
    return tuple(sorted(piece for piece in value.split("|") if piece))


def normalized_tuple(row: dict[str, str], prefixes: dict[str, str]) -> tuple:
    return (
        *(expand(row[key], prefixes) for key in IRI_FIELDS),
        *(row.get(key, "") for key in PLAIN_FIELDS),
        reviewers(row.get("reviewer_label", "")),
    )


def verify(tsv: Path, rdf: Path, replay: Path) -> dict[str, int]:
    metadata, prefixes, original = read_tsv(tsv)
    reparse_meta, reparse_prefixes, replayed = read_tsv(replay)
    if metadata.get("license") != LICENSE:
        raise ValueError("Missing/wrong mandatory SSSOM TSV license")
    if reparse_meta.get("license") != LICENSE:
        raise ValueError("SSSOM RDF replay lost mandatory license metadata")

    if len(original) != 141 or len(replayed) != 141:
        raise ValueError("SSSOM must have exactly 141 records")
    if sum(row.get("comment", "") != "" for row in original) != 90:
        raise ValueError("Original SSSOM is missing 90 mapping comments")
    if sum(expand(row["object_id"], prefixes) == str(SSSOM.NoTermFound)
           for row in original) != 34:
        raise ValueError("SSSOM must preserve 34 NoTermFound sentinels")

    full_map = {**prefixes, **reparse_prefixes}
    expected = Counter(normalized_tuple(row, full_map) for row in original)
    got = Counter(normalized_tuple(row, full_map) for row in replayed)
    if expected != got:
        raise ValueError("SSSOM RDF replay changed full mapping tuples")

    graph = Graph().parse(rdf, format="turtle")
    license_objects = set(graph.objects(MAPPING_SET, DCTERMS.license))
    if license_objects != {URIRef(LICENSE)}:
        raise ValueError("Missing/wrong dcterms:license on MappingSet RDF")
    if any(graph.triples((None, SSSOM.comment, None))):
        raise ValueError("SSSOM mapping comment must use rdfs:comment")

    nodes = list(graph.objects(MAPPING_SET, SSSOM.mappings))
    if len(nodes) != 141 or len(set(nodes)) != 141:
        raise ValueError("RDF mapping records missing or duplicated")
    if sum(1 for n in nodes if graph.value(n, RDFS.comment) is not None) != 90:
        raise ValueError("RDF lost one or more rdfs:comment values")

    # This more stringent RDF check also covers mapping_tool; sssom-py
    # may promote that field to MappingSet metadata during RDF -> TSV.
    tools_in_tsv = {row["mapping_tool"] for row in original}
    if len(tools_in_tsv) != 1:
        raise ValueError("Multiple mapping tools need an explicit per-row replay policy")
    expected_rdf = Counter((
        expand(row["subject_id"], prefixes),
        expand(row["predicate_id"], prefixes),
        expand(row["object_id"], prefixes),
        row.get("subject_label", ""),
        row.get("object_label", ""),
        expand(row["mapping_justification"], prefixes),
        reviewers(row.get("reviewer_label", "")),
        row.get("comment", ""),
        row["mapping_tool"],
    ) for row in original)
    rdf_tuples = Counter()
    for node in nodes:
        def text(predicate):
            value = graph.value(node, predicate)
            return str(value) if value is not None else ""
        rdf_tuples[(
            text(OWL.annotatedSource), text(OWL.annotatedProperty),
            text(OWL.annotatedTarget), text(SSSOM.subject_label),
            text(SSSOM.object_label), text(SSSOM.mapping_justification),
            tuple(sorted(str(v) for v in graph.objects(node, SSSOM.reviewer_label))),
            text(RDFS.comment), text(SSSOM.mapping_tool),
        )] += 1
    if expected_rdf != rdf_tuples:
        raise ValueError("SSSOM RDF records differ from the full TSV mapping tuples")

    return {"mapping_records": 141, "no_term_found": 34, "comments": 90}


def main() -> None:
    parser = argparse.ArgumentParser(description="Check complete SSSOM TSV <-> RDF replay and license")
    parser.add_argument("--tsv", type=Path, required=True)
    parser.add_argument("--rdf", type=Path, required=True)
    parser.add_argument("--replayed", type=Path, required=True)
    args = parser.parse_args()
    print("PASS SSSOM independent cross-check:", verify(args.tsv, args.rdf, args.replayed))


if __name__ == "__main__":
    main()
