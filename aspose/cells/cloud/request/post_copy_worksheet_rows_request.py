"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostCopyWorksheetRowsRequest(RequestOption):
    """Copy data and formats from specific entire rows in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        source_row_index: int,
        destination_row_index: int,
        row_number: int,
        worksheet: Optional[str] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if source_row_index is None:
            raise ValueError("sourceRowIndex is required")
        if destination_row_index is None:
            raise ValueError("destinationRowIndex is required")
        if row_number is None:
            raise ValueError("rowNumber is required")
        self.name = name
        self.sheet_name = sheet_name
        self.source_row_index = source_row_index
        self.destination_row_index = destination_row_index
        self.row_number = row_number
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
            "/cells/rows/copy"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["sourceRowIndex"] = str(self.source_row_index)
        params["destinationRowIndex"] = str(self.destination_row_index)
        params["rowNumber"] = str(self.row_number)
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
