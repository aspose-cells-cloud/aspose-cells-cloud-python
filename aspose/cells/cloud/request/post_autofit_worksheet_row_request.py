"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostAutofitWorksheetRowRequest(RequestOption):
    """Autofit a row in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        row_index: int,
        first_column: Optional[int] = None,
        last_column: Optional[int] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        row_count: Optional[int] = None,
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
        self.first_column = first_column
        self.last_column = last_column
        self.folder = folder
        self.storage_name = storage_name
        self.row_count = row_count

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/autofitrow"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["rowIndex"] = str(self.row_index)
        if self.first_column is not None:
            params["firstColumn"] = str(self.first_column)
        if self.last_column is not None:
            params["lastColumn"] = str(self.last_column)
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.row_count is not None:
            params["rowCount"] = str(self.row_count)
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
