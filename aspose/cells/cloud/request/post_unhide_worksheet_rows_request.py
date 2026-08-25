"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostUnhideWorksheetRowsRequest(RequestOption):
    """Unhide rows in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        startrow: int,
        total_rows: int,
        height: Optional[float] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if startrow is None:
            raise ValueError("startrow is required")
        if total_rows is None:
            raise ValueError("totalRows is required")
        self.name = name
        self.sheet_name = sheet_name
        self.startrow = startrow
        self.total_rows = total_rows
        self.height = height
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
            "/cells/rows/unhide"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["startrow"] = str(self.startrow)
        params["totalRows"] = str(self.total_rows)
        if self.height is not None:
            params["height"] = str(self.height)
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
