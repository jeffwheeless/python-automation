"""Fletching skill migrated from the legacy `fletch.py` script."""

from __future__ import annotations

import random
import time
from dataclasses import dataclass, field
from typing import Any, Iterable, List, Mapping, Sequence

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
class ActionSpec:
    x: int
    y: int
    action: str | None = None
    wait: float = 1.0
    move_radius: float = 5.0

    @property
    def requires_key(self) -> bool:
        normalized = (self.action or "").lower()
        return normalized not in ("", "leftclick", "rightclick")

    @property
    def uses_right_click(self) -> bool:
        return (self.action or "").lower() == "rightclick"


@dataclass(frozen=True)
class InventoryCheck:
    x: int
    y: int
    r: int
    g: int
    b: int
    tolerance: int = 10


@dataclass
class FletchingConfig(SkillConfig):
    bank_sequence: List[ActionSpec] = field(default_factory=list)
    combine_sequence: List[ActionSpec] = field(default_factory=list)
    inventory_patterns: List[List[ActionSpec]] = field(default_factory=list)
    variance: int = 0
    post_combine_wait: float = 50.0
    inventory_check: InventoryCheck | None = None
    max_inventory_attempts: int = 12

    @staticmethod
    def from_mapping(mapping: Mapping[str, Any]) -> "FletchingConfig":
        bank_sequence = [_parse_action(item) for item in mapping.get("bank_sequence", []) if _parse_action(item)]
        combine_sequence = [_parse_action(item) for item in mapping.get("combine_sequence", []) if _parse_action(item)]
        inventory_patterns = []
        for pattern in mapping.get("inventory_patterns", []):
            actions_list = [_parse_action(item) for item in pattern if _parse_action(item)]
            if actions_list:
                inventory_patterns.append(actions_list)
        config = FletchingConfig(
            bank_sequence=bank_sequence,
            combine_sequence=combine_sequence,
            inventory_patterns=inventory_patterns,
        )
        config.variance = int(mapping.get("variance", 0))
        if "post_combine_wait" in mapping:
            try:
                config.post_combine_wait = float(mapping["post_combine_wait"])
            except (TypeError, ValueError):
                pass
        if "max_inventory_attempts" in mapping:
            try:
                config.max_inventory_attempts = max(1, int(mapping["max_inventory_attempts"]))
            except (TypeError, ValueError):
                pass
        inv_check = mapping.get("inventory_check")
        if isinstance(inv_check, Mapping):
            try:
                config.inventory_check = InventoryCheck(
                    x=int(inv_check.get("x", 0)),
                    y=int(inv_check.get("y", 0)),
                    r=int(inv_check.get("r", 0)),
                    g=int(inv_check.get("g", 0)),
                    b=int(inv_check.get("b", 0)),
                    tolerance=int(inv_check.get("tolerance", 10)),
                )
            except (TypeError, ValueError):
                config.inventory_check = None
        iterations = mapping.get("iterations")
        if iterations is not None:
            try:
                config.iterations = int(iterations)
            except (TypeError, ValueError):
                pass
        return config


def _parse_action(item: Any) -> ActionSpec | None:
    if isinstance(item, Mapping):
        try:
            return ActionSpec(
                x=int(item.get("x", 0)),
                y=int(item.get("y", 0)),
                action=item.get("action"),
                wait=float(item.get("wait", 1.0)),
                move_radius=float(item.get("move_radius", 5.0)),
            )
        except (TypeError, ValueError):
            return None
    if isinstance(item, (list, tuple)) and len(item) >= 2:
        x = int(item[0])
        y = int(item[1])
        action = item[2] if len(item) > 2 else ""
        wait = float(item[3]) if len(item) > 3 else 1.0
        move_radius = float(item[4]) if len(item) > 4 else 5.0
        return ActionSpec(x, y, action or "", wait, move_radius)
    return None


