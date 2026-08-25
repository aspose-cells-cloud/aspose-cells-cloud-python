"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutInsertNewWorksheetRequest(RequestOption):
    """Insert a new worksheet in the workbook."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        index: int,
        sheettype: str,
        newsheetname: Optional[str] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if index is None:
            raise ValueError("index is required")
        if not sheettype:
            raise ValueError("sheettype is required")
        self.name = name
        self.sheet_name = sheet_name
        self.index = index
        self.sheettype = sheettype
        self.newsheetname = newsheetname
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/insert"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["sheetName"] = self.sheet_name
        params["index"] = str(self.index)
        params["sheettype"] = self.sheettype
        if self.newsheetname:
            params["newsheetname"] = self.newsheetname
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
