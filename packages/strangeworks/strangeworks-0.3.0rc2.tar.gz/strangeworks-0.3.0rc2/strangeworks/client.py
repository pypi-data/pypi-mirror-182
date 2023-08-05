"""client.py."""
import importlib.metadata
import os
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

from strangeworks.config.base import ConfigSource
from strangeworks.errors.error import StrangeworksError
from strangeworks.transport import jobs, resource, workspace
from strangeworks.transport.backends import Backend, get_backend, get_backends
from strangeworks.transport.gql_client import StrangeworksGQLClient
from strangeworks.transport.jobs import Job
from strangeworks.transport.resource import Resource
from strangeworks.transport.rest_client import StrangeworksRestClient
from strangeworks.transport.workspace import Workspace

__version__ = importlib.metadata.version("strangeworks")


class Client:
    """Strangeworks client object."""

    def __init__(
        self,
        cfg: ConfigSource,
        headers: Optional[Dict[str, str]] = None,
        rest_client: Optional[StrangeworksRestClient] = None,
        gql_client: Optional[StrangeworksGQLClient] = None,
        **kwargs,
    ) -> None:
        """Strangeworks client.

        Implements the Strangeworks API and provides core functionality for cross-vendor
        applications.

        Parameters
        ----------
        cfg: ConfigSource
            Source for retrieving SDK configuration values.
        headers : Optional[Dict[str, str]]
            Headers that are sent as part of the request to Strangeworks.
        rest_client : Optional[StrangeworksRestClient]
        **kwargs
            Other keyword arguments to pass to tools like ``requests``.
        """
        self.cfg = cfg
        self.kwargs = kwargs

        self.headers = (
            os.getenv("STRANGEWORKS_HEADERS", default=None)
            if headers is None
            else headers
        )

        self.rest_client = rest_client
        self.gql_client = gql_client

    def _is_authenticated(self) -> bool:
        """Return whether client has been authenticated.

        Return
        ------
        bool
            True if client has been authenticated, False otherwise.
        """
        return self.rest_client and self.gql_client

    def authenticate(
        self,
        api_key: str,
        url: Optional[str] = None,
        profile: Optional[str] = None,
        store_credentials: bool = True,
        overwrite: bool = False,
        **kwargs,
    ) -> None:
        """Authenticate to Strangeworks.

        Obtains an authorization token from the platform using the api_key. The auth
        token is used to make calls to the platform.

        Parameters
        ----------
        api_key : Optional[str]
            The API key.
        url: Optional[str]
            The base URL to the Strangeworks API.
        profile: Optional[str]
            The profile name to use for configuration.
        store_credentials: bool
            Indicates whether credentials (api key an url)  should be saved. Defaults
            to True.
        overwrite: bool
            Indicates whether to overwrite credentials if they already exist. Defaults
            to False.
        **kwargs
            Additional arguments.
        """
        key = api_key or self.cfg.get("api_key")

        if key is None:
            raise StrangeworksError.authentication_error(
                message="Unable to retrieve api key from configuration. Please retry with your api_key."
            )

        # create new clients w/ auth in place
        self.gql_client = StrangeworksGQLClient(
            api_key=key,
            base_url=url or self.cfg.get("url"),
        )

        self.rest_client = StrangeworksRestClient(
            api_key=key, host=url or self.cfg.get("url")
        )

        # if we made it this far, lets go ahead and try to save the configuration to a
        # file.
        if api_key and store_credentials:
            self.cfg.set(
                profile=profile,
                overwrite=overwrite,
                api_key=api_key,
                url=self.rest_client.get_host(),
            )

    def resources(self, slug: Optional[str] = None) -> Optional[List[Resource]]:
        """Retrieve list of resources that are available for this workspace account.


        Parameters
        ----------
        slug: Optional[str]
            Identifier for a specific resource. Defaults to None.

        Return
        ------
        Optional[List[Resource]]
            List of resources for the current workspace account or None if no resources
            have been created.
        """
        return resource.get(client=self.gql_client, resource_slug=slug)

    def jobs(
        self,
        slug: Optional[str] = None,
        resource_slugs: Optional[List[str]] = None,
        product_slugs: Optional[List[str]] = None,
        statuses: Optional[List[str]] = None,
    ) -> Job:
        """Retrieve list of jobs associated with the current workspace account.

        Parameters
        ----------
        slug : Optional[str] = None
            Identifier for a specific job. Defaults to None.
        resource_slugs: Optional[List[str]]
            List of resource identifiers. Only jobs whose resources match will be
            returned. Defaults to None.
        product_slugs: Optional[List[str]]
            List of product identifiers. Only jobs whose product slugs match will be
            returned. Defaults to None.
        statuses: Optional[List[str]]
            List of job statuses. Only obs whose statuses match will be returned.
            Defaults to None.

        Return
        -------
        : Optional[List[Job]]
            List of jobs or None if there are no jobs that match selection criteria.
        """
        return jobs.get(
            client=self.gql_client,
            job_slug=slug,
            product_slugs=product_slugs or [],
            resource_slugs=resource_slugs or [],
            statuses=statuses or [],
        )

    def workspace_info(self) -> Workspace:
        """Retrieve information about the current workspace."""
        return workspace.get(self.gql_client)

    def execute(
        self,
        res: resource.Resource,
        payload: Optional[Dict[str, Any]] = None,
        endpoint: Optional[str] = None,
    ):
        """Execute a job request.

        Parameters
        ----------
        res: resource.Resource
            the resource that has the function to call.
        payload: Optiona;[Dict[str, Any]]
            the payload to send with the request.
        endpoint:
            additional endpoint to append to the proxy path for the resource.

        """
        if endpoint:
            url = urljoin(res.proxy_url(), endpoint)

        if payload:
            return self.rest_client.post(
                url=url,
                json=payload,
            )

        return self.rest_client.get(url=url)

    def get_backends(
        self,
        product_slugs: List[str] = None,
        backend_type_slugs: List[str] = None,
        backend_statuses: List[str] = None,
        backend_tags: List[str] = None,
    ) -> List[Backend]:
        """Return a list of backends available based on the filters provided.

        Replaces the deprecated BackendsService.
        """
        return get_backends(
            client=self.gql_client,
            product_slugs=product_slugs,
            backend_type_slugs=backend_type_slugs,
            backend_statuses=backend_statuses,
            backend_tags=backend_tags,
        )

    def get_backend(self, backend_slug: str) -> Backend:
        """Return a single backend by the slug.

        Replaces the deprecated BackendsService.
        """
        return get_backend(self.gql_client, backend_slug)