def _default_config() -> FletchingConfig:
    return FletchingConfig(
        bank_sequence=[
            ActionSpec(2872, 460, "", wait=8.0, move_radius=45.0),
            ActionSpec(2576, 742, "", wait=8.0, move_radius=45.0),
        ],
        combine_sequence=[
            ActionSpec(3511, 962, "", wait=5.0, move_radius=1.0),
            ActionSpec(3462, 964, "3", wait=5.0, move_radius=1.0),
        ],
        inventory_patterns=[
            [
                ActionSpec(3366, 835, "", 5.0, 0.5),
                ActionSpec(3414, 834, "", 5.0, 0.5),
                ActionSpec(3465, 837, "", 5.0, 0.5),
                ActionSpec(3464, 877, "", 5.0, 0.5),
                ActionSpec(3414, 877, "", 5.0, 0.5),
                ActionSpec(3365, 877, "", 5.0, 0.5),
                ActionSpec(3367, 921, "", 5.0, 0.5),
                ActionSpec(3416, 917, "", 5.0, 0.5),
                ActionSpec(3463, 920, "", 5.0, 0.5),
                ActionSpec(3467, 964, "", 5.0, 0.5),
                ActionSpec(3415, 961, "", 5.0, 0.5),
                ActionSpec(3366, 960, "", 5.0, 0.5),
                ActionSpec(3366, 1002, "", 5.0, 0.5),
                ActionSpec(3418, 1003, "", 5.0, 0.5),
                ActionSpec(3467, 1001, "", 5.0, 0.5),
                ActionSpec(3465, 918, "", 5.0, 0.5),
                ActionSpec(3414, 1043, "", 5.0, 0.5),
                ActionSpec(3367, 1044, "", 5.0, 0.5),
            ],
            [
                ActionSpec(3366, 836, "", 5.0, 0.5),
                ActionSpec(3417, 834, "", 5.0, 0.5),
                ActionSpec(3415, 880, "", 5.0, 0.5),
                ActionSpec(3366, 880, "", 5.0, 0.5),
                ActionSpec(3365, 919, "", 5.0, 0.5),
                ActionSpec(3422, 923, "", 5.0, 0.5),
                ActionSpec(3419, 962, "", 5.0, 0.5),
                ActionSpec(3368, 967, "", 5.0, 0.5),
                ActionSpec(3368, 1001, "", 5.0, 0.5),
                ActionSpec(3421, 1004, "", 5.0, 0.5),
                ActionSpec(3414, 1049, "", 5.0, 0.5),
                ActionSpec(3368, 1044, "", 5.0, 0.5),
                ActionSpec(3466, 1046, "", 5.0, 0.5),
                ActionSpec(3467, 1004, "", 5.0, 0.5),
                ActionSpec(3467, 957, "", 5.0, 0.5),
                ActionSpec(3467, 918, "", 5.0, 0.5),
                ActionSpec(3466, 876, "", 5.0, 0.5),
                ActionSpec(3460, 837, "", 5.0, 0.5),
            ],
            [
                ActionSpec(3370, 1042, "", 5.0, 0.5),
                ActionSpec(3421, 1044, "", 5.0, 0.5),
                ActionSpec(3467, 1042, "", 5.0, 0.5),
                ActionSpec(3467, 999, "", 5.0, 0.5),
                ActionSpec(3416, 1001, "", 5.0, 0.5),
                ActionSpec(3364, 1001, "", 5.0, 0.5),
                ActionSpec(3367, 957, "", 5.0, 0.5),
                ActionSpec(3417, 961, "", 5.0, 0.5),
                ActionSpec(3467, 962, "", 5.0, 0.5),
                ActionSpec(3466, 919, "", 5.0, 0.5),
                ActionSpec(3420, 919, "", 5.0, 0.5),
                ActionSpec(3365, 914, "", 5.0, 0.5),
                ActionSpec(3368, 876, "", 5.0, 0.5),
                ActionSpec(3368, 830, "", 5.0, 0.5),
                ActionSpec(3423, 837, "", 5.0, 0.5),
                ActionSpec(3423, 878, "", 5.0, 0.5),
                ActionSpec(3464, 877, "", 5.0, 0.5),
                ActionSpec(3464, 835, "", 5.0, 0.5),
            ],
        ],
        variance=1,
        post_combine_wait=50.0,
        inventory_check=InventoryCheck(x=3465, y=1045, r=0, g=255, b=192, tolerance=10),
        max_inventory_attempts=15,
    )


