"""Thieving skill migrated from the legacy `thief.py` script."""

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
class ThievingTarget:
    x: int
    y: int
    action: str | None = None
    wait: float = 0.3
    move_radius: float = 5.0

    @property
    def requires_key(self) -> bool:
        return self.action not in (None, "", "leftClick", "rightClick")


@dataclass(frozen=True)
class BonusAction:
    x: int
    y: int
    action: str | None = None
    wait: float = 4.0
    move_radius: float = 5.0

    @property
    def requires_key(self) -> bool:
        return self.action not in (None, "", "leftClick", "rightClick")


@dataclass
class ThievingConfig(SkillConfig):
    targets: List[ThievingTarget] = field(default_factory=list)
    bonus_actions: List[BonusAction] = field(default_factory=list)
    variance: int = 0
    bonus_progress_increment: float = 0.3
    bonus_trigger_base: float = 98.0

    @staticmethod
    def from_mapping(mapping: Mapping[str, Any]) -> "ThievingConfig":
        targets_payload = mapping.get("targets", [])
        targets: List[ThievingTarget] = []
        for item in targets_payload:
            if isinstance(item, Mapping):
                x = int(item.get("x", 0))
                y = int(item.get("y", 0))
                action = item.get("action")
                wait = float(item.get("wait", 0.3))
                move_radius = float(item.get("move_radius", 5.0))
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                x = int(item[0])
                y = int(item[1])
                action = item[2] if len(item) > 2 else ""
                wait = float(item[3]) if len(item) > 3 else 0.3
                move_radius = float(item[4]) if len(item) > 4 else 5.0
            else:
                continue
            targets.append(ThievingTarget(x, y, action or "", wait, move_radius))

        bonus_payload = mapping.get("bonus_actions", [])
        bonus_actions: List[BonusAction] = []
        for item in bonus_payload:
            if isinstance(item, Mapping):
                x = int(item.get("x", 0))
                y = int(item.get("y", 0))
                action = item.get("action")
                wait = float(item.get("wait", 4.0))
                move_radius = float(item.get("move_radius", 5.0))
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                x = int(item[0])
                y = int(item[1])
                action = item[2] if len(item) > 2 else ""
                wait = float(item[3]) if len(item) > 3 else 4.0
                move_radius = float(item[4]) if len(item) > 4 else 5.0
            else:
                continue
            bonus_actions.append(BonusAction(x, y, action or "", wait, move_radius))

        config = ThievingConfig(targets=targets, bonus_actions=bonus_actions)
        config.variance = int(mapping.get("variance", 0))
        if "bonus_progress_increment" in mapping:
            try:
                config.bonus_progress_increment = float(mapping["bonus_progress_increment"])
            except (TypeError, ValueError):
                pass
        if "bonus_trigger_base" in mapping:
            try:
                config.bonus_trigger_base = float(mapping["bonus_trigger_base"])
            except (TypeError, ValueError):
                pass
        iterations = mapping.get("iterations")
        if iterations is not None:
            try:
                config.iterations = int(iterations)
            except (TypeError, ValueError):
                pass
        return config


def _default_config() -> ThievingConfig:
    return ThievingConfig(
        targets=[
            ThievingTarget(3198, 1030, "", wait=0.3, move_radius=5.0),
        ],
        bonus_actions=[
            BonusAction(3315, 1067, "", wait=4.0, move_radius=5.0),
        ],
        variance=1,
        bonus_progress_increment=0.3,
        bonus_trigger_base=98.0,
    )


