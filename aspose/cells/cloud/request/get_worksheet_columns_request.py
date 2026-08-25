"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class GetWorksheetColumnsRequest(RequestOption):
    """Retrieve descriptions of worksheet columns."""

    def __init__(
        self,
        name: Optional[str] = None,
        sheet_name: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        self.name = name
        self.sheet_name = sheet_name
        self.offset = offset
        self.count = count
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/cells/columns/"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.offset is not None:
            params["offset"] = str(self.offset)
        if self.count is not None:
            params["count"] = str(self.count)
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
