"""The Aspose.Cells Cloud SDK client."""

from __future__ import annotations

import json
import os
import threading
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import requests

from aspose.cells.cloud.configuration import Configuration
from aspose.cells.cloud.request_option import RequestOption
from aspose.cells.cloud.rich_response import RichResponse
from aspose.cells.cloud.sdk_error import SDKError
from aspose.cells.cloud.version import API_VERSION, USER_AGENT


class CellsCloudClient:
    """Client for the Aspose.Cells Cloud REST API.

    Authenticates using OAuth2 client-credentials and executes
    :class:`RequestOption` instances against the configured base URL.

    Args:
        client_id: Aspose Cloud Client ID.
        client_secret: Aspose Cloud Client Secret.
        base_url: Base URL (defaults to ``https://api.aspose.cloud``).
        auth_url: OAuth2 token endpoint. Defaults to the versioned production
            endpoint ``{base_url}/v{api_version}/cells/connect/token``.
        api_version: API version used for authentication (``"4.0"`` or
            ``"3.0"``); the token is acquired from the matching
            ``/v{api_version}/cells/connect/token`` endpoint.
        timeout: Request timeout in seconds.
        retries: Number of automatic retries on transient failures.
    """

    def __init__(
        self,
        client_id: str,
        client_secret: str,
        base_url: str = "https://api.aspose.cloud",
        auth_url: Optional[str] = None,
        api_version: str = "4.0",
        timeout: int = 300,
        retries: int = 0,
    ) -> None:
        if not client_id:
            raise ValueError("client_id is required")
        if not client_secret:
            raise ValueError("client_secret is required")

        self.configuration = Configuration(
            client_id=client_id,
            client_secret=client_secret,
            base_url=base_url,
            auth_url=auth_url,
            api_version=api_version,
            timeout=timeout,
            retries=retries,
        )

        self._session = requests.Session()
        self._token_lock = threading.Lock()
        self._access_token: Optional[str] = None
        self._token_expires_at: float = 0.0

    # ------------------------------------------------------------------ #
    # Configuration
    # ------------------------------------------------------------------ #
    def get_configuration(self) -> Configuration:
        """Returns the underlying :class:`Configuration`."""
        return self.configuration

    # ------------------------------------------------------------------ #
    # Authentication
    # ------------------------------------------------------------------ #
    def get_access_token(self) -> str:
        """Returns a valid OAuth2 access token (cached until near expiry).

        The token is acquired from the versioned token endpoint
        ``{base_url}/v{api_version}/cells/connect/token`` (see
        :meth:`aspose.cells.cloud.configuration.Configuration.get_auth_url`).
        """
        return self._request_oauth_token()

    def _request_oauth_token(self) -> str:
        """Acquires (and caches) an OAuth2 access token via client credentials."""
        with self._token_lock:
            if self._access_token and time.time() < self._token_expires_at - 60:
                return self._access_token

            payload = {
                "grant_type": "client_credentials",
                "client_id": self.configuration.client_id,
                "client_secret": self.configuration.client_secret,
            }
            response = self._session.post(
                self.configuration.auth_url,
                data=payload,
                timeout=self.configuration.timeout,
            )
            if response.status_code >= 400:
                raise SDKError(
                    "Failed to acquire OAuth2 access token: %s" % response.text[:512],
                    status_code=response.status_code,
                    body=response.text,
                )

            token_data = response.json()
            self._access_token = token_data.get("access_token")
            if not self._access_token:
                raise SDKError("OAuth2 token response did not contain an access token.")

            expires_in = int(token_data.get("expires_in", 3600))
            self._token_expires_at = time.time() + expires_in
            return self._access_token

    # ------------------------------------------------------------------ #
    # Request execution
    # ------------------------------------------------------------------ #
    def _authorization_headers(self) -> Dict[str, str]:
        token = self._request_oauth_token()
        return {
            "Authorization": "Bearer %s" % token,
            "x-aspose-client": USER_AGENT,
            "x-aspose-client-version": API_VERSION,
            "Accept": "application/json",
        }

    @staticmethod
    def _to_query_string(params: Optional[Dict[str, Any]]) -> Optional[Dict[str, str]]:
        """Normalises query parameter values to strings."""
        if not params:
            return None
        result: Dict[str, str] = {}
        for key, value in params.items():
            if value is None:
                continue
            if isinstance(value, bool):
                result[key] = "true" if value else "false"
            else:
                result[key] = str(value)
        return result or None

    @staticmethod
    def _is_file_value(value: Any) -> bool:
        """Returns ``True`` when a form value denotes a file part.

        A form value is treated as a file when it is:
          * an existing local file path (``str`` or :class:`pathlib.Path`),
          * raw binary content (``bytes`` / ``bytearray`` / ``memoryview``),
          * a file-like object exposing ``.read()``,
          * a ``requests``-style ``(filename, content[, content_type])`` tuple.

        Anything else is sent as a plain multipart form field.
        """
        if isinstance(value, (bytes, bytearray, memoryview)):
            return True
        if hasattr(value, "read"):
            return True
        if isinstance(value, (str, Path)):
            return os.path.isfile(value)
        if isinstance(value, tuple) and len(value) in (2, 3, 4):
            return True
        return False

    @staticmethod
    def _file_part(field_name: str, value: Any) -> Tuple[str, Tuple[Any, ...]]:
        """Normalises one form value into a ``requests`` file tuple.

        Returns ``(field_name, (filename, fileobj[, content_type]))``. The
        ``requests`` library sets the multipart ``Content-Type`` (with boundary)
        from this tuple, so no literal ``Content-Type`` header is needed.
        """
        # ``requests``-style tuple: (filename, content[, content_type[, headers]]).
        if isinstance(value, tuple) and len(value) in (2, 3, 4):
            if len(value) == 2:
                return (field_name, (str(value[0]), value[1], "application/octet-stream"))
            return (field_name, value)

        # Raw binary content -- the filename defaults to the wire field name.
        if isinstance(value, (bytes, bytearray, memoryview)):
            return (field_name, (field_name, bytes(value), "application/octet-stream"))

        # File-like object -- use ``.name`` when present, else the field name.
        if hasattr(value, "read"):
            filename = getattr(value, "name", None) or field_name
            return (field_name, (str(filename), value, "application/octet-stream"))

        # Local file path (str / pathlib.Path).
        return (
            field_name,
            (os.path.basename(str(value)), open(value, "rb"), "application/octet-stream"),
        )

    def _build_files(self, form: Dict[str, Any]) -> List[Any]:
        """Builds a ``requests`` multipart file list from a form mapping."""
        files: List[Any] = []
        for field_name, value in form.items():
            if self._is_file_value(value):
                files.append(self._file_part(field_name, value))
        return files

    @staticmethod
    def _build_data(form: Dict[str, Any]) -> Dict[str, str]:
        """Collects non-file form fields for multipart ``data``."""
        data: Dict[str, str] = {}
        for field_name, value in form.items():
            if CellsCloudClient._is_file_value(value):
                continue
            if isinstance(value, (dict, list)):
                data[field_name] = json.dumps(value)
            elif value is not None:
                data[field_name] = str(value)
        return data

    def do(self, request: RequestOption) -> RichResponse:
        """Executes a single request and returns a :class:`RichResponse`.

        Raises:
            SDKError: on authentication or transport failures.
        """
        method = request.get_method()
        path = request.get_path()
        url = self.configuration.get_base_url() + path

        headers = self._authorization_headers()
        headers.update(self.configuration.header_parameters)
        headers.update(request.get_header_parameters())

        params = self._to_query_string(request.get_query_parameters())
        json_body = request.get_json_body()
        form = request.get_multipart_form()

        last_error: Optional[Exception] = None
        attempts = max(1, self.configuration.retries + 1)

        for attempt in range(attempts):
            try:
                if form:
                    files = self._build_files(form)
                    data = self._build_data(form)
                    # ``requests`` sets the multipart ``Content-Type`` together
                    # with its boundary; forwarding a literal
                    # ``multipart/form-data`` header would omit the boundary and
                    # break the upload.
                    headers.pop("Content-Type", None)
                    # When a request carries both a multipart payload and a
                    # JSON body, the body is attached as a form field.
                    if json_body is not None:
                        data = data or {}
                        body_field = self._body_field_name(request)
                        data[body_field] = (
                            json.dumps(json_body, default=str)
                            if not isinstance(json_body, str)
                            else json_body
                        )
                    response = self._session.request(
                        method,
                        url,
                        params=params,
                        headers=headers,
                        files=files or None,
                        data=data or None,
                        timeout=self.configuration.timeout,
                    )
                elif json_body is not None:
                    response = self._session.request(
                        method,
                        url,
                        params=params,
                        headers=headers,
                        json=json_body,
                        timeout=self.configuration.timeout,
                    )
                else:
                    response = self._session.request(
                        method,
                        url,
                        params=params,
                        headers=headers,
                        timeout=self.configuration.timeout,
                    )
                return RichResponse(
                    status_code=response.status_code,
                    headers=dict(response.headers),
                    body=response.content,
                )
            except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as exc:
                last_error = exc
                if attempt + 1 < attempts:
                    time.sleep(0.5 * (attempt + 1))
                    continue
                break

        raise SDKError(
            "Request to %s failed after %d attempt(s): %s"
            % (url, attempts, last_error or "unknown transport error")
        )

    @staticmethod
    def _body_field_name(request: RequestOption) -> str:
        """Best-effort name for the JSON body when attached to a multipart form."""
        for candidate in ("cellsDocuments", "protectWorkbookRequest", "data", "body"):
            if candidate in request.get_multipart_form():
                continue
            return candidate
        return "data"

    def do_batch(self, *requests: RequestOption) -> List[RichResponse]:
        """Executes several requests in order and returns their responses."""
        return [self.do(req) for req in requests]

    # ------------------------------------------------------------------ #
    # Storage helpers
    # ------------------------------------------------------------------ #
    def upload_file(
        self,
        local_path: str,
        remote_path: str,
        storage_name: Optional[str] = None,
    ) -> RichResponse:
        """Uploads a local file to cloud storage.

        Args:
            local_path: Path to the local file.
            remote_path: Destination path in cloud storage.
            storage_name: Optional storage name.

        Returns:
            The upload response.
        """
        if not os.path.isfile(local_path):
            raise ValueError("local file not found: %s" % local_path)

        from aspose.cells.cloud.request.upload_file_request import UploadFileRequest

        request = UploadFileRequest(
            path=remote_path,
            upload_files=local_path,
            storage_name=storage_name,
        )
        return self.do(request)

    def download_file(
        self,
        remote_path: str,
        storage_name: Optional[str] = None,
    ) -> RichResponse:
        """Downloads a file from cloud storage."""
        from aspose.cells.cloud.request.download_file_request import DownloadFileRequest

        request = DownloadFileRequest(
            path=remote_path,
            storage_name=storage_name,
        )
        return self.do(request)