@register_skill
class ThievingSkill(BaseSkill):
    name = "thieving"

    def __init__(self, config: ThievingConfig | None = None) -> None:
        super().__init__(config or _default_config())
        self._bonus_progress: float = 0.0

    def prepare(self, context: LoopContext) -> None:
        super().prepare(context)
        payload = context.metadata.get("config") if context.metadata else None
        if isinstance(payload, Mapping) and payload:
            self.config = ThievingConfig.from_mapping(payload)
        if not self.config.targets:
            raise SystemExit("Thieving skill requires at least one target location")
        self._bonus_progress = 0.0
        print("Thieving skill ready with targets:")
        for target in self.config.targets:
            print(f"  - ({target.x}, {target.y}) wait≈{target.wait:.2f}s (radius {target.move_radius})")
        if self.config.bonus_actions:
            print("Bonus action locations available:")
            for bonus in self.config.bonus_actions:
                print(f"  * ({bonus.x}, {bonus.y}) wait≈{bonus.wait:.2f}s")

    def perform_iteration(self, context: LoopContext) -> None:
        super().perform_iteration(context)
        start = time.time()
        for target in self.config.targets:
            wait_low, wait_high = self._variant_window(target.wait)
            randomness.sleep_random(context, wait_low, wait_high)
            point = self._move_to(context, target.x, target.y, target.move_radius)
            self._handle_mouse_action(context, target.action or "leftClick", point)
            self._bonus_progress += self.config.bonus_progress_increment
            self._maybe_trigger_bonus(context)
        duration = max(time.time() - start, 0.0)
        context.stats.record_iteration(duration=duration, dry_run=context.dry_run)
        self._print_iteration_summary(context)

    def teardown(self, context: LoopContext) -> None:
        super().teardown(context)
        print("Thieving session complete.")

    # Bonus interactions

    def _maybe_trigger_bonus(self, context: LoopContext) -> None:
        if not self.config.bonus_actions:
            return
        threshold = max(1.0, self.config.bonus_trigger_base - self._bonus_progress)
        if random.randint(1, 100) >= threshold:
            self._bonus_progress = 0.0
            bonus = random.choice(self.config.bonus_actions)
            wait_low, wait_high = self._variant_window(bonus.wait)
            randomness.sleep_random(context, wait_low, wait_high)
            point = self._move_to(context, bonus.x, bonus.y, bonus.move_radius)
            if bonus.requires_key:
                self._handle_key_action(context, bonus.action or "")
            else:
                self._handle_mouse_action(context, bonus.action or "leftClick", point)

    # Interaction helpers

    def _move_to(self, context: LoopContext, x: int, y: int, radius: float) -> tuple[int, int]:
        if context.dry_run:
            return (x, y)
        variance = int(radius) if radius > 0 else 5
        modified = MouseAutomation.modifyLocationMove(x, y, variance)
        adjusted = MouseAutomation.mouseOutOfRange(modified, True)
        return adjusted[0], adjusted[1]

    def _handle_mouse_action(self, context: LoopContext, action: str, point: tuple[int, int]) -> None:
        if context.dry_run:
            return
        action_lower = action.lower()
        if action_lower == "rightclick":
            MouseAutomation.performRightClick(point)
        else:
            actions.perform_left_click(point, dry_run=context.dry_run)

    def _handle_key_action(self, context: LoopContext, action_name: str) -> None:
        if context.dry_run or pyautogui is None:
            return
        action = action_name.lower()
        if action == "alttab":
            pyautogui.keyDown("alt")
            randomness.sleep_random(context, 0.08, 0.18)
            pyautogui.press("tab")
            randomness.sleep_random(context, 0.08, 0.18)
            pyautogui.keyUp("alt")
        elif action == "clickinv":
            Inventory.clickInventory([])
        else:
            pyautogui.press(action)

    # Timing helpers

    def _variant_window(self, timer: float) -> tuple[float, float]:
        variance = self.config.variance
        if timer == 0:
            return (0.05, 0.1)
        if variance == 0:
            return (timer * 0.98, timer * 1.02)
        if variance == 1:
            return (timer * 0.90, timer * 1.10)
        if variance == 2:
            return (timer * 0.75, timer * 1.25)
        if variance == 3:
            return (timer * 0.50, timer * 1.50)
        return (max(timer - 0.9, 0.05), timer + 0.5)

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
