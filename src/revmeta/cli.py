"""RevMeta command-line interface (non-publishing, local and CI)."""
from __future__ import annotations

import argparse
import sys


def main() -> None:
    # Keep release operations behind their own CLI and dependency boundary.
    if sys.argv[1:2] == ["release"]:
        from revmeta.release.cli import main as run_release
        run_release(sys.argv[2:])
        return
    parser = argparse.ArgumentParser(prog="revmeta")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("release", help="Prepare offline release/Pages candidates")
    build = commands.add_parser("build", help="Rebuild controlled vocabulary outputs")
    build.add_argument("--registry")
    build.add_argument("--mappings")
    build.add_argument("--guide")
    build.add_argument("--output")
    build.add_argument("--base")
    build.add_argument("--require-complete", action="store_true")
    build.add_argument("--allow-partial", action="store_true")
    analyze = commands.add_parser("analyze", help="Run private statistics")
    analyze.add_argument("analysis", choices=("mapping-coverage",))
    analyze.add_argument("--output-prefix")
    analyze.add_argument("--plot", action="store_true")
    args = parser.parse_args()
    if args.command == "build":
        from revmeta.build.cli import main as run_build
        argv = []
        for name in ("registry", "mappings", "guide", "output", "base"):
            value = getattr(args, name)
            if value:
                argv.extend(("--" + name, value))
        if args.require_complete:
            argv.append("--require-complete")
        if args.allow_partial:
            argv.append("--allow-partial")
        run_build(argv)
    else:
        from revmeta.analysis.mapping_coverage import main as run_analysis
        sys.argv = ["mapping_coverage", *([] if not args.output_prefix else
                    ["--output-prefix", args.output_prefix]), *(
                    ["--plot"] if args.plot else [])]
        run_analysis()
