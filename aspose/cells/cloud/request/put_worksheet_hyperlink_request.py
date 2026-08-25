"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetHyperlinkRequest(RequestOption):
    """Add hyperlink in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        first_row: int,
        first_column: int,
        total_rows: int,
        total_columns: int,
        address: str,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if first_row is None:
            raise ValueError("firstRow is required")
        if first_column is None:
            raise ValueError("firstColumn is required")
        if total_rows is None:
            raise ValueError("totalRows is required")
        if total_columns is None:
            raise ValueError("totalColumns is required")
        if not address:
            raise ValueError("address is required")
        self.name = name
        self.sheet_name = sheet_name
        self.first_row = first_row
        self.first_column = first_column
        self.total_rows = total_rows
        self.total_columns = total_columns
        self.address = address
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
            "/hyperlinks"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["firstRow"] = str(self.first_row)
        params["firstColumn"] = str(self.first_column)
        params["totalRows"] = str(self.total_rows)
        params["totalColumns"] = str(self.total_columns)
        params["address"] = self.address
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
