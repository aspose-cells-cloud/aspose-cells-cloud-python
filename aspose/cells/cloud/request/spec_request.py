"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class SpecRequest(RequestOption):
    """Get the specifications"""

    def __init__(
        self,
        version: str,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not version:
            raise ValueError("version is required")
        self.version = version
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return "/v4.0/cells/swagger/spec"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["version"] = self.version
        if self.region:
            params["region"] = self.region
        if self.password:
            params["password"] = self.password
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
