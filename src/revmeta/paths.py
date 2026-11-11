"""Repository data layout: file locations are separate from logical source identities.

All SHA-256 calculations use file *contents*; manifest keys are stable logical IDs.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESOURCES = ROOT / "resources"
VOCABULARY_INPUTS = RESOURCES / "inputs" / "vocabulary"
VOCABULARY_OUTPUTS = RESOURCES / "outputs" / "vocabulary"
ANALYSIS_OUTPUTS = RESOURCES / "outputs" / "analysis"
HISTORY = RESOURCES / "history"
SOURCE_FILENAMES = {
    "registry": "registry.json",
    "codebook": "codebook.md",
    "mappings": "mappings.xlsx",
}


def vocabulary_sources(root: Path = ROOT) -> dict[str, Path]:
    directory = root / "resources" / "inputs" / "vocabulary"
    return {identifier: directory / filename for identifier, filename in SOURCE_FILENAMES.items()}


def project_version() -> str:
    """Resolve the installed distribution version, including non-editable wheels."""
    from importlib.metadata import PackageNotFoundError, version
    try:
        found = version("revmeta")
    except PackageNotFoundError:
        version_file = ROOT / "VERSION"
        if not version_file.is_file():
            raise RuntimeError("RevMeta version unavailable; refusing unversioned build")
        found = version_file.read_text(encoding="utf-8").strip()
    if not found:
        raise RuntimeError("RevMeta version is empty")
    return found
