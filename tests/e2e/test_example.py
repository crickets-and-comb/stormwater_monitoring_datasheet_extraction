"""This is just an example test."""

import time

import pytest

from stormwater_monitoring_datasheet_extraction import wait_a_second


@pytest.mark.parametrize("seconds", [1, 2, 3])
def test_example(seconds: int) -> None:
    """e2e tests are usually to test live stuff (DBs, filesystems) and workflows.

    For now, we'll just make a simple unit test here of our example function.

    Test that we wait at least as long as we expect to wait.
    """
    start_time = time.time()
    wait_a_second(seconds=seconds)
    end_time = time.time()
    assert end_time - start_time > seconds
