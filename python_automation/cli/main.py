"""Command-line interface for the automation bot."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Optional

from ..botcore import automation_loop
from ..io import config as config_io
from ..skills import available_skills


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Intentionally inefficient automation bot")
    subparsers = parser.add_subparsers(dest="command", required=True)

    list_parser = subparsers.add_parser("list", help="List available skills")
    list_parser.set_defaults(func=_cmd_list)

    run_parser = subparsers.add_parser("run", help="Run a skill")
    run_parser.add_argument("skill", help="Skill name to execute")
    run_parser.add_argument("--iterations", type=int, default=1, help="Iterations to run")
    run_parser.add_argument("--dry-run", action="store_true", help="Run without performing actions")
    run_parser.add_argument("--profile", default="default", help="Configuration profile to load")
    run_parser.add_argument(
        "--config-file",
        type=Path,
        help="Explicit path to a JSON/INI config file overriding profiles",
    )
    run_parser.set_defaults(func=_cmd_run)

    return parser


def _cmd_list(args: argparse.Namespace) -> None:
    for skill_name in sorted(available_skills().keys()):
        print(skill_name)


def _cmd_run(args: argparse.Namespace) -> None:
    skills = available_skills()
    if args.skill not in skills:
        raise SystemExit(f"Unknown skill: {args.skill}")
    skill_cls = skills[args.skill]
    skill = skill_cls()
    config_mapping = {}
    if args.config_file is not None:
        config_mapping = config_io.load_from_file(args.config_file)
    else:
        config_mapping = config_io.load_skill_config(args.skill, args.profile)

    loop_config = automation_loop.LoopConfig(iterations=args.iterations, dry_run=args.dry_run)
    stats = automation_loop.run_skill(
        skill,
        config=loop_config,
        metadata={
            "config": config_mapping,
            "profile": args.profile,
            "config_file": str(args.config_file) if args.config_file else None,
        },
    )
    print(f"Completed {stats.total_iterations} iterations (avg delay: {stats.average_duration:.2f}s)")


def main(argv: Optional[list[str]] = None) -> None:
    parser = build_parser()
    args = parser.parse_args(argv)
    args.func(args)


if __name__ == "__main__":  # pragma: no cover
    main()
