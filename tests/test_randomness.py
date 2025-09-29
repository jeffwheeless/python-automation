"""Smoke tests for randomness helpers."""

from python_automation.botcore import randomness


def test_next_action_delay_within_bounds():
    value = randomness.next_action_delay(0.1, 0.2)
    assert 0.1 <= value <= 0.2
