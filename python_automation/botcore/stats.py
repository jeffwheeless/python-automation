"""Tracking helpers for automation runs."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class IterationRecord:
    duration: float
    dry_run: bool = False


@dataclass
class RunStats:
    skill_name: str
    iterations: List[IterationRecord] = field(default_factory=list)
    total_time: float = 0.0
    total_time_stamped: float = 0.0
    new_total: int = 0
    longest_run: float = 0.0
    shortest_run: float = float("inf")
    last_duration: float = 0.0

    def record_iteration(self, *, duration: float, dry_run: bool = False) -> None:
        """Record an iteration for later reporting."""

        self.iterations.append(IterationRecord(duration=duration, dry_run=dry_run))
        self.new_total += 1
        self.last_duration = duration
        if dry_run:
            return
        self.total_time += duration
        self.total_time_stamped += duration
        if duration > self.longest_run:
            self.longest_run = duration
        if duration < self.shortest_run:
            self.shortest_run = duration

    @property
    def total_iterations(self) -> int:
        return len(self.iterations)

    @property
    def average_duration(self) -> float:
        if not self.iterations:
            return 0.0
        total = sum(record.duration for record in self.iterations if not record.dry_run)
        counted = sum(1 for record in self.iterations if not record.dry_run)
        if counted == 0:
            return 0.0
        return total / counted

    @property
    def shortest_run_duration(self) -> float:
        if self.shortest_run == float("inf"):
            return 0.0
        return self.shortest_run

    def reset_focus(self) -> None:
        """Reset variance-related counters after a distraction."""

        self.total_time = 0.0
        self.new_total = 1
        self.last_duration = 0.0
