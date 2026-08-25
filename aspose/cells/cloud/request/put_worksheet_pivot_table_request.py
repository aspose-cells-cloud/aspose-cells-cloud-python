"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetPivotTableRequest(RequestOption):
    """Add a PivotTable in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        folder: Optional[str] = None,
        source_data: Optional[str] = None,
        dest_cell_name: Optional[str] = None,
        table_name: Optional[str] = None,
        use_same_source: Optional[bool] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.folder = folder
        self.source_data = source_data
        self.dest_cell_name = dest_cell_name
        self.table_name = table_name
        self.use_same_source = use_same_source
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/pivottables"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.folder:
            params["folder"] = self.folder
        if self.source_data:
            params["sourceData"] = self.source_data
        if self.dest_cell_name:
            params["destCellName"] = self.dest_cell_name
        if self.table_name:
            params["tableName"] = self.table_name
        if self.use_same_source is not None:
            params["useSameSource"] = "true" if self.use_same_source else "false"
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
