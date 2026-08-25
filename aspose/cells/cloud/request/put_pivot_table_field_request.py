"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutPivotTableFieldRequest(RequestOption):
    """Add a pivot field in the PivotTable."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        pivot_table_index: int,
        pivot_field_type: str,
        pivot_table_field_request: PivotTableFieldRequest,
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
        if pivot_table_field_request is None:
            raise ValueError("pivotTableFieldRequest is required")
        self.name = name
        self.sheet_name = sheet_name
        self.pivot_table_index = pivot_table_index
        self.pivot_field_type = pivot_field_type
        self.pivot_table_field_request = pivot_table_field_request
        self.need_re_calculate = need_re_calculate
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
            "/pivottables/" +
            quote(str(self.pivot_table_index), safe="/") +
            "/PivotField"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["pivotFieldType"] = self.pivot_field_type
        if self.need_re_calculate is not None:
            params["needReCalculate"] = "true" if self.need_re_calculate else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.pivot_table_field_request.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
