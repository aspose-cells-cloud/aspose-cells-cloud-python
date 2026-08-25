"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostSetWorksheetColumnWidthRequest(RequestOption):
    """Set worksheet column width."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        column_index: int,
        width: float,
        count: Optional[int] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if column_index is None:
            raise ValueError("columnIndex is required")
        if width is None:
            raise ValueError("width is required")
        self.name = name
        self.sheet_name = sheet_name
        self.column_index = column_index
        self.width = width
        self.count = count
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/cells/columns/" +
            quote(str(self.column_index), safe="/")
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["width"] = str(self.width)
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
