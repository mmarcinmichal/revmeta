# RevMeta — Review Metadata

RevMeta is a versioned, self-contained SKOS vocabulary and SSSOM mapping resource
for describing research review publications. This source package contains
102 concepts in 14 facet collections, 691 Codebook guidance items and
141 reviewed mapping decisions (107 concrete external links and 34 bounded
NoTermFound outcomes). The 34 negative decisions describe the default
external vocabulary families considered in RevMeta; they do not prove
universal nonexistence of equivalents.

## Build and provenance

This repository content is derived from a private validated source snapshot
using an explicit file allowlist. The three authoritative scientific inputs
are preserved in resources/inputs/vocabulary/. The eight reproducible output
files, including their content-hash manifest, are in resources/outputs/vocabulary/.
The manifest describes a deterministic build, **not** whether its owner
authorized publication. Only a specific public GitHub tag/Release, after the
owner's explicit approval, establishes release status for that commit.

Project-owned content is licensed under Apache-2.0 (LICENSE).
The confirmed resource author and current baseline version are in CITATION.cff.
Do not invent a DOI or public release date from the build manifest.

For independent rebuild instructions, Codebook rules, decision states,
mapping provenance and illustrations see the
[RevMeta user guide](docs/user/README.md).
Browsable generated HTML is at
[resources/outputs/vocabulary/index.html](resources/outputs/vocabulary/index.html).

## Identifier and release scope

The base IRI https://w3id.org/revmeta/ is a proposed stable identifier.
Actual registration, redirect resolution, content negotiation and the published
version must be checked against the *live* W3ID registry and public release.
This README alone does not authorize publishing, DOI deposition or W3ID changes.
