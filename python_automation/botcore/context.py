"""Shared runtime context for automation loops."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict

from . import stats


@dataclass
class BehaviorState:
    """Mutable state used to emulate human-like randomness."""

    variance: float = 0.0
    attentive: int = 0
    quick_click: int = 0
    depth: int = 0

    def increment_depth(self) -> None:
        self.depth += 1

    def decrement_depth(self) -> None:
        if self.depth > 0:
            self.depth -= 1


@dataclass
class LoopContext:
    """Execution context shared across an automation run."""

    stats: stats.RunStats
    dry_run: bool = False
    behavior: BehaviorState = field(default_factory=BehaviorState)
    start_time: float = 0.0
    last_sleep_duration: float = 0.0
    metadata: Dict[str, object] = field(default_factory=dict)

    def mark_iteration_start(self, start_time: float) -> None:
        """Store the iteration start timestamp for later timing calculations."""

        self.start_time = start_time