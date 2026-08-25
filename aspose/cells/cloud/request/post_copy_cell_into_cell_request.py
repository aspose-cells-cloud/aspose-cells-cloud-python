"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostCopyCellIntoCellRequest(RequestOption):
    """Copy data from a source cell to a destination cell in the worksheet."""

    def __init__(
        self,
        name: str,
        dest_cell_name: str,
        sheet_name: str,
        worksheet: str,
        cellname: Optional[str] = None,
        row: Optional[int] = None,
        column: Optional[int] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not dest_cell_name:
            raise ValueError("destCellName is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if not worksheet:
            raise ValueError("worksheet is required")
        self.name = name
        self.dest_cell_name = dest_cell_name
        self.sheet_name = sheet_name
        self.worksheet = worksheet
        self.cellname = cellname
        self.row = row
        self.column = column
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
            "/cells/" +
            quote(self.dest_cell_name, safe="/") +
            "/copy"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["worksheet"] = self.worksheet
        if self.cellname:
            params["cellname"] = self.cellname
        if self.row is not None:
            params["row"] = str(self.row)
        if self.column is not None:
            params["column"] = str(self.column)
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
