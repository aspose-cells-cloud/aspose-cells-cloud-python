"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class GetWorksheetCellsRangeValueRequest(RequestOption):
    """Retrieve the values of cells within the specified range."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        namerange: Optional[str] = None,
        first_row: Optional[int] = None,
        first_column: Optional[int] = None,
        row_count: Optional[int] = None,
        column_count: Optional[int] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.namerange = namerange
        self.first_row = first_row
        self.first_column = first_column
        self.row_count = row_count
        self.column_count = column_count
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
            "/ranges/value"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.namerange:
            params["namerange"] = self.namerange
        if self.first_row is not None:
            params["firstRow"] = str(self.first_row)
        if self.first_column is not None:
            params["firstColumn"] = str(self.first_column)
        if self.row_count is not None:
            params["rowCount"] = str(self.row_count)
        if self.column_count is not None:
            params["columnCount"] = str(self.column_count)
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
