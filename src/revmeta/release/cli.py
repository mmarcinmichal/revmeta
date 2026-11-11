"""Offline release preparation CLI. Absolutely no remote write operations."""
from __future__ import annotations

import argparse
from pathlib import Path
import subprocess


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="revmeta release",
        description="Prepare offline RevMeta release candidates (no publication)",
    )
    commands = parser.add_subparsers(dest="action", required=True)
    stage = commands.add_parser("stage", help="Stage an allowlisted standalone public candidate")
    stage.add_argument("--output", type=Path, required=True)
    stage.add_argument("--reference-dist", type=Path)
    pages = commands.add_parser("pages", help="Prepare GitHub Pages and optional W3ID drafts offline")
    pages.add_argument("--source", type=Path)
    pages.add_argument("--inputs", type=Path)
    pages.add_argument("--output", type=Path, required=True)
    pages.add_argument("--w3id-draft", type=Path)

    args = parser.parse_args(argv)
    if args.action == "stage":
        from .candidate import stage_release
        try:
            target = stage_release(args.output, args.reference_dist)
        except (ValueError, OSError, subprocess.CalledProcessError) as exc:
            parser.exit(1, f"BLOCKED: staging failed; nothing published: {exc}\n")
        print(f"Offline public CANDIDATE at {target}. No public operation was performed.")
    else:
        from .pages import prepare
        options = {}
        if args.inputs is not None:
            options["inputs"] = args.inputs
        if args.w3id_draft is not None:
            options["w3id_draft"] = args.w3id_draft
        from revmeta.paths import VOCABULARY_OUTPUTS
        try:
            target = prepare(args.source or VOCABULARY_OUTPUTS, args.output, **options)
        except (ValueError, OSError) as exc:
            parser.exit(1, f"BLOCKED: Pages preview not prepared: {exc}\n")
        print(f"Offline Pages preview: {target}; no publishing or registration")


if __name__ == "__main__":
    main()
