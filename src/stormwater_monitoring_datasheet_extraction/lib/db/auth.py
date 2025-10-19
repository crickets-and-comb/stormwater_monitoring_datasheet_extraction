"""DB auth utilities.."""

import logging
import os
from os import getcwd as os_getcwd  # For test patching.
from pathlib import Path

from dotenv import load_dotenv
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib.constants import ENV_VARS

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@typechecked
def get_FMP_credentials() -> tuple[str, str]:
    """Get the FMP credentials."""
    load_dotenv(dotenv_path=Path(os_getcwd()) / ".env", override=True)

    username = os.getenv(ENV_VARS.FMP_USERNAME)
    password = os.getenv(ENV_VARS.FMP_PASSWORD)
    if not username or not password:
        raise ValueError(
            f"FMP credentials not found. Set the {ENV_VARS.FMP_USERNAME} "
            f"and {ENV_VARS.FMP_PASSWORD} environment variables."
        )

    return username, password
