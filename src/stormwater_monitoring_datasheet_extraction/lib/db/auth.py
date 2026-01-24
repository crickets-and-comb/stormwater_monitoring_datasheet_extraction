"""DB auth utilities.."""

import logging
import os
from os import getcwd as os_getcwd  # For test patching.
from pathlib import Path

from dotenv import load_dotenv
from typeguard import typechecked

from stormwater_monitoring_datasheet_extraction.lib.constants import EnvVars

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


@typechecked
def get_FMP_credentials() -> tuple[str, str]:
    """Get the FMP credentials."""
    load_dotenv(dotenv_path=Path(os_getcwd()) / ".env", override=True)

    username = os.getenv(EnvVars.FMP_USERNAME)
    password = os.getenv(EnvVars.FMP_PASSWORD)
    if not username or not password:
        raise ValueError(
            f"FMP credentials not found. Set the {EnvVars.FMP_USERNAME} "
            f"and {EnvVars.FMP_PASSWORD} environment variables."
        )

    return username, password


@typechecked
def get_FMP_host_and_db() -> tuple[str, str]:
    """Get the FMP host and database name."""
    load_dotenv(dotenv_path=Path(os_getcwd()) / ".env", override=True)

    host = os.getenv(EnvVars.FMP_HOSTNAME)
    database = os.getenv(EnvVars.FMP_DATABASE_NAME)
    if not host or not database:
        raise ValueError(
            f"FMP host and database not found. Set the {EnvVars.FMP_HOSTNAME} "
            f"and {EnvVars.FMP_DATABASE_NAME} environment variables."
        )

    return host, database