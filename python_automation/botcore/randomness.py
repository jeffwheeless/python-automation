"""Randomness helpers preserving the intentionally erratic behavior."""

from __future__ import annotations

import random
import time

from . import actions
from .context import LoopContext

DEFAULT_MIN_DELAY = 0.35
DEFAULT_MAX_DELAY = 1.25


def next_action_delay(min_delay: float = DEFAULT_MIN_DELAY, max_delay: float = DEFAULT_MAX_DELAY) -> float:
    """Return the next sleep duration between actions."""

    if min_delay > max_delay:
        min_delay, max_delay = max_delay, min_delay
    return random.uniform(min_delay, max_delay)


def jitter(value: float, *, spread: float = 0.05) -> float:
    """Apply a small random variation to a numeric value."""

    delta = random.uniform(-spread, spread)
    return max(0.0, value + delta)


def go_to_sleep(context: LoopContext, duration: float) -> None:
    """Sleep for ``duration`` seconds unless running in dry-run mode."""

    context.last_sleep_duration = max(duration, 0.0)
    if context.dry_run:
        return
    actions.sleep(context.last_sleep_duration)


def sleep_random(context: LoopContext, small_int: float, large_int: float) -> float:
    """Replicate the legacy ``sleepRandom`` behaviour with nested randomness.

    The intentionally chaotic branching is preserved so the automation remains
    slow and human-like. The returned value is the final sleep duration for the
    current invocation (the legacy implementation did not return a value).
    """

    state = context.behavior
    state.increment_depth()
    try:
        small_variant = small_int
        large_variant = large_int
        if state.variance > 0:
            small_variant = small_int * state.variance
            large_variant = large_int + (large_int * state.variance)
        if large_variant > 150:
            large_variant = random.uniform(150, 210)
        sleep_duration = round(
            random.uniform(small_variant, large_variant),
            10,
        )

        if state.depth <= 20:
            if random.randint(1, 1000) > (734 - state.attentive):
                sleep_random(context, 0, 0.8)

            afk_time = 0.0
            if context.start_time:
                afk_time = time.time() - context.start_time

            if state.variance > 0 and (afk_time + sleep_duration) <= random.randint(260, 300):
                if random.randint(1, 1000) > (874 - state.attentive):
                    sleep_random(context, 1, 2)
                elif random.randint(1, 1000) > (924 - state.attentive):
                    sleep_random(context, 1, 3)

                threshold = (99.35 - (state.attentive / 10)) - state.variance
                if random.uniform(1, 100) > threshold:
                    sleep_random(context, 0, random.randint(10, 60))
                    if state.depth <= 2 and random.randint(1, 1000) > 825:
                        _trigger_distraction(context)
                else:
                    threshold = (100.60 - (state.attentive / 10)) - state.variance
                    if random.uniform(1, 100) > threshold:
                        state.variance += 10
                        sleep_random(context, random.randint(1, 10), 100)
                        if state.depth <= 2 and random.randint(1, 1000) > (815 - state.variance):
                            _trigger_distraction(context)

                if random.randint(1, 1000) > 913:
                    _trigger_distraction(context)
        else:
            print("Too Deeply Nested")

        go_to_sleep(context, sleep_duration)
        return sleep_duration
    finally:
        state.decrement_depth()


def _trigger_distraction(context: LoopContext) -> None:
    """Helper to import detectors lazily and execute the distraction routine."""

    from . import detectors  # Local import to avoid circular dependency

    detectors.handle_distraction(context)
