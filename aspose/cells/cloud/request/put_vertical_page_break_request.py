"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutVerticalPageBreakRequest(RequestOption):
    """Add a vertical page break in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        cellname: Optional[str] = None,
        column: Optional[int] = None,
        row: Optional[int] = None,
        start_row: Optional[int] = None,
        end_row: Optional[int] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.cellname = cellname
        self.column = column
        self.row = row
        self.start_row = start_row
        self.end_row = end_row
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/verticalpagebreaks"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.cellname:
            params["cellname"] = self.cellname
        if self.column is not None:
            params["column"] = str(self.column)
        if self.row is not None:
            params["row"] = str(self.row)
        if self.start_row is not None:
            params["startRow"] = str(self.start_row)
        if self.end_row is not None:
            params["endRow"] = str(self.end_row)
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
