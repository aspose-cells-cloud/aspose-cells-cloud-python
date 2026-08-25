"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetListObjectRequest(RequestOption):
    """Add a ListObject in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        start_row: Optional[int] = None,
        start_column: Optional[int] = None,
        end_row: Optional[int] = None,
        end_column: Optional[int] = None,
        folder: Optional[str] = None,
        has_headers: Optional[bool] = None,
        display_name: Optional[str] = None,
        show_totals: Optional[bool] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.start_row = start_row
        self.start_column = start_column
        self.end_row = end_row
        self.end_column = end_column
        self.folder = folder
        self.has_headers = has_headers
        self.display_name = display_name
        self.show_totals = show_totals
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/listobjects"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.start_row is not None:
            params["startRow"] = str(self.start_row)
        if self.start_column is not None:
            params["startColumn"] = str(self.start_column)
        if self.end_row is not None:
            params["endRow"] = str(self.end_row)
        if self.end_column is not None:
            params["endColumn"] = str(self.end_column)
        if self.folder:
            params["folder"] = self.folder
        if self.has_headers is not None:
            params["hasHeaders"] = "true" if self.has_headers else "false"
        if self.display_name:
            params["displayName"] = self.display_name
        if self.show_totals is not None:
            params["showTotals"] = "true" if self.show_totals else "false"
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
