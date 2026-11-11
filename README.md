# RevMeta — Review Metadata

RevMeta is a controlled vocabulary and mapping resource for describing research review publications. It provides **102 SKOS concepts** grouped into **14 facets**, **691 Codebook guidance items**, and **141 reviewed SSSOM mapping decisions**: 107 links to external terms and 34 `NoTermFound` outcomes. A `NoTermFound` outcome indicates that no suitable counterpart was identified in the vocabularies examined; it does not imply that no equivalent exists elsewhere.

## Explore RevMeta

- [Browse the vocabulary](https://mmarcinmichal.github.io/revmeta/) — definitions and structured HTML documentation.
- [User guide](docs/user/README.md) — concept definitions, coding guidance, decision states, mapping provenance, and illustrations.
- [Source data](resources/inputs/vocabulary/) — the registry, Codebook, and reviewed mapping table.
- [RDF and SSSOM exports](resources/outputs/vocabulary/) — Turtle, JSON-LD, SSSOM TSV/Turtle, alignments, decision states, and the [SHA-256 manifest](resources/outputs/vocabulary/manifest.json).

## Reproducibility

The vocabulary and its exports can be regenerated from the included source data using Python 3.12 or later:

```bash
python -m pip install -e ".[validation]"
python -m revmeta build --require-complete
```

Generated files and their checksums are listed in [`manifest.json`](resources/outputs/vocabulary/manifest.json).

## License and citation

RevMeta project-owned content is available under the [Apache License 2.0](LICENSE). See [`CITATION.cff`](CITATION.cff) for citation metadata.

The RDF uses `https://w3id.org/revmeta/` as its identifier namespace. HTTP resolution through W3ID is not yet available.
