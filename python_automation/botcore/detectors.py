"""Anti-detection helpers used to insert human-like behaviour."""

from __future__ import annotations

import random
from typing import Optional

from . import actions
from .context import LoopContext


def should_inject_distraction(threshold: float = 0.07) -> bool:
    """Randomly decide whether to simulate a distraction."""

    return random.random() < threshold


def apply_distraction(min_seconds: float = 10.0, max_seconds: float = 45.0) -> Optional[float]:
    """Perform a distraction pause, returning the duration if executed."""

    if min_seconds <= 0 and max_seconds <= 0:
        return None
    duration = random.uniform(min_seconds, max_seconds)
    actions.sleep(duration)
    return duration


def handle_distraction(context: LoopContext) -> None:
    """Port of the legacy ``distract`` routine using structured state."""

    state = context.behavior
    stats = context.stats

    print(f"quickClick: {state.quick_click}")

    if state.quick_click > 45 and random.uniform(1, 100) > (92.9 - state.variance):
        state.attentive = random.randint(-5, 6)
        print("Distracted")
        from . import randomness  # local import to avoid circular dependency

        randomness.sleep_random(
            context,
            random.randint(30, 45),
            random.randint(100, 240),
        )
        print(f"Attentive: {state.attentive}")
        print("Locking In")
        state.variance = 0
        stats.reset_focus()
        state.quick_click = 0

    if state.quick_click < random.randint(random.randint(20, 26), 45):
        print("Quick Clicking")
        state.variance = 0
        state.quick_click += 1
    else:
        state.quick_click = 50
