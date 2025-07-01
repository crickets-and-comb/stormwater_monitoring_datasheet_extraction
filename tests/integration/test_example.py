"""This is just an example test."""

import time

import pytest

from stormwater_monitoring_datasheet_extraction.lib.example import wait_a_second


@pytest.mark.parametrize("seconds", [1, 2, 3])
def test_example(seconds: int) -> None:
    """Integration tests are usually to test that stuff works together.

    For instance, instead of connecting to a live DB, we might spin up a lightweight test DB
    in conftest.

    For now, we'll just make a simple unit test here of our example function.

    Test that we wait is at least as long as we expect to wait.
    """
    start_time = time.time()
    wait_a_second(seconds=seconds)
    end_time = time.time()
    assert end_time - start_time > seconds
