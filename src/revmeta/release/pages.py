"""Offline GitHub Pages preview and W3ID redirect draft; never deploy.

Only the already validated eight-file vocabulary build is staged. The W3ID
rules are a reviewable draft, not registered redirects or a release.
"""
from __future__ import annotations

import argparse
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import shutil
import tempfile

from rdflib import Graph, RDF, URIRef
from rdflib.namespace import SKOS

from revmeta.paths import ROOT, VOCABULARY_INPUTS, VOCABULARY_OUTPUTS
from revmeta.release.w3id import BASE, PAGES_BASE, render_w3id_draft

FILES = frozenset({
    "index.html", "vocabulary.ttl", "vocabulary.jsonld",
    "mappings.sssom.tsv", "mappings.sssom.ttl", "alignments.ttl",
    "decision-states.ttl", "manifest.json",
})
INPUTS = {"registry": "registry.json", "codebook": "codebook.md", "mappings": "mappings.xlsx"}


class Anchors(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name == "id" and value is not None:
                self.ids.append(value)


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verified_graph(source: Path, inputs: Path = VOCABULARY_INPUTS) -> Graph:
    """Reject partial, tampered or noncanonical outputs before staging."""
    if source.is_symlink() or not source.is_dir():
        raise ValueError("Missing or symlinked vocabulary output directory")
    names = {p.name for p in source.iterdir()}
    if names != FILES:
        raise ValueError(f"Expected exactly eight vocabulary files: {names ^ FILES}")
    if any((source / name).is_symlink() or not (source / name).is_file() for name in FILES):
        raise ValueError("Nonregular or symlinked vocabulary file")
    manifest = json.loads((source / "manifest.json").read_text(encoding="utf-8"))
    if manifest.get("inputs_complete") is not True:
        raise ValueError("Cannot stage a partial vocabulary")
    if manifest.get("source_identity_scheme") != "logical-id-v1":
        raise ValueError("Unexpected source identity scheme")
    if set(manifest.get("source_sha256", {})) != set(INPUTS):
        raise ValueError("Incomplete source checksum list")
    if set(manifest.get("output_sha256", {})) != FILES - {"manifest.json"}:
        raise ValueError("Invalid output manifest file list")
    for name, digest in manifest["output_sha256"].items():
        if _sha(source / name) != digest:
            raise ValueError(f"Output checksum mismatch: {name}")
    for name, filename in INPUTS.items():
        path = inputs / filename
        if not path.is_file() or path.is_symlink() or _sha(path) != manifest["source_sha256"][name]:
            raise ValueError(f"Canonical input SHA-256 mismatch: {name}")
    graph = Graph().parse(source / "vocabulary.ttl", format="turtle")
    jsonld = Graph().parse(source / "vocabulary.jsonld", format="json-ld")
    if not graph.isomorphic(jsonld):
        raise ValueError("Turtle/JSON-LD graph mismatch")
    concepts = set(graph.subjects(RDF.type, SKOS.Concept))
    facets = set(graph.subjects(RDF.type, SKOS.Collection))
    schemes = set(graph.subjects(RDF.type, SKOS.ConceptScheme))
    if (len(concepts), len(facets), schemes) != (102, 14, {URIRef(BASE + "scheme")}):
        raise ValueError("Unexpected scheme or 102/14 cardinalities")
    anchors = Anchors()
    anchors.feed((source / "index.html").read_text(encoding="utf-8"))
    if len(anchors.ids) != len(set(anchors.ids)):
        raise ValueError("Duplicate HTML anchor")
    expected = {"concept-" + str(c)[len(BASE):] for c in concepts}
    expected |= {"facet-" + str(f)[len(BASE + "facet/"):] for f in facets}
    if any(not str(c).startswith(BASE) for c in concepts) or any(
            not str(f).startswith(BASE + "facet/") for f in facets):
        raise ValueError("Unexpected RevMeta URI")
    if not expected <= set(anchors.ids):
        raise ValueError("Missing HTML concept/facet anchors")
    return graph



def prepare(source: Path, destination: Path, *, inputs: Path = VOCABULARY_INPUTS,
            w3id_draft: Path | None = None) -> Path:
    destination = destination.resolve()
    if destination == ROOT or destination.is_relative_to(ROOT):
        raise ValueError("Pages preview destination must be outside repository")
    if destination.exists():
        raise ValueError("Pages preview destination must not already exist")
    if w3id_draft is not None:
        proposed = w3id_draft.resolve()
        if proposed == destination or proposed.is_relative_to(destination):
            raise ValueError("W3ID draft cannot be placed inside published Pages site")
        if w3id_draft.exists():
            raise ValueError("W3ID draft destination must not already exist")
    graph = verified_graph(source, inputs)
    with tempfile.TemporaryDirectory(prefix="revmeta-pages-") as temporary:
        staged = Path(temporary) / "site"
        staged.mkdir()
        for name in sorted(FILES):
            shutil.copyfile(source / name, staged / name)
        (staged / ".nojekyll").write_bytes(b"")
        if {p.name for p in staged.iterdir()} != FILES | {".nojekyll"}:
            raise ValueError("Unexpected Pages site file")
        shutil.copytree(staged, destination)
    if w3id_draft is not None:
        w3id_draft.parent.mkdir(parents=True, exist_ok=True)
        w3id_draft.write_text(render_w3id_draft(graph), encoding="utf-8")
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description="Build OFFLINE Pages and W3ID drafts (no publishing)")
    parser.add_argument("--source", type=Path, default=VOCABULARY_OUTPUTS)
    parser.add_argument("--inputs", type=Path, default=VOCABULARY_INPUTS)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--w3id-draft", type=Path)
    args = parser.parse_args()
    try:
        output = prepare(args.source, args.output, inputs=args.inputs, w3id_draft=args.w3id_draft)
    except (ValueError, OSError) as exc:
        parser.exit(1, f"BLOCKED: Pages preview not prepared: {exc}\n")
    print(f"Offline Pages preview: {output}; no publishing or registration")


if __name__ == "__main__":
    main()
