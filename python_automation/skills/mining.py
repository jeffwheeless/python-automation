"""Mining skill migrated from the legacy `miningIron.py` script."""

from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from typing import Any, List, Mapping, Sequence

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
class OreSpot:
    x: int
    y: int
    wait: float = 1.0
    move_radius: float = 5.0
    double_click_chance: float = 0.3


@dataclass(frozen=True)
class RouteStep:
    x: int
    y: int
    action: str | None = None
    wait: float = 1.0
    move_radius: float = 5.0

    @property
    def requires_key(self) -> bool:
        return self.action not in (None, "", "leftClick", "rightClick")


@dataclass
class MiningConfig(SkillConfig):
    ore_spots: List[OreSpot] = field(default_factory=list)
    route_steps: List[RouteStep] = field(default_factory=list)
    variance: int = 0
    bags_per_run: int = 9
    rocks_per_cycle: int = 3
    shuffle_probability: float = 0.35
    random_move_probability: float = 0.5

    @staticmethod
    def from_mapping(mapping: Mapping[str, Any]) -> "MiningConfig":
        ore_payload = mapping.get("ore_spots", [])
        ore_spots: List[OreSpot] = []
        for item in ore_payload:
            if isinstance(item, Mapping):
                x = int(item.get("x", 0))
                y = int(item.get("y", 0))
                wait = float(item.get("wait", 1.0))
                move_radius = float(item.get("move_radius", 5.0))
                double_click_chance = float(item.get("double_click_chance", 0.3))
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                x = int(item[0])
                y = int(item[1])
                wait = float(item[2]) if len(item) > 2 else 1.0
                move_radius = float(item[3]) if len(item) > 3 else 5.0
                double_click_chance = float(item[4]) if len(item) > 4 else 0.3
            else:
                continue
            ore_spots.append(OreSpot(x, y, wait, move_radius, double_click_chance))

        route_payload = mapping.get("route_steps", [])
        route_steps: List[RouteStep] = []
        for item in route_payload:
            if isinstance(item, Mapping):
                x = int(item.get("x", 0))
                y = int(item.get("y", 0))
                action = item.get("action")
                wait = float(item.get("wait", 1.0))
                move_radius = float(item.get("move_radius", 5.0))
            elif isinstance(item, (list, tuple)) and len(item) >= 2:
                x = int(item[0])
                y = int(item[1])
                action = item[2] if len(item) > 2 else ""
                move_radius = float(item[3]) if len(item) > 3 else 5.0
                wait = float(item[4]) if len(item) > 4 else 1.0
            else:
                continue
            route_steps.append(RouteStep(x, y, action or "", wait, move_radius))

        config = MiningConfig(
            ore_spots=ore_spots,
            route_steps=route_steps,
        )
        config.variance = int(mapping.get("variance", 0))
        if "bags_per_run" in mapping:
            try:
                config.bags_per_run = max(1, int(mapping["bags_per_run"]))
            except (TypeError, ValueError):
                pass
        if "rocks_per_cycle" in mapping:
            try:
                config.rocks_per_cycle = max(1, int(mapping["rocks_per_cycle"]))
            except (TypeError, ValueError):
                pass
        if "shuffle_probability" in mapping:
            try:
                config.shuffle_probability = float(mapping["shuffle_probability"])
            except (TypeError, ValueError):
                pass
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


def _default_config() -> MiningConfig:
    return MiningConfig(
        ore_spots=[
            OreSpot(988, 617, wait=1.0, move_radius=6.0, double_click_chance=0.25),
            OreSpot(780, 893, wait=5.0, move_radius=5.0, double_click_chance=0.25),
            OreSpot(650, 1037, wait=4.0, move_radius=4.0, double_click_chance=0.25),
        ],
        route_steps=[
            RouteStep(988, 617, "", wait=1.0, move_radius=6.0),
            RouteStep(780, 893, "", wait=5.0, move_radius=5.0),
            RouteStep(650, 1037, "", wait=4.0, move_radius=4.0),
        ],
        variance=1,
        bags_per_run=9,
        rocks_per_cycle=3,
        shuffle_probability=0.35,
    )


