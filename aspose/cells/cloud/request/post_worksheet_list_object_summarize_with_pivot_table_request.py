"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorksheetListObjectSummarizeWithPivotTableRequest(RequestOption):
    """Create a pivot table with a list object in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        list_object_index: int,
        destsheet_name: str,
        create_pivot_table_request: CreatePivotTableRequest,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if list_object_index is None:
            raise ValueError("listObjectIndex is required")
        if not destsheet_name:
            raise ValueError("destsheetName is required")
        if create_pivot_table_request is None:
            raise ValueError("createPivotTableRequest is required")
        self.name = name
        self.sheet_name = sheet_name
        self.list_object_index = list_object_index
        self.destsheet_name = destsheet_name
        self.create_pivot_table_request = create_pivot_table_request
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
            "/listobjects/" +
            quote(str(self.list_object_index), safe="/") +
            "/SummarizeWithPivotTable"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["destsheetName"] = self.destsheet_name
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.create_pivot_table_request.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