@register_skill
class FletchingSkill(BaseSkill):
    name = "fletching"

    def __init__(self, config: FletchingConfig | None = None) -> None:
        super().__init__(config or _default_config())

    def prepare(self, context: LoopContext) -> None:
        super().prepare(context)
        payload = context.metadata.get("config") if context.metadata else None
        if isinstance(payload, Mapping) and payload:
            self.config = FletchingConfig.from_mapping(payload)
        if not self.config.bank_sequence:
            raise SystemExit("Fletching skill requires a bank sequence")
        if not self.config.combine_sequence:
            raise SystemExit("Fletching skill requires a combine sequence")
        if not self.config.inventory_patterns:
            raise SystemExit("Fletching skill requires inventory patterns")
        print("Fletching skill ready:")
        print(f"  - Bank sequence: {len(self.config.bank_sequence)} actions")
        print(f"  - Combine sequence: {len(self.config.combine_sequence)} actions")
        print(f"  - Inventory patterns: {len(self.config.inventory_patterns)} variants")

    def perform_iteration(self, context: LoopContext) -> None:
        super().perform_iteration(context)
        start = time.time()
        self._prepare_inventory(context)
        self._run_sequence(context, self.config.combine_sequence)
        wait_low, wait_high = self._variant_window(self.config.post_combine_wait)
        randomness.sleep_random(context, wait_low, wait_high)
        pattern = random.choice(self.config.inventory_patterns)
        self._run_sequence(context, pattern)
        duration = max(time.time() - start, 0.0)
        context.stats.record_iteration(duration=duration, dry_run=context.dry_run)
        self._print_iteration_summary(context)

    def teardown(self, context: LoopContext) -> None:
        super().teardown(context)
        print("Fletching session complete.")

    # Sequences -----------------------------------------------------------------

    def _prepare_inventory(self, context: LoopContext) -> None:
        attempts = 0
        if context.dry_run or self.config.inventory_check is None:
            self._run_sequence(context, self.config.bank_sequence)
            return
        while attempts < self.config.max_inventory_attempts:
            if self._inventory_ready():
                return
            self._run_sequence(context, self.config.bank_sequence)
            attempts += 1
        print("Inventory color check did not trigger; continuing anyway.")

    def _run_sequence(self, context: LoopContext, sequence: Sequence[ActionSpec]) -> None:
        if not sequence:
            return
        for action in sequence:
            self._maybe_random_move(sequence)
            wait_low, wait_high = self._variant_window(action.wait)
            if random.randint(1, 100) < 75:
                randomness.sleep_random(context, wait_low, wait_high)
                point = self._move_to(context, action)
            else:
                randomness.sleep_random(context, 0.01, 0.1)
                point = self._move_to(context, action)
                randomness.sleep_random(context, wait_low, wait_high)
            randomness.sleep_random(context, 0.01, 0.1)
            self._execute_action(context, action, point)
            if action.wait > 2 and random.randint(1, 1000) > 980:
                print("-- Long Break --")
                randomness.sleep_random(context, 5, 120)

    # Interaction helpers -------------------------------------------------------

    def _execute_action(self, context: LoopContext, action: ActionSpec, point: tuple[int, int]) -> None:
        if action.requires_key:
            self._handle_key_action(context, action.action or "")
        else:
            if action.uses_right_click:
                self._handle_mouse_action(context, "rightClick", point)
            else:
                self._handle_mouse_action(context, "leftClick", point)

    def _move_to(self, context: LoopContext, action: ActionSpec) -> tuple[int, int]:
        if context.dry_run:
            return (action.x, action.y)
        radius = int(action.move_radius) if action.move_radius > 0 else 5
        modified = MouseAutomation.modifyLocationMove(action.x, action.y, radius)
        adjusted = MouseAutomation.mouseOutOfRange(modified, True)
        return adjusted[0], adjusted[1]

    def _handle_mouse_action(self, context: LoopContext, action_name: str, point: tuple[int, int]) -> None:
        if context.dry_run:
            return
        action_lower = action_name.lower()
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

    def _maybe_random_move(self, sequence: Sequence[ActionSpec]) -> None:
        if len(sequence) <= 2:
            return
        if random.randint(0, 10) < 8:
            return
        choice = random.choice(sequence)
        MouseAutomation.modifyLocationMove(choice.x, choice.y, 30)

    # Timing & status -----------------------------------------------------------

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

    def _inventory_ready(self) -> bool:
        if pyautogui is None or self.config.inventory_check is None:
            return True
        check = self.config.inventory_check
        try:
            return pyautogui.pixelMatchesColor(
                check.x,
                check.y,
                (check.r, check.g, check.b),
                tolerance=check.tolerance,
            )
        except TypeError:
            return False

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
