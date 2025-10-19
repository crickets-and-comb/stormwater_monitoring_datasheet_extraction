"""Tests for the db.auth module."""

from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib.db.auth import get_FMP_credentials


@typechecked
def test_get_FMP_credentials(mock_FMP_credentials: tuple[str, str]) -> None:
    """Test get_FMP_credentials function."""
    # Seems to be subject to race condition when running `act`. Indeterminant failures.
    username, password = get_FMP_credentials()
    assert (username, password) == mock_FMP_credentials
