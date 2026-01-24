"""Tests conftest."""

import os
from collections.abc import Iterator
from pathlib import Path
from unittest.mock import patch

import pytest
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib.constants import EnvVars


def pytest_collection_modifyitems(config: pytest.Config, items: list[pytest.Item]) -> None:
    """Mark test types."""
    unit_tests_dir = os.path.join(config.rootdir, "tests/unit")
    integration_tests_dir = os.path.join(config.rootdir, "tests/integration")
    e2e_tests_dir = os.path.join(config.rootdir, "tests/e2e")

    for item in items:
        test_path = str(item.fspath)
        if test_path.startswith(unit_tests_dir):
            item.add_marker("unit")
        elif test_path.startswith(integration_tests_dir):
            item.add_marker("integration")
        elif test_path.startswith(e2e_tests_dir):
            item.add_marker("e2e")


@pytest.fixture
def mock_FMP_credentials() -> tuple[str, str]:
    """Fake FMP credentials."""
    return "fmp_username", "fmp_password"


@pytest.fixture(autouse=True)
@typechecked
def mock_get_FMP_credentials(
    mock_FMP_credentials: tuple[str, str], tmp_path: Path
) -> Iterator:
    """Mock get_FMP_credentials."""
    env_path = tmp_path / ".env"
    env_path.write_text(
        f"{EnvVars.FMP_USERNAME}={mock_FMP_credentials[0]}"
        f"\n{EnvVars.FMP_PASSWORD}={mock_FMP_credentials[1]}"
    )

    with patch(
        "stormwater_monitoring_datasheet_extraction.lib.db.auth.os_getcwd",
        return_value=tmp_path,
    ) as mock_getcwd:
        mock_getcwd.return_value = tmp_path
        yield
