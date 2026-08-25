"""Abstract base class for every API request in the SDK."""

from abc import ABC, abstractmethod
from typing import Any, Dict, Optional


class RequestOption(ABC):
    """The interface every request class implements.

    A request knows how to describe itself to the HTTP layer: the verb, the
    path (with placeholders already substituted), query parameters, headers,
    an optional JSON body, and an optional multipart form payload.
    """

    @abstractmethod
    def get_method(self) -> str:
        """Returns the HTTP verb as an uppercase string (GET/POST/PUT/DELETE)."""

    @abstractmethod
    def get_path(self) -> str:
        """Returns the request path with every ``{param}`` already substituted
        and URL-encoded."""

    def get_query_parameters(self) -> Dict[str, str]:
        """Returns the query string parameters (name -> value)."""
        return {}

    def get_header_parameters(self) -> Dict[str, str]:
        """Returns request-specific headers (notably ``Content-Type``)."""
        return {}

    def get_json_body(self) -> Optional[Any]:
        """Returns the JSON-serializable request body, or ``None``."""
        return None

    def get_multipart_form(self) -> Optional[Dict[str, Any]]:
        """Returns the multipart form fields (name -> value), or ``None``.

        File upload fields map the parameter name to a local file path.
        """
        return None
