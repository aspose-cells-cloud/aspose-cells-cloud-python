"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorksheetCellsRangeRowHeightRequest(RequestOption):
    """Sets row height of range."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        range_: Range,
        value: float,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if range_ is None:
            raise ValueError("range is required")
        if value is None:
            raise ValueError("value is required")
        self.name = name
        self.sheet_name = sheet_name
        self.range_ = range_
        self.value = value
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
            "/ranges/rowHeight"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["value"] = str(self.value)
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
