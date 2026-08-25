"""Runtime configuration for the Aspose.Cells Cloud SDK for Python."""

from typing import Dict, Optional

DEFAULT_BASE_URL = "https://api.aspose.cloud"
DEFAULT_API_VERSION = "4.0"
DEFAULT_AUTH_URL = "https://api.aspose.cloud/v4.0/cells/connect/token"
DEFAULT_TIMEOUT = 300  # seconds
DEFAULT_RETRIES = 0


class Configuration:
    """Holds client credentials, endpoint, and transport settings.

    Attributes:
        client_id (Optional[str]): Aspose Cloud Client ID.
        client_secret (Optional[str]): Aspose Cloud Client Secret.
        base_url (str): Base URL of the Aspose Cloud API.
        auth_url (str): OAuth2 token endpoint. When not provided it is derived
            from ``base_url`` and ``api_version`` as
            ``{base_url}/v{api_version}/cells/connect/token``.
        api_version (str): API version used for authentication (``"4.0"`` or
            ``"3.0"``).
        timeout (int): Request timeout in seconds.
        retries (int): Number of automatic retries for idempotent failures.
        header_parameters (Dict[str, str]): Default headers applied to every
            request.
    """

    def __init__(
        self,
        client_id: Optional[str] = None,
        client_secret: Optional[str] = None,
        base_url: str = DEFAULT_BASE_URL,
        auth_url: Optional[str] = None,
        api_version: str = DEFAULT_API_VERSION,
        timeout: int = DEFAULT_TIMEOUT,
        retries: int = DEFAULT_RETRIES,
        header_parameters: Optional[Dict[str, str]] = None,
    ) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = base_url
        self.api_version = api_version
        self.auth_url = auth_url or self.get_auth_url()
        self.timeout = timeout
        self.retries = retries
        # A fresh dict is created per instance to avoid the shared-mutable-
        # default pitfall.
        self.header_parameters: Dict[str, str] = dict(header_parameters or {})

    def get_auth_url(self) -> str:
        """Returns the versioned OAuth2 token endpoint.

        The access token is acquired from ``{base_url}/v{api_version}/cells/connect/token``
        (e.g. ``https://api.aspose.cloud/v4.0/cells/connect/token``). The old
        unversioned ``/connect/token`` endpoint (and the historical v1.1 OAuth
        endpoint) are no longer used.
        """
        version = str(self.api_version)
        if version.startswith("v"):
            version = version[1:]
        return "%s/v%s/cells/connect/token" % (self.get_base_url(), version)

    def add_default_header(self, key: str, value: str) -> "Configuration":
        """Adds or replaces a default header applied to every request.

        Returns ``self`` to allow chaining.
        """
        self.header_parameters[key] = value
        return self

    def remove_default_header(self, key: str) -> "Configuration":
        """Removes a default header, if present."""
        self.header_parameters.pop(key, None)
        return self

    def get_base_url(self) -> str:
        """Returns the base URL (without a trailing slash)."""
        return self.base_url.rstrip("/")
