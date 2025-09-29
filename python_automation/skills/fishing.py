"""Fishing skill migrated from the legacy script."""

from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from typing import Any, List, Mapping

try:  # Optional dependency during testing environments
    import pyautogui
except ModuleNotFoundError:  # pragma: no cover - optional dependency at this stage
    pyautogui = None

from modules.inventory import Inventory
from modules.mouseAutomation import MouseAutomation

from ..botcore import actions, randomness
from ..botcore.context import LoopContext
from . import register_skill
from .base import BaseSkill, SkillConfig


@dataclass(frozen=True)
class FishingLocation:
    x: int
    y: int
    action: str | None = None
    wait: float = 3.0
    move_radius: float = 5.0

    @property
    def requires_key(self) -> bool:
        return self.action not in (None, "", "leftClick", "rightClick")


@dataclass
class FishingConfig(SkillConfig):
    locations: List[FishingLocation] = field(default_factory=list)
    variance: int = 0
    random_move_probability: float = 0.6

    @staticmethod
    def from_mapping(mapping: Mapping[str, Any]) -> "FishingConfig":
        locations_payload = mapping.get("locations", [])
        locations: List[FishingLocation] = []
        for item in locations_payload:
            if isinstance(item, Mapping):
                x = int(item.get("x", 0))
                y = int(item.get("y", 0))
                action = item.get("action")
                wait = float(item.get("wait", 3.0))
                move_radius = float(item.get("move_radius", 5.0))
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                x = int(item[0])
                y = int(item[1])
                action = item[2] if len(item) > 2 else ""
                wait = float(item[3]) if len(item) > 3 else 3.0
                move_radius = float(item[4]) if len(item) > 4 else 5.0
            else:
                continue
            locations.append(FishingLocation(x, y, action or "", wait, move_radius))

        config = FishingConfig(locations=locations)
        config.variance = int(mapping.get("variance", 0))
        if "random_move_probability" in mapping:
            try:
                config.random_move_probability = float(mapping["random_move_probability"])
            except (TypeError, ValueError):
                pass
        iterations = mapping.get("iterations")
        if iterations is not None:
            try:
                config.iterations = int(iterations)
            except (TypeError, ValueError):
                pass
        return config


@register_skill
class FishingSkill(BaseSkill):
    name = "fishing"

    def __init__(self, config: FishingConfig | None = None) -> None:
        super().__init__(config or FishingConfig())

    def prepare(self, context: LoopContext) -> None:
        super().prepare(context)
        payload = context.metadata.get("config") if context.metadata else None
        if isinstance(payload, Mapping) and payload:
            self.config = FishingConfig.from_mapping(payload)
        if not self.config.locations:
            raise SystemExit("Fishing skill requires at least one configured location")
        print("Fishing skill ready with locations:")
        for loc in self.config.locations:
            action = loc.action or "leftClick"
            print(f"  - ({loc.x}, {loc.y}) -> {action} (wait≈{loc.wait:.2f}s)")

    def perform_iteration(self, context: LoopContext) -> None:
        super().perform_iteration(context)
        start = time.time()
        for location in self.config.locations:
            self._maybe_random_move(context)
            self._perform_location(context, location)
        duration = max(time.time() - start, 0.0)
        context.stats.record_iteration(duration=duration, dry_run=context.dry_run)
        self._print_iteration_summary(context)

    def teardown(self, context: LoopContext) -> None:
        super().teardown(context)
        print("Fishing session complete.")

    def _perform_location(self, context: LoopContext, location: FishingLocation) -> None:
        wait_low, wait_high = self._variant_window(location.wait)
        randomness.sleep_random(context, wait_low, wait_high)
        modified = self._move_to_location(context, location)
        if location.requires_key:
            self._handle_key_action(context, location.action or "")
        else:
            self._handle_mouse_action(context, location, modified)

    def _variant_window(self, timer: float) -> tuple[float, float]:
        variance = self.config.variance
        if timer == 0:
            return (0.05, 0.1)
        if variance == 0:
            return (timer * 0.98, timer * 1.02)
        if variance == 1:
            return (timer * 0.95, timer * 1.10)
        if variance == 2:
            return (timer * 0.90, timer * 1.25)
        if variance == 3:
            return (timer * 0.90, timer * 2.00)
        return (max(timer - 0.9, 0.05), timer + 0.5)

    def _move_to_location(self, context: LoopContext, location: FishingLocation) -> tuple[int, int]:
        if context.dry_run:
            return (location.x, location.y)
        radius = int(location.move_radius)
        modified = MouseAutomation.modifyLocationMove(location.x, location.y, radius if radius > 0 else 5)
        adjusted = MouseAutomation.mouseOutOfRange(modified, True)
        return adjusted[0], adjusted[1]

    def _handle_mouse_action(
        self,
        context: LoopContext,
        location: FishingLocation,
        point: tuple[int, int],
    ) -> None:
        if context.dry_run:
            return
        action = (location.action or "leftClick").lower()
        if action == "rightclick":
            MouseAutomation.performRightClick(point)
        else:
            actions.perform_left_click(point, dry_run=context.dry_run)

    def _handle_key_action(self, context: LoopContext, action_name: str) -> None:
        if context.dry_run or pyautogui is None:
            return
        action_name = action_name.lower()
        if action_name == "alttab":
            pyautogui.keyDown("alt")
            randomness.sleep_random(context, 0.08, 0.18)
            pyautogui.press("tab")
            randomness.sleep_random(context, 0.08, 0.18)
            pyautogui.keyUp("alt")
        elif action_name == "clickinv":
            Inventory.clickInventory([])
        else:
            pyautogui.press(action_name)

    def _maybe_random_move(self, context: LoopContext) -> None:
        if context.dry_run:
            return
        if random.random() > self.config.random_move_probability:
            return
        if not self.config.locations:
            return
        choice = random.choice(self.config.locations)
        MouseAutomation.modifyLocationMove(choice.x, choice.y, int(choice.move_radius or 5))

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
