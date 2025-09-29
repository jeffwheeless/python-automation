"""I/O primitives used by the automation loop.

These will ultimately wrap `pyautogui` and other OS interactions.
"""

from __future__ import annotations

import importlib
import random
import time
from typing import Any, Optional, Tuple

from .context import LoopContext

pyautogui: Optional[Any]
try:
    pyautogui = importlib.import_module("pyautogui")
except ModuleNotFoundError:  # pragma: no cover - optional dependency at this stage
    pyautogui = None

Point = Tuple[int, int]


def sleep(duration: float) -> None:
    """Sleep for the requested duration."""

    time.sleep(max(duration, 0.0))


def move_cursor(point: Point) -> None:
    """Move the cursor to a specific screen coordinate."""

    if pyautogui is None:
        return
    pyautogui.moveTo(point[0], point[1])


def click(point: Point) -> None:
    """Perform a click at the given point."""

    if pyautogui is None:
        return
    pyautogui.click(point[0], point[1])


def press_key(key: str) -> None:
    """Press a keyboard key."""

    if pyautogui is None:
        return
    pyautogui.press(key)


def perform_left_click(point: Point, *, dry_run: bool = False) -> None:
    """Mirror the legacy left-click with a randomised duration."""

    if dry_run or pyautogui is None:
        return
    duration = random.uniform(0.2, 0.6)
    pyautogui.click(point[0], point[1], duration=duration)


def mouse_out_of_range(point: Point) -> Point:
    """Placeholder for moving the mouse out of the main action area."""

    # Legacy implementation returned the same location; keep behaviour for now.
    return point


def perform_action_click(context: LoopContext, main_location: Point, wait_time: float = 3.0) -> None:
    """Sleep with the legacy randomness, then click the target location."""

    from . import randomness  # Local import to avoid circular dependency

    randomness.sleep_random(
        context,
        wait_time + random.uniform(2.8, 3.5),
        wait_time + random.uniform(4.5, 4.7),
    )
    target = mouse_out_of_range(main_location)
    perform_left_click(target, dry_run=context.dry_run)
    if random.randint(1, 1000) > 990:
        # Rare missed-click simulation – intentionally does nothing.
        return


def perform_action_key(context: LoopContext, key: str, wait_time: float = 3.0) -> None:
    """Press a key after a randomised delay with optional dry-run handling."""

    from . import randomness  # Local import to avoid circular dependency

    randomness.sleep_random(
        context,
        wait_time + random.uniform(2.8, 3.5),
        wait_time + random.uniform(4.5, 4.7),
    )
    if context.dry_run or pyautogui is None:
        return
    pyautogui.press(str(key))
