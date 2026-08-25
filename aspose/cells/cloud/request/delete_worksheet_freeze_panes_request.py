"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class DeleteWorksheetFreezePanesRequest(RequestOption):
    """Unfreeze panes in worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        row: int,
        column: int,
        freezed_rows: int,
        freezed_columns: int,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if row is None:
            raise ValueError("row is required")
        if column is None:
            raise ValueError("column is required")
        if freezed_rows is None:
            raise ValueError("freezedRows is required")
        if freezed_columns is None:
            raise ValueError("freezedColumns is required")
        self.name = name
        self.sheet_name = sheet_name
        self.row = row
        self.column = column
        self.freezed_rows = freezed_rows
        self.freezed_columns = freezed_columns
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "DELETE"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/freezepanes"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["row"] = str(self.row)
        params["column"] = str(self.column)
        params["freezedRows"] = str(self.freezed_rows)
        params["freezedColumns"] = str(self.freezed_columns)
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
