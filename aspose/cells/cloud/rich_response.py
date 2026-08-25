"""A rich HTTP response wrapper returned by the SDK client."""

import json
from typing import Any, Dict, Optional, Union


class RichResponse:
    """Wraps an HTTP response: status code, headers, and raw body.

    Attributes:
        status_code (int): HTTP status code.
        headers (Dict[str, str]): Response headers.
        body (bytes): The raw response body.
    """

    def __init__(
        self,
        status_code: int,
        headers: Optional[Dict[str, str]] = None,
        body: Optional[Union[bytes, str]] = None,
    ) -> None:
        self.status_code = status_code
        self.headers: Dict[str, str] = dict(headers or {})
        if body is None:
            self.body: bytes = b""
        elif isinstance(body, bytes):
            self.body = body
        else:
            self.body = body.encode("utf-8")

    def __str__(self) -> str:
        """Returns the body decoded as UTF-8."""
        return self.text()

    def text(self) -> str:
        """Returns the body decoded as UTF-8 (lossy for binary payloads)."""
        return self.body.decode("utf-8", errors="replace")

    def to_bytes(self) -> bytes:
        """Returns the raw body as bytes."""
        return self.body

    def get_json(self) -> Any:
        """Decodes the body as JSON and returns the resulting object.

        Raises:
            ValueError: if the body is not valid JSON.
        """
        return json.loads(self.text())

    def is_success(self) -> bool:
        """Returns ``True`` when the status code is in the 2xx range."""
        return 200 <= self.status_code < 300
