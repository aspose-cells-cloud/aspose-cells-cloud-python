"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetSparklineGroupRequest(RequestOption):
    """Add a sparkline group in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        type_: str,
        data_range: str,
        is_vertical: bool,
        location_range: str,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if not type_:
            raise ValueError("type is required")
        if not data_range:
            raise ValueError("dataRange is required")
        if is_vertical is None:
            raise ValueError("isVertical is required")
        if not location_range:
            raise ValueError("locationRange is required")
        self.name = name
        self.sheet_name = sheet_name
        self.type_ = type_
        self.data_range = data_range
        self.is_vertical = is_vertical
        self.location_range = location_range
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
            "/sparklineGroups"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["type"] = self.type_
        params["dataRange"] = self.data_range
        params["isVertical"] = "true" if self.is_vertical else "false"
        params["locationRange"] = self.location_range
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
