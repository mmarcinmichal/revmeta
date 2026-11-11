"""Strict, deterministic parser for the *frozen* RevMeta Codebook Markdown.

Every coding item is retained in its exact source order and wording. Unknown
source structure raises ValueError: never silently drop scientific guidance.
No private history, ZIP or network input is used by this portable parser.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
import re

SECTION_PREDICATES = (
    ("CODE WHEN", "codeWhen"),
    ("DO NOT CODE WHEN", "doNotCodeWhen"),
    ("Boundary notes", "boundaryNote"),
    ("Positive examples", "positiveExample"),
    ("Negative examples", "negativeExample"),
)
SECTION_NAMES = dict(SECTION_PREDICATES)
EXPECTED_COUNTS = {
    "codeWhen": 134,
    "doNotCodeWhen": 193,
    "boundaryNote": 155,
    "positiveExample": 104,
    "negativeExample": 105,
}

FACET_PATTERN = re.compile(r"^## (revmeta:[A-Za-z][A-Za-z0-9_]*) — (.+)$")
TERM_PATTERN = re.compile(r"^### \x60(revmeta:[A-Za-z][A-Za-z0-9_.]*)\x60 — (.+)$")
ATTRIBUTE = re.compile(r"^\*\*(Tier|Depth|Definition|Boundary):\*\* (.+?)\s*$")


@dataclass(frozen=True)
class CodingItem:
    text: str
    ordinal: int
    source_line: int


@dataclass
class TermGuide:
    identifier: str
    label: str
    depth: str = ""
    definition: str = ""
    sections: dict[str, list[CodingItem]] = field(
        default_factory=lambda: {name: [] for name in SECTION_NAMES.values()}
    )
    observed_sections: set[str] = field(default_factory=set)


@dataclass
class FacetGuide:
    identifier: str
    label: str
    tier: str = ""
    definition: str = ""
    boundary: str = ""
    term_ids: list[str] = field(default_factory=list)


@dataclass
class Codebook:
    facets: dict[str, FacetGuide]
    terms: dict[str, TermGuide]

    @property
    def rule_counts(self) -> dict[str, int]:
        return {
            role: sum(len(term.sections[role]) for term in self.terms.values())
            for role in SECTION_NAMES.values()
        }


def parse_codebook(source: Path | str) -> Codebook:
    """Parse source Markdown; reject all unexpected body content and omissions.

    A path is read as UTF-8. A string is the Markdown itself, not a path.
    The current RevMeta preamble is metadata, not a coding instruction.
    """
    raw = source.read_text(encoding="utf-8") if isinstance(source, Path) else source
    facets: dict[str, FacetGuide] = {}
    terms: dict[str, TermGuide] = {}
    facet: FacetGuide | None = None
    term: TermGuide | None = None
    section: str | None = None
    preamble_keys = ("# ", "Registry: ", "Checksums: ", "> Development-only")

    for line_number, original in enumerate(raw.splitlines(), start=1):
        line = original.strip()
        if not line:
            continue

        found = FACET_PATTERN.fullmatch(line)
        if found:
            identifier, label = found.groups()
            if identifier in facets:
                raise ValueError(f"Duplicate Codebook facet {identifier} at line {line_number}")
            facet = FacetGuide(identifier, label)
            facets[identifier] = facet
            term = None
            section = None
            continue

        found = TERM_PATTERN.fullmatch(line)
        if found:
            identifier, label = found.groups()
            if facet is None or not identifier.startswith(facet.identifier + "."):
                raise ValueError(f"Unmatched Codebook term {identifier} at line {line_number}")
            if identifier in terms:
                raise ValueError(f"Duplicate Codebook term {identifier} at line {line_number}")
            term = TermGuide(identifier, label)
            terms[identifier] = term
            facet.term_ids.append(identifier)
            section = None
            continue

        if facet is None:
            if line.startswith(preamble_keys):
                continue
            raise ValueError(f"Unexpected Codebook preamble line {line_number}: {line!r}")

        found = ATTRIBUTE.fullmatch(line)
        if found:
            field_name, value = found.groups()
            value = value.strip()
            if not value:
                raise ValueError(f"Blank Codebook {field_name} at line {line_number}")
            if term is None:
                attr = {"Tier": "tier", "Definition": "definition", "Boundary": "boundary"}.get(field_name)
            else:
                attr = {"Depth": "depth", "Definition": "definition"}.get(field_name)
            if attr is None:
                raise ValueError(f"Unexpected Codebook {field_name} at line {line_number}")
            owner = term if term is not None else facet
            if getattr(owner, attr):
                raise ValueError(f"Repeated Codebook {field_name} at line {line_number}")
            setattr(owner, attr, value.strip("\x60") if field_name in {"Tier", "Depth"} else value)
            section = None
            continue

        if line.startswith("**") and line.endswith("**"):
            heading = line[2:-2]
            if term is None or heading not in SECTION_NAMES:
                raise ValueError(f"Unknown Codebook section at line {line_number}: {line!r}")
            section = SECTION_NAMES[heading]
            if section in term.observed_sections:
                raise ValueError(f"Repeated Codebook section {heading} for {term.identifier}")
            term.observed_sections.add(section)
            continue

        if line.startswith("- "):
            if term is None or section is None:
                raise ValueError(f"Orphan Codebook bullet at line {line_number}")
            # Exactly preserve the content after the Markdown list marker.
            text = original[original.index("- ") + 2:]
            if not text.strip():
                raise ValueError(f"Blank Codebook bullet at line {line_number}")
            bucket = term.sections[section]
            bucket.append(CodingItem(text=text, ordinal=len(bucket) + 1,
                                     source_line=line_number))
            continue

        raise ValueError(f"Unrecognized Codebook content at line {line_number}: {line!r}")

    if len(facets) != 14 or len(terms) != 102:
        raise ValueError(f"Codebook must contain 14 facets and 102 terms, got {len(facets)} / {len(terms)}")
    for f in facets.values():
        if not f.label or not f.tier or not f.definition or not f.boundary or not f.term_ids:
            raise ValueError(f"Incomplete Codebook facet {f.identifier}")
    for t in terms.values():
        if not t.label or not t.depth or not t.definition:
            raise ValueError(f"Incomplete Codebook term {t.identifier}")
        if t.observed_sections != set(SECTION_NAMES.values()):
            raise ValueError(f"Missing Codebook sections for {t.identifier}")
        if any(not entries for entries in t.sections.values()):
            raise ValueError(f"Empty coding section in {t.identifier}")
    counts = Codebook(facets, terms).rule_counts
    if counts != EXPECTED_COUNTS:
        raise ValueError(f"Frozen Codebook item counts differ: {counts!r}")
    return Codebook(facets=facets, terms=terms)


def check_registry_parity(codebook: Codebook, registry: dict) -> None:
    """Fail closed if any term identifier, label, depth or definition drifts."""
    source_terms = registry.get("terms", [])
    expected_terms = {item["term"]: item for item in source_terms}
    expected_facets = {item["property"] for item in source_terms}
    if set(codebook.terms) != set(expected_terms):
        raise ValueError("Codebook and registry term identifier sets differ")
    if set(codebook.facets) != expected_facets:
        raise ValueError("Codebook and registry facet sets differ")
    for name, entry in expected_terms.items():
        guide = codebook.terms[name]
        for attr in ("label", "definition", "depth"):
            if getattr(guide, attr) != entry[attr]:
                raise ValueError(f"Codebook/registry {attr} mismatch for {name}")
    for facet in codebook.facets.values():
        if set(facet.term_ids) != {
            entry["term"] for entry in source_terms if entry["property"] == facet.identifier
        }:
            raise ValueError(f"Codebook facet membership mismatch: {facet.identifier}")