@register_skill
class MiningSkill(BaseSkill):
    name = "mining"

    def __init__(self, config: MiningConfig | None = None) -> None:
        super().__init__(config or _default_config())

    def prepare(self, context: LoopContext) -> None:
        super().prepare(context)
        payload = context.metadata.get("config") if context.metadata else None
        if isinstance(payload, Mapping) and payload:
            self.config = MiningConfig.from_mapping(payload)
        if not self.config.ore_spots or not self.config.route_steps:
            raise SystemExit("Mining skill requires ore spots and route steps")
        print("Mining skill ready with ore spots:")
        for spot in self.config.ore_spots:
            print(f"  - ({spot.x}, {spot.y}) wait≈{spot.wait:.2f}s (radius {spot.move_radius})")

    def perform_iteration(self, context: LoopContext) -> None:
        super().perform_iteration(context)
        start = time.time()
        ore_spots = list(self.config.ore_spots)
        for bag_index in range(self.config.bags_per_run):
            self._maybe_shuffle_ores(ore_spots)
            self._mine_bag(context, ore_spots, bag_index)
        self._execute_route(context)
        duration = max(time.time() - start, 0.0)
        context.stats.record_iteration(duration=duration, dry_run=context.dry_run)
        self._print_iteration_summary(context)

    def teardown(self, context: LoopContext) -> None:
        super().teardown(context)
        print("Mining session complete.")

    # Mining flow helpers

    def _maybe_shuffle_ores(self, ore_spots: List[OreSpot]) -> None:
        if random.random() < self.config.shuffle_probability:
            random.shuffle(ore_spots)

    def _mine_bag(self, context: LoopContext, ore_spots: Sequence[OreSpot], bag_index: int) -> None:
        rocks = list(ore_spots)[: self.config.rocks_per_cycle]
        for idx, spot in enumerate(rocks):
            wait_low, wait_high = self._variant_window(spot.wait)
            randomness.sleep_random(context, wait_low, wait_high)
            target = self._move_to(context, spot.x, spot.y, spot.move_radius)
            self._perform_click(context, target)
            if random.random() < spot.double_click_chance:
                randomness.sleep_random(context, 0.05, 0.2)
                self._perform_click(context, target)
            if random.random() < self.config.random_move_probability:
                self._wiggle_mouse(ore_spots)
        if bag_index % 3 == 0 and ore_spots:
            # Occasional extra click to mimic legacy behaviour
            extra = random.choice(ore_spots)
            randomness.sleep_random(context, 0.2, 0.6)
            target = self._move_to(context, extra.x, extra.y, extra.move_radius)
            if random.random() < 0.5:
                self._perform_click(context, target)

    def _execute_route(self, context: LoopContext) -> None:
        for step in self.config.route_steps:
            wait_low, wait_high = self._variant_window(step.wait)
            randomness.sleep_random(context, wait_low, wait_high)
            target = self._move_to(context, step.x, step.y, step.move_radius)
            if step.requires_key:
                self._handle_key_action(context, step.action or "")
            else:
                self._handle_mouse_action(context, step.action or "leftClick", target)

    # Interaction helpers

    def _move_to(self, context: LoopContext, x: int, y: int, radius: float) -> tuple[int, int]:
        if context.dry_run:
            return (x, y)
        variance = int(radius) if radius > 0 else 5
        modified = MouseAutomation.modifyLocationMove(x, y, variance)
        adjusted = MouseAutomation.mouseOutOfRange(modified, True)
        return adjusted[0], adjusted[1]

    def _perform_click(self, context: LoopContext, point: tuple[int, int]) -> None:
        if context.dry_run:
            return
        actions.perform_left_click(point, dry_run=context.dry_run)

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

    def _wiggle_mouse(self, ore_spots: Sequence[OreSpot]) -> None:
        if not ore_spots:
            return
        choice = random.choice(ore_spots)
        MouseAutomation.modifyLocationMove(choice.x, choice.y, int(choice.move_radius or 5))

    # Timing helpers

    def _variant_window(self, timer: float) -> tuple[float, float]:
        variance = self.config.variance
        if timer == 0:
            return (0.05, 0.1)
        if variance == 0:
            return (timer * 0.98, timer * 1.02)
        if variance == 1:
            return (timer * 0.95, timer * 1.10)
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
