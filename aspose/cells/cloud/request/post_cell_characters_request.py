"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostCellCharactersRequest(RequestOption):
    """Set cell characters in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        cell_name: str,
        options: Optional[List[FontSetting]] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if not cell_name:
            raise ValueError("cellName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.cell_name = cell_name
        self.options = options
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
            "/cells/" +
            quote(self.cell_name, safe="/") +
            "/characters"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        if self.options is not None:
            return [x.to_dict() for x in self.options]
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
