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

    @pytest.mark.parametrize(
        "output_dir,expected_dir_name",
        [
            (Path("test_output"), "test_output"),
            (Path(""), "stormwater_extraction_"),  # Will contain timestamp
        ],
    )
    @typechecked
    def test_load_creates_output_directory_and_file(
        self,
        sample_json_data: Dict[str, Any],
        output_dir: Path,
        expected_dir_name: str,
        tmp_path: Path,
    ) -> None:
        """Test that load creates the output directory and file correctly."""
        if output_dir == Path(""):
            # Change to tmp_path directory to control where the file is created
            original_cwd = Path.cwd()
            try:
                os.chdir(tmp_path)
                result_path = load(sample_json_data, output_dir)
                result_path = result_path.resolve()  # Make absolute
            finally:
                os.chdir(original_cwd)
        else:
            result_path = load(sample_json_data, output_dir)

        # Verify the file was created with expected properties
        assert result_path.exists()
        assert result_path.suffix == ".json"
        assert result_path.name.startswith("stormwater_extraction_")
        assert result_path.parent.name.startswith(expected_dir_name)

    @typechecked
    def test_load_writes_correct_json_data_to_file(
        self, sample_json_data: Dict[str, Any], tmp_path: Path
    ) -> None:
        """Test that load writes the correct JSON data to the file."""
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
