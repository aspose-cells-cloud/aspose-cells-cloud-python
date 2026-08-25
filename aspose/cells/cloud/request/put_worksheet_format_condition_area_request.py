"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetFormatConditionAreaRequest(RequestOption):
    """Add a cell area for the format condition in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        index: int,
        cell_area: str,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if index is None:
            raise ValueError("index is required")
        if not cell_area:
            raise ValueError("cellArea is required")
        self.name = name
        self.sheet_name = sheet_name
        self.index = index
        self.cell_area = cell_area
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
            "/conditionalFormattings/" +
            quote(str(self.index), safe="/") +
            "/area"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["cellArea"] = self.cell_area
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
