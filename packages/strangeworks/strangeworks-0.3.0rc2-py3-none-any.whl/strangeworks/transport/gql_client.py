"""platform.py."""
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import requests
from gql import Client, gql
from gql.transport.exceptions import TransportQueryError
from gql.transport.requests import RequestsHTTPTransport
from requests.adapters import HTTPAdapter, Retry

from strangeworks.errors.error import StrangeworksError
from strangeworks.transport import auth

PLATFORM_SDK_PATH = "sdk"


ALLOWED_HEADERS = {""}


class Operation:
    """Object for definining requests made to the platform."""

    def __init__(
        self,
        query: str,
        allowed_vars: Optional[List[str]] = None,
        upload_files: bool = False,
    ) -> None:
        """Initialize object

        Accepts a GraphQL query or mutation as a string. Derives variable names used by
        the query if none were provided.

        Parameters
        ----------
        query: str
            a GraphQL query or mutation as string.
        allowed_vars: Optional[List[str]]
            list to override which variables can be sent was part of query.
        """
        self.query = gql(query)
        self.allowed_vars = (
            allowed_vars
            if allowed_vars
            else list(
                map(
                    lambda x: x.variable.name.value,
                    self.query.definitions[0].variable_definitions,
                )
            )
        )
        self.upload_files = upload_files

    def variables(
        self, values: Optional[Dict[str, Any]] = None
    ) -> Optional[Dict[str, Any]]:

        if not self.allowed_vars:
            return values

        vars = {}
        for k, v in values.items():
            if k in self.allowed_vars and v is not None:
                vars[k] = v
        return vars


class StrangeworksTransport(RequestsHTTPTransport):
    """Transport layer with automatic token refresh."""

    def __init__(
        self,
        api_key: str,
        base_url: str,
        platform_ep: str = PLATFORM_SDK_PATH,
        auth_token: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
        retries: int = 0,
        **kvargs,
    ) -> None:
        self.platform_url = urljoin(base_url, platform_ep)
        self.api_key = api_key
        self.base_url = base_url
        super().__init__(
            url=self.platform_url,
            headers=headers,
            timeout=timeout,
            retries=retries,
        )

        self.auth_token = auth_token
        self.headers = headers or {}
        if self.auth_token:
            self.headers["Authorization"] = self.auth_token

    def connect(self):
        """Set up a session object.

        Creates a session object for the transport to use and configures retries and
        re-authentication.
        """
        if self.session is None:

            self.session = requests.Session()

            # set up retries.
            if self.retries > 0:
                adapter = HTTPAdapter(
                    max_retries=Retry(
                        total=self.retries,
                        backoff_factor=0.1,
                        status_forcelist=[500, 502, 503, 504],
                        allowed_methods=None,
                    )
                )

                for prefix in "http://", "https://":
                    self.session.mount(prefix, adapter)

            # setup token refresh if expired.
            self.session.hooks["response"].append(self._reauthenticate)

        self._refresh_token()

    def _refresh_token(self) -> None:
        self.auth_token = auth.get_token(self.api_key, self.base_url)
        self.headers["Authorization"] = f"Bearer {self.auth_token}"

    def _reauthenticate(self, res: requests.Response, **kwargs) -> requests.Response:
        """Reauthenticate to Strangeworks.

        Parameters
        ----------
        res : requests.Response
        **kwargs

        Returns
        -------
        : requests.Response
        """
        if res.status_code == requests.codes.unauthorized:
            seen_before_header = "X-SW-SDK-Re-Auth"
            # We've tried once before but no luck. Maybe they've changed their api_key?
            if res.request.headers.get(seen_before_header):
                raise StrangeworksError(
                    "Unable to re-authenticate your request. Utilize "
                    "strangeworks.authenticate(api_key) with your most up "
                    "to date credentials and try again."
                )

            self._refresh_token()

            # ensure that the new token is part of the header
            res.request.headers["Authorization"] = f"Bearer {self.auth_token}"
            res.request.headers[seen_before_header] = True
            return self.session.send(res.request)


class StrangeworksGQLClient:
    """Client for Platform API."""

    def __init__(
        self,
        base_url: str,
        api_key: Optional[str],
        auth_token: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: Optional[int] = None,
        retries: int = 0,
    ) -> None:
        """Initialize platform API client.

        Provides access to the platform API methods which allows python SDK clients to
        interact with the Strangeworks platform.

        Parameters
        ----------
        auth_token: str
            jwt token used to authorize requests to the platform API's.
        platform_url: str
            Base url for accessing the platform API.
        headers: Dict[str, str]
            Additional values to set in the header for the request. The header must
            belong to ALLOWED_HEADERS.
        """
        self.gql_client = Client(
            transport=StrangeworksTransport(
                base_url=base_url,
                api_key=api_key,
                auth_token=auth_token,
                headers=headers,
                retries=retries,
                timeout=timeout,
            )
        )

    def execute(self, op: Operation, **kvargs):
        """Execute an operation on the platform.
        Parameters
        ----------
        op: Operation
            which request to run
        variable_values; Optional[Dict[str, Any]]
            values to send with the request
        """
        try:
            result = self.gql_client.execute(
                document=op.query,
                variable_values=op.variables(kvargs),
                upload_files=op.upload_files,
            )
            return result
        except TransportQueryError as e:
            print(f"error during query: {e}")
            raise StrangeworksError.server_error(str(e.errors[0]), e.query_id)
