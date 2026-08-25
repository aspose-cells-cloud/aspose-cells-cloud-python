"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostPivotTableFieldHideItemRequest(RequestOption):
    """Hide a pivot field item in the PivotTable."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        pivot_table_index: int,
        pivot_field_type: str,
        field_index: int,
        item_index: int,
        is_hide: bool,
        need_re_calculate: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if pivot_table_index is None:
            raise ValueError("pivotTableIndex is required")
        if not pivot_field_type:
            raise ValueError("pivotFieldType is required")
        if field_index is None:
            raise ValueError("fieldIndex is required")
        if item_index is None:
            raise ValueError("itemIndex is required")
        if is_hide is None:
            raise ValueError("isHide is required")
        self.name = name
        self.sheet_name = sheet_name
        self.pivot_table_index = pivot_table_index
        self.pivot_field_type = pivot_field_type
        self.field_index = field_index
        self.item_index = item_index
        self.is_hide = is_hide
        self.need_re_calculate = need_re_calculate
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
            "/pivottables/" +
            quote(str(self.pivot_table_index), safe="/") +
            "/PivotField/Hide"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["pivotFieldType"] = self.pivot_field_type
        params["fieldIndex"] = str(self.field_index)
        params["itemIndex"] = str(self.item_index)
        params["isHide"] = "true" if self.is_hide else "false"
        if self.need_re_calculate is not None:
            params["needReCalculate"] = "true" if self.need_re_calculate else "false"
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
