"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class PostProtectRequest(RequestOption):
    """Excel files encryption."""

    def __init__(
        self,
        file: FileSource,
        protect_workbook_request: ProtectWorkbookRequest,
        password: Optional[str] = None,
    ):
        if not file:
            raise ValueError("File is required")
        if protect_workbook_request is None:
            raise ValueError("protectWorkbookRequest is required")
        self.file = file
        self.protect_workbook_request = protect_workbook_request
        self.password = password

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/protect"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.password:
            params["password"] = self.password
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        form = {}
        if self.file is not None:
            form["File"] = self.file
        if self.protect_workbook_request is not None:
            form["protectWorkbookRequest"] = json.dumps(self.protect_workbook_request.to_dict(), default=str)
        return form
