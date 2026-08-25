"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostUpdateWorksheetRowRequest(RequestOption):
    """Update height of rows in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        row_index: int,
        height: Optional[float] = None,
        count: Optional[int] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if row_index is None:
            raise ValueError("rowIndex is required")
        self.name = name
        self.sheet_name = sheet_name
        self.row_index = row_index
        self.height = height
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
            "/cells/rows/" +
            quote(str(self.row_index), safe="/")
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.height is not None:
            params["height"] = str(self.height)
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
