"""Exception types raised by the Aspose.Cells Cloud SDK for Python."""


class SDKError(Exception):
    """Raised for SDK-level failures such as authentication, transport, or
    non-2xx HTTP responses.

    Attributes:
        status_code (Optional[int]): HTTP status code, when available.
        body (Optional[str]): The raw response body, when available.
        message (str): A human-readable error description.
    """

    def __init__(
        self,
        message: str,
        status_code: int = None,
        body: str = None,
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.body = body
        super().__init__(message)

    def __str__(self) -> str:  # pragma: no cover - trivial
        if self.status_code is not None:
            return "[%s] %s" % (self.status_code, self.message)
        return self.message


class ApiException(SDKError):
    """Raised when the Aspose Cloud API returns an error response."""

    def __init__(self, status_code: int, body: str = None) -> None:
        message = "The Aspose Cloud API returned an error."
        if body:
            message = "%s Response body: %s" % (message, body[:512])
        super().__init__(message, status_code=status_code, body=body)


class AuthError(SDKError):
    """Raised when OAuth2 token acquisition fails."""


class InvalidArgumentException(ValueError):
    """Raised when a caller supplies an invalid local argument.

    This is kept as a distinct ``ValueError`` subclass so that callers may
    distinguish SDK validation failures from other ``ValueError`` instances.
    """
