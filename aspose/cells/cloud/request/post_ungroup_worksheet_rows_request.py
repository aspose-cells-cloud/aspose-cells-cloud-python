"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostUngroupWorksheetRowsRequest(RequestOption):
    """Ungroup rows in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        first_index: int,
        last_index: int,
        is_all: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if first_index is None:
            raise ValueError("firstIndex is required")
        if last_index is None:
            raise ValueError("lastIndex is required")
        self.name = name
        self.sheet_name = sheet_name
        self.first_index = first_index
        self.last_index = last_index
        self.is_all = is_all
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
            "/cells/rows/ungroup"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["firstIndex"] = str(self.first_index)
        params["lastIndex"] = str(self.last_index)
        if self.is_all is not None:
            params["isAll"] = "true" if self.is_all else "false"
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
