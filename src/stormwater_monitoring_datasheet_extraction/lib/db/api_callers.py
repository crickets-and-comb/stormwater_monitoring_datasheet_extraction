"""API callers for FileMaker Server REST API."""

from comb_utils.lib.api_callers import BasePostCaller
from typeguard import typechecked
from urllib.parse import quote

from stormwater_monitoring_datasheet_extraction.lib.db.auth import get_FMP_credentials, get_FMP_host_and_db
from stormwater_monitoring_datasheet_extraction.lib.constants import FMP_DATA_API_VERSION

class FMPAPIPostCaller(BasePostCaller):
    """API caller for FileMaker Server REST API POST requests."""

    token: str

    @typechecked
    def __init__(self) -> None:
        super().__init__()
        self._call_kwargs = {"headers": {"Content-Type": "application/json", "Accept": "application/json"}}

    def _set_url(self) -> None:
        hostname, database = get_FMP_host_and_db()
        encoded_db_name = quote(database)
        self._url = f"https://{hostname}.fmphost.com/fmi/data/{FMP_DATA_API_VERSION}/databases/{encoded_db_name}/sessions"

    @typechecked
    def _get_API_key(self) -> tuple[str, str]:
        """Get the username and password for FileMaker Server REST API."""
        return get_FMP_credentials()
    
    def _handle_200(self) -> None:
        super()._handle_200()
        self.token = self.response_json["token"]