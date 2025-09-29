"""Automation loop orchestrating skill execution."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Protocol

from . import stats
from .context import LoopContext


class Skill(Protocol):
    """Protocol that all skills must implement."""

    name: str

    def prepare(self, context: LoopContext) -> None:
        """Perform setup before execution."""

    def perform_iteration(self, context: LoopContext) -> None:
        """Execute a single automation iteration."""

    def teardown(self, context: LoopContext) -> None:
        """Clean up resources after execution."""


@dataclass
class LoopConfig:
    iterations: int
    dry_run: bool = False
    distraction_frequency: float = 0.0


def run_skill(
    skill: Skill,
    *,
    config: LoopConfig,
    metadata: dict[str, object] | None = None,
) -> stats.RunStats:
    """Run a skill for the desired number of iterations."""

    run_stats = stats.RunStats(skill_name=skill.name)
    context = LoopContext(
        stats=run_stats,
        dry_run=config.dry_run,
        metadata=metadata or {},
    )
    skill.prepare(context)
    try:
        for _ in range(config.iterations):
            context.mark_iteration_start(time.time())
            before = run_stats.total_iterations
            skill.perform_iteration(context)
            after = run_stats.total_iterations
            if after == before:
                duration = max(time.time() - context.start_time, 0.0)
                run_stats.record_iteration(duration=duration, dry_run=config.dry_run)
    finally:
        skill.teardown(context)
    return run_stats
