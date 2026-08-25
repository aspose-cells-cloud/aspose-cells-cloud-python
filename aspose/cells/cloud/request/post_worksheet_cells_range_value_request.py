"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorksheetCellsRangeValueRequest(RequestOption):
    """Assign a value to the range; if necessary, the value will be converted to another data type, and the cell's number format will be reset."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        range_: Range,
        value: str,
        is_converted: Optional[bool] = None,
        set_style: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if range_ is None:
            raise ValueError("range is required")
        if not value:
            raise ValueError("Value is required")
        self.name = name
        self.sheet_name = sheet_name
        self.range_ = range_
        self.value = value
        self.is_converted = is_converted
        self.set_style = set_style
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
            "/ranges/value"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["Value"] = self.value
        if self.is_converted is not None:
            params["isConverted"] = "true" if self.is_converted else "false"
        if self.set_style is not None:
            params["setStyle"] = "true" if self.set_style else "false"
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
