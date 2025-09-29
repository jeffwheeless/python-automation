"""Skill that mirrors the intentionally inefficient behaviour from `dunno.py`."""

from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from typing import Any, List, Mapping, Sequence

from ..botcore import actions
from ..botcore.context import LoopContext
from . import register_skill
from .base import BaseSkill, SkillConfig


@dataclass(frozen=True)
class LocationSpec:
    """Describe a target interaction point."""

    x: int
    y: int
    action: str | None = None
    wait_hint: float = 3.0
    move_radius: float = 0.0

    @property
    def is_keypress(self) -> bool:
        return self.action is not None and self.action != ""


def _default_locations() -> List[LocationSpec]:
    return [
        LocationSpec(1890, 721, "", 0.9122617244720459, 6),
        LocationSpec(1899, 632, "", 1.034623146057129, 6),
        LocationSpec(0, 0, "space", 14.5885329246521, 0),
    ]


@dataclass
class DumbClickerConfig(SkillConfig):
    """Configuration for the dumb clicker skill."""

    locations: List[LocationSpec] = field(default_factory=_default_locations)

    @staticmethod
    def from_mapping(mapping: Mapping[str, Any]) -> "DumbClickerConfig":
        locations_payload = mapping.get("locations", [])
        locations: List[LocationSpec] = []
        for item in locations_payload:
            if isinstance(item, Mapping):
                x = int(item.get("x", 0))
                y = int(item.get("y", 0))
                action = item.get("action")
                wait = float(item.get("wait", item.get("wait_hint", 3.0)))
                move_radius = float(item.get("move_radius", 0))
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                x = int(item[0])
                y = int(item[1])
                action = item[2] if len(item) > 2 else ""
                wait = float(item[3]) if len(item) > 3 else 3.0
                move_radius = float(item[4]) if len(item) > 4 else 0.0
            else:
                continue
            locations.append(LocationSpec(x, y, action or "", wait, move_radius))
        config = DumbClickerConfig(locations=locations or _default_locations())
        iterations = mapping.get("iterations")
        if iterations is not None:
            try:
                config.iterations = int(iterations)
            except (TypeError, ValueError):
                pass
        return config


@register_skill
class DumbClickerSkill(BaseSkill):
    """Replicate the "dumb bot" loop using the refactored architecture."""

    name = "dumb_clicker"

    def __init__(self, config: DumbClickerConfig | None = None) -> None:
        super().__init__(config or DumbClickerConfig())

    def prepare(self, context: LoopContext) -> None:
        super().prepare(context)
        payload = context.metadata.get("config") if context.metadata else None
        if isinstance(payload, Mapping) and payload:
            self.config = DumbClickerConfig.from_mapping(payload)
        print("Running dumb clicker skill with locations:")
        for spec in self.config.locations:
            action = spec.action or "click"
            print(f"  - ({spec.x}, {spec.y}) -> {action} (wait≈{spec.wait_hint:.2f}s)")

    def perform_iteration(self, context: LoopContext) -> None:
        super().perform_iteration(context)
        for spec in self._locations_cycle():
            if spec.is_keypress:
                actions.perform_action_key(context, spec.action or "", wait_time=spec.wait_hint)
            else:
                target = self._jitter_target(spec)
                actions.perform_action_click(context, target, wait_time=spec.wait_hint)
        duration = max(time.time() - context.start_time, 0.0)
        context.stats.record_iteration(duration=duration, dry_run=context.dry_run)
        self._print_iteration_summary(context)

    def teardown(self, context: LoopContext) -> None:
        super().teardown(context)
        print("Dumb clicker skill finished.")

    def _locations_cycle(self) -> Sequence[LocationSpec]:
        return self.config.locations

    def _jitter_target(self, spec: LocationSpec) -> tuple[int, int]:
        if spec.move_radius <= 0:
            return (spec.x, spec.y)
        radius = int(spec.move_radius)
        return (
            spec.x + random.randint(-radius, radius),
            spec.y + random.randint(-radius, radius),
        )

    def _print_iteration_summary(self, context: LoopContext) -> None:
        stats = context.stats
        duration = stats.last_duration
        print(f"\nIteration took: {duration:.3f}s")
        print(f"Range {stats.shortest_run_duration:.3f} thru {stats.longest_run:.3f}")
        print("AverageTimeStamped = TotalTimeStamped  / Total")
        total_iters = max(stats.total_iterations, 1)
        average_stamped = stats.total_time_stamped / total_iters if total_iters else 0.0
        print(f"{average_stamped:.3f} = {stats.total_time_stamped:.3f} / {total_iters}")
        if stats.new_total:
            rolling = stats.total_time / stats.new_total if stats.new_total else 0.0
            print(f"{rolling:.3f}")
            print(f"{rolling:.3f} = {stats.total_time:.3f} / {stats.new_total}")
