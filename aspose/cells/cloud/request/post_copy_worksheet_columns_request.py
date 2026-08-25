"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostCopyWorksheetColumnsRequest(RequestOption):
    """Copy data from source columns to destination columns in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        source_column_index: int,
        destination_column_index: int,
        column_number: int,
        worksheet: Optional[str] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if source_column_index is None:
            raise ValueError("sourceColumnIndex is required")
        if destination_column_index is None:
            raise ValueError("destinationColumnIndex is required")
        if column_number is None:
            raise ValueError("columnNumber is required")
        self.name = name
        self.sheet_name = sheet_name
        self.source_column_index = source_column_index
        self.destination_column_index = destination_column_index
        self.column_number = column_number
        self.worksheet = worksheet
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
            "/cells/columns/copy"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["sourceColumnIndex"] = str(self.source_column_index)
        params["destinationColumnIndex"] = str(self.destination_column_index)
        params["columnNumber"] = str(self.column_number)
        if self.worksheet:
            params["worksheet"] = self.worksheet
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
