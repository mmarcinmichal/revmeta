"""Build a self-contained, offline RevMeta PUBLIC-CANDIDATE directory.

This is deliberately not a publication command: no GitHub writes, tags,
network calls, Pages deployment, DOI actions or release authorization.
Private history and development records are never copied.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

from revmeta.paths import ROOT, VOCABULARY_OUTPUTS

# Deliberately explicit: adding a private repository file does not silently
# add it to the public candidate. This set is reviewed when changing the build.
ALLOWLIST = (
    "VERSION", "LICENSE", "CITATION.cff", "pyproject.toml",
    "resources/inputs/vocabulary/registry.json",
    "resources/inputs/vocabulary/codebook.md",
    "resources/inputs/vocabulary/mappings.xlsx",
    "src/revmeta/__init__.py", "src/revmeta/__main__.py",
    "src/revmeta/cli.py", "src/revmeta/paths.py",
    "src/revmeta/build/__init__.py", "src/revmeta/build/cli.py",
    "src/revmeta/build/vocabulary.py", "src/revmeta/build/codebook.py",
    "src/revmeta/build/manifest.py", "src/revmeta/build/mappings.py",
    "src/revmeta/build/alignments.py", "src/revmeta/build/sssom_rdf.py",
    "src/revmeta/build/decision_states.py", "src/revmeta/build/html_docs.py",
    "src/revmeta/build/verify_sssom.py",
    "src/revmeta/release/__init__.py", "src/revmeta/release/__main__.py",
    "src/revmeta/release/cli.py", "src/revmeta/release/candidate.py",
    "src/revmeta/release/pages.py", "src/revmeta/release/w3id.py",
    "src/revmeta/build/shapes/vocabulary.shacl.ttl",
    "tests/__init__.py", "tests/build/__init__.py",
    "tests/build/test_codebook.py", "tests/build/test_codebook_rdf.py",
    "tests/build/test_user_guide.py", "tests/build/test_source_identity.py",
    "tests/build/test_manifest.py", "tests/build/test_mappings.py",
    "tests/build/test_sssom_rdf.py", "tests/build/test_decision_states.py",
    "tests/build/test_vocabulary.py", "tests/build/test_html_docs.py",
    "tests/build/sssom_fixture.py",
    "docs/user/README.md", "docs/user/assets/revmeta-artifacts.svg",
    "docs/user/assets/revmeta-teaser.svg",
    "docs/user/assets/revmeta-teaser-paper.svg",
)
GENERATED_FILES = frozenset({
    'index.html', 'vocabulary.ttl', 'vocabulary.jsonld',
    'mappings.sssom.tsv', 'mappings.sssom.ttl', 'alignments.ttl', 'decision-states.ttl', 'manifest.json',
})
PUBLIC_README = """# RevMeta — Review Metadata

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
"""


def check_destination(destination: Path) -> Path:
    resolved = destination.resolve()
    if resolved == ROOT or resolved.is_relative_to(ROOT):
        raise ValueError('Staging destination must be outside the private repository')
    if destination.exists() or destination.is_symlink():
        raise ValueError('Staging destination must not already exist')
    return resolved


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _run(command: list[str], cwd: Path, env: dict[str, str] | None = None) -> None:
    # Do not contaminate the audited candidate with interpreter bytecode caches.
    environment = os.environ.copy()
    if env is not None:
        environment.update(env)
    environment['PYTHONDONTWRITEBYTECODE'] = '1'
    subprocess.run(command, cwd=cwd, env=environment, check=True)


def _copy_allowlist(stage: Path) -> None:
    for name in ALLOWLIST:
        source = ROOT / name
        if not source.is_file() or source.is_symlink():
            raise ValueError(f'Missing or symlinked allowlisted source: {name}')
        destination = stage / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    (stage / 'README.md').write_text(PUBLIC_README, encoding='utf-8')


def _verify(stage: Path, reference_dist: Path) -> None:
    private_dist = reference_dist
    stage_dist = stage / 'resources/outputs/vocabulary'
    for directory in (private_dist, stage_dist):
        found = {p.name for p in directory.iterdir() if p.is_file()}
        if found != GENERATED_FILES:
            raise ValueError(f'Unexpected or missing generated artifacts in {directory}: {found}')
    manifest = json.loads((stage_dist / 'manifest.json').read_text(encoding='utf-8'))
    if (manifest.get('inputs_complete') is not True or
            manifest.get('status') != 'build-output' or
            'publication_authorized' in manifest):
        raise ValueError('Release staging requires a complete publication-neutral build')
    if set(manifest.get('output_sha256', {})) != GENERATED_FILES - {'manifest.json'}:
        raise ValueError('Manifest output list differs from eight-file contract')
    if set(manifest.get('source_sha256', {})) != {'registry', 'mappings', 'codebook'}:
        raise ValueError('Incomplete canonical source manifest')
    for name in ALLOWLIST[:]:
        if name.startswith('resources/inputs/vocabulary/') and _sha(stage / name) != _sha(ROOT / name):
            raise ValueError(f'Scientific source modified during staging: {name}')
    for file in GENERATED_FILES:
        if (stage_dist / file).read_bytes() != (private_dist / file).read_bytes():
            raise ValueError(f'Staging build differs from validated private dist: {file}')
    for name, digest in manifest['output_sha256'].items():
        if _sha(stage_dist / name) != digest:
            raise ValueError(f'Output manifest hash mismatch: {name}')
    for name, digest in manifest['source_sha256'].items():
        if _sha(stage / 'resources/inputs/vocabulary' / {'registry':'registry.json', 'codebook':'codebook.md', 'mappings':'mappings.xlsx'}[name]) != digest:
            raise ValueError(f'Input manifest hash mismatch: {name}')
    actual = {p.relative_to(stage).as_posix()
              for p in stage.rglob('*') if p.is_file() or p.is_symlink()}
    expected = set(ALLOWLIST) | {'README.md'} | {'resources/outputs/vocabulary/' + name for name in GENERATED_FILES}
    if actual != expected:
        raise ValueError(f'Unapproved public staging file paths: {actual ^ expected}')


def stage_release(destination: Path, reference_dist: Path | None = None) -> Path:
    target = check_destination(destination)
    # Work in a temporary dir. A failed build never publishes a partial candidate.
    with tempfile.TemporaryDirectory(prefix='revmeta-candidate-') as temporary:
        stage = Path(temporary) / 'candidate'
        stage.mkdir()
        _copy_allowlist(stage)
        env = os.environ.copy()
        env['PYTHONPATH'] = 'src'
        _run([sys.executable, '-m', 'unittest', 'discover',
              '-s', 'tests/build', '-v'], stage, env)
        _run([sys.executable, '-m', 'revmeta', 'build', '--require-complete'], stage, env)
        _run([sys.executable, '-m', 'pyshacl',
              '-s', 'src/revmeta/build/shapes/vocabulary.shacl.ttl', '-df', 'turtle',
              '-sf', 'turtle', 'resources/outputs/vocabulary/vocabulary.ttl'], stage)
        _run(['sssom', 'validate', 'resources/outputs/vocabulary/mappings.sssom.tsv'], stage)
        _verify(stage, reference_dist if reference_dist is not None else VOCABULARY_OUTPUTS)
        shutil.copytree(stage, target)
    return target


def main() -> None:
    parser = argparse.ArgumentParser(
        description='Prepare a verified, allowlisted offline RevMeta candidate (NO publication)')
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--reference-dist', type=Path,
                        help='Already validated clean build, for CI under controlled source changes')
    arguments = parser.parse_args()
    try:
        target = stage_release(arguments.output, arguments.reference_dist)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f'BLOCKED: staging failed; nothing published: {exc}\n')
    print(f'Offline public CANDIDATE at {target}. No public operation was performed.')


if __name__ == '__main__':
    main()
