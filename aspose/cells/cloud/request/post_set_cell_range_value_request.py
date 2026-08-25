"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostSetCellRangeValueRequest(RequestOption):
    """Set the value of the range in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        cellarea: str,
        value: str,
        type_: str,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if not cellarea:
            raise ValueError("cellarea is required")
        if not value:
            raise ValueError("value is required")
        if not type_:
            raise ValueError("type is required")
        self.name = name
        self.sheet_name = sheet_name
        self.cellarea = cellarea
        self.value = value
        self.type_ = type_
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
            "/cells"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["cellarea"] = self.cellarea
        params["value"] = self.value
        params["type"] = self.type_
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
