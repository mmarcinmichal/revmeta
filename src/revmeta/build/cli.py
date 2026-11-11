"""Build RevMeta development artifacts, without publishing or creating a release."""
from __future__ import annotations

import argparse
import json
import os
import tempfile
from pathlib import Path
from revmeta.paths import VOCABULARY_INPUTS, VOCABULARY_OUTPUTS
from revmeta.build.vocabulary import BASE, build
from revmeta.build.mappings import load_mapping_rows, export_sssom
from revmeta.build.alignments import write_alignments
from revmeta.build.sssom_rdf import write_sssom_rdf
from revmeta.build.decision_states import write_decision_states
from revmeta.build.manifest import write_manifest
from revmeta.build.html_docs import write_html


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description='Build RevMeta RDF/SSSOM (development stage)')
    parser.add_argument('--registry', type=Path, default=VOCABULARY_INPUTS / 'registry.json')
    parser.add_argument('--mappings', type=Path, default=VOCABULARY_INPUTS / 'mappings.xlsx')
    parser.add_argument('--guide', type=Path, default=VOCABULARY_INPUTS / 'codebook.md')
    parser.add_argument('--output', type=Path, default=VOCABULARY_OUTPUTS)
    parser.add_argument('--base', default=BASE)
    parser.add_argument('--require-complete', action='store_true',
                        help='Retained for compatibility; complete sources are now mandatory by default')
    parser.add_argument('--allow-partial', action='store_true',
                        help='Explicitly allow omitting the mapping source (nonrelease exploratory use)')
    args = parser.parse_args(argv)

    if args.require_complete and args.allow_partial:
        parser.error('--require-complete and --allow-partial cannot be combined')
    if not args.registry.is_file():
        raise SystemExit('BLOCKED: authoritative registry.json is missing')
    if not args.guide.is_file():
        raise SystemExit('BLOCKED: Codebook required for RDF vocabulary generation')
    if not args.mappings.is_file() and not args.allow_partial:
        raise SystemExit('BLOCKED: authoritative mappings.xlsx is missing')
    registry = json.loads(args.registry.read_text(encoding='utf-8'))
    target = args.output.resolve()
    if target.exists() and not target.is_dir():
        raise SystemExit('BLOCKED: output path exists and is not a directory')
    if args.allow_partial and (target == VOCABULARY_OUTPUTS.resolve() or
                               (target.exists() and any(target.iterdir()))):
        raise SystemExit('BLOCKED: partial build cannot replace a canonical or populated output')
    # Validate the potentially invalid XLSX before writing any output.
    checked_rows = load_mapping_rows(args.mappings, registry) if args.mappings.is_file() else None
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.revmeta-build-', dir=target.parent) as work:
        stage = Path(work) / 'staged'
        backup = Path(work) / 'old'
        paths = build(args.registry, stage, args.base, args.guide, args.mappings)
        generated = list(paths)
        state_path = write_decision_states(stage / 'decision-states.ttl', args.base)
        generated.append(state_path)
        print('Generated:', state_path, '(seven primary epistemic states)')
        for path in paths:
            print('Generated:', path)
        html = write_html(paths[0], stage / 'index.html')
        generated.append(html)
        print('Generated:', html)
    
        if args.mappings.is_file():
            rows = checked_rows
            dest = stage / 'mappings.sssom.tsv'
            export_sssom(rows, dest)
            generated.append(dest)
            print('Generated:', dest, f'({len(rows)} reviewed records)')
            rdf_path = stage / 'mappings.sssom.ttl'
            write_sssom_rdf(rows, rdf_path)
            generated.append(rdf_path)
            print('Generated:', rdf_path, f'({len(rows)} annotated mapping records)')
            alignment_path = stage / 'alignments.ttl'
            write_alignments(rows, alignment_path)
            generated.append(alignment_path)
            print('Generated:', alignment_path, '(107 concrete SKOS relations)')
        else:
            print('PARTIAL BUILD: mappings omitted by explicit --allow-partial; not releasable')
    
        manifest = write_manifest({'registry': args.registry, 'mappings': args.mappings,
                                   'codebook': args.guide}, generated,
                                  stage / 'manifest.json')
        print('Generated:', manifest)
        print('Development build only; no public release authorized.')
        # Only promote a fully generated directory; keep the previous state on failure.
        had_previous = target.exists()
        if had_previous:
            os.replace(target, backup)
        try:
            os.replace(stage, target)
        except BaseException:
            if had_previous:
                os.replace(backup, target)
            raise
    print('Committed complete development build to:', target)


if __name__ == '__main__':
    main()
