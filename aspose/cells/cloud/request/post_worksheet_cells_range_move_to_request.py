"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorksheetCellsRangeMoveToRequest(RequestOption):
    """Move the current range to the destination range."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        range_: Range,
        dest_row: int,
        dest_column: int,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if range_ is None:
            raise ValueError("range is required")
        if dest_row is None:
            raise ValueError("destRow is required")
        if dest_column is None:
            raise ValueError("destColumn is required")
        self.name = name
        self.sheet_name = sheet_name
        self.range_ = range_
        self.dest_row = dest_row
        self.dest_column = dest_column
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
            "/ranges/moveto"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["destRow"] = str(self.dest_row)
        params["destColumn"] = str(self.dest_column)
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.range_.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
