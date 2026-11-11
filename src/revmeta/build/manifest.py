"""Stable SHA-256 source/output manifest; never asserts publication approval."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
from revmeta.paths import project_version


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_manifest(inputs: dict[str, Path], outputs: list[Path], destination: Path,
                   version_path: Path | None = None) -> Path:
    allowed = {'registry', 'codebook', 'mappings'}
    if not set(inputs) <= allowed or len(inputs) != len(set(inputs)):
        raise ValueError('Unknown or duplicate logical source identifier')
    complete = set(inputs) == allowed and all(path.is_file() for path in inputs.values())
    sources = {identifier: _sha(path) for identifier, path in inputs.items()
               if path.is_file()}
    generated = {p.name: _sha(p) for p in outputs if p.is_file()}
    payload = {
        'project': 'RevMeta',
        'version': version_path.read_text(encoding='utf-8').strip() if version_path is not None else project_version(),
        'status': 'build-output',
        'inputs_complete': complete,
        'source_sha256': dict(sorted(sources.items())),
        'source_identity_scheme': 'logical-id-v1',
        'output_sha256': dict(sorted(generated.items())),
    }
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(payload, ensure_ascii=False, sort_keys=True, indent=2) + '\n',
                           encoding='utf-8')
    return destination
