"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class PostLockRequest(RequestOption):
    """Lock Excel files."""

    def __init__(
        self,
        file: FileSource,
        password: str,
    ):
        if not file:
            raise ValueError("File is required")
        if not password:
            raise ValueError("password is required")
        self.file = file
        self.password = password

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/lock"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["password"] = self.password
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"File": self.file}
