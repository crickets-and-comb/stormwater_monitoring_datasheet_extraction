"""Test the load_datasheets library."""

import json
import os
from pathlib import Path
from typing import Any, Dict

import pytest
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib.load_datasheets import load


@pytest.fixture
def sample_json_data() -> Dict[str, Any]:
    """Sample JSON data from the field datasheet definition."""
    return {
        "metadata": {
            "date": {"format": "YYYY-MM-DD"},
            "form_id": "str",
            "form_type": {
                "options": ["field_datasheet_stormwater_monitoring_friends_of_salish_sea"]
            },
            "form_version": "str",
            "investigators": {
                "name": "str",
                "end_time": {"format": "HH:MM"},
                "start_time": {"format": "HH:MM"},
            },
        },
        "forms": {
            "IMG_9527.jpg": {
                "form_type": "field_datasheet_stormwater_monitoring_friends_of_salish_sea",
                "form_version": "4.4-1-29-2025",
                "city": "BELLINGHAM",
                "date": "2025-04-17",
                "investigators": {"CIARA H": {"start_time": "14:40", "end_time": "15:23"}},
                "notes": "C ST: MICROBIAL MAT RETREATED ...",
                "observations": {
                    "field": {
                        "tide_height": -0.7,
                        "tide_time": "14:39",
                        "past_24hr_rainfall": 0.0,
                        "weather": "cloud_clear",
                    },
                    "site": [
                        {
                            "site_id": "C ST",
                            "dry_outfall": False,
                            "arrival_time": "14:41",
                            "flow": "M",
                            "flow_compared_to_expected": "Normal",
                            "air_temp": 21.0,
                            "water_temp": 11.6,
                            "DO_mg_per_l": 10.35,
                            "SPS micro_S_per_cm": 414.1,
                            "salinity_ppt": 0.2,
                            "pH": 5.91,
                            "color": {"rank": 1, "description": "YELLOW"},
                            "odor": {"rank": 1, "description": "SULPHUR"},
                            "visual": {"rank": None, "description": None},
                            "bacteria_bottle_no": "B1",
                        }
                    ],
                },
            }
        },
    }


class TestLoad:
    """Test the load function."""

    @typechecked
    def test_load_creates_output_directory_when_not_exists(
        self, sample_json_data: Dict[str, Any], tmp_path: Path
    ) -> None:
        """Test that load creates the output directory if it doesn't exist."""
        output_dir = tmp_path / "new_output_dir"
        result_path = load(sample_json_data, output_dir)

        assert output_dir.exists()
        assert result_path.exists()

    @typechecked
    def test_load_returns_path_to_json_file(
        self, sample_json_data: Dict[str, Any], tmp_path: Path
    ) -> None:
        """Test that load returns a path to a JSON file."""
        result_path = load(sample_json_data, tmp_path)

        assert result_path.suffix == ".json"

    @typechecked
    def test_load_creates_file_with_timestamp_name(
        self, sample_json_data: Dict[str, Any], tmp_path: Path
    ) -> None:
        """Test that load creates a file with timestamp in the name."""
        result_path = load(sample_json_data, tmp_path)

        assert result_path.name.startswith("stormwater_extraction_")

    @typechecked
    def test_load_writes_json_data_to_file(
        self, sample_json_data: Dict[str, Any], tmp_path: Path
    ) -> None:
        """Test that load writes the JSON data to the file."""
        result_path = load(sample_json_data, tmp_path)

        with open(result_path, "r", encoding="utf-8") as f:
            written_data = json.load(f)

        assert written_data == sample_json_data

    @typechecked
    def test_load_raises_value_error_for_empty_data(self, tmp_path: Path) -> None:
        """Test that load raises ValueError for empty JSON data."""
        with pytest.raises(ValueError, match="restructured_json cannot be empty or None"):
            load({}, tmp_path)

    @typechecked
    def test_load_uses_specified_output_directory(
        self, sample_json_data: Dict[str, Any], tmp_path: Path
    ) -> None:
        """Test that load uses the specified output directory."""
        output_dir = tmp_path / "test_output"
        result_path = load(sample_json_data, output_dir)

        assert result_path.parent == output_dir

    @typechecked
    def test_load_uses_default_directory_when_output_dir_empty(
        self, sample_json_data: Dict[str, Any], tmp_path: Path
    ) -> None:
        """Test that load uses default directory when output_dir is empty."""
        # Change to tmp_path directory to control where the file is created
        original_cwd = Path.cwd()
        try:
            os.chdir(tmp_path)
            result_path = load(sample_json_data, Path(""))
            # Make the path absolute so it works after changing back to original directory
            result_path = result_path.resolve()
        finally:
            os.chdir(original_cwd)

        # Verify the file was created with the expected name pattern
        assert result_path.name.startswith("stormwater_extraction_")
        assert result_path.suffix == ".json"
        assert result_path.exists()

    @typechecked
    def test_load_raises_os_error_on_write_failure(
        self, sample_json_data: Dict[str, Any], tmp_path: Path
    ) -> None:
        """Test that load raises OSError when file writing fails."""
        # Create a read-only directory to cause write failure
        readonly_dir = tmp_path / "readonly"
        readonly_dir.mkdir()
        readonly_dir.chmod(0o444)  # Read-only

        with pytest.raises(OSError, match="Failed to write data to"):
            load(sample_json_data, readonly_dir)
