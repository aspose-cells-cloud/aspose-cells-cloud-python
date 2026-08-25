"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetFilterTop10Request(RequestOption):
    """Filter the top 10 items in the list in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        range_: str,
        field_index: int,
        is_top: bool,
        is_percent: bool,
        item_count: int,
        match_blanks: Optional[bool] = None,
        refresh: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if not range_:
            raise ValueError("range is required")
        if field_index is None:
            raise ValueError("fieldIndex is required")
        if is_top is None:
            raise ValueError("isTop is required")
        if is_percent is None:
            raise ValueError("isPercent is required")
        if item_count is None:
            raise ValueError("itemCount is required")
        self.name = name
        self.sheet_name = sheet_name
        self.range_ = range_
        self.field_index = field_index
        self.is_top = is_top
        self.is_percent = is_percent
        self.item_count = item_count
        self.match_blanks = match_blanks
        self.refresh = refresh
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
            "/autoFilter/filterTop10"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["range"] = self.range_
        params["fieldIndex"] = str(self.field_index)
        params["isTop"] = "true" if self.is_top else "false"
        params["isPercent"] = "true" if self.is_percent else "false"
        params["itemCount"] = str(self.item_count)
        if self.match_blanks is not None:
            params["matchBlanks"] = "true" if self.match_blanks else "false"
        if self.refresh is not None:
            params["refresh"] = "true" if self.refresh else "false"
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
