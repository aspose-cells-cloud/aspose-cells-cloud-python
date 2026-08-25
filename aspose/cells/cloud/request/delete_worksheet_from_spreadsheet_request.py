"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class DeleteWorksheetFromSpreadsheetRequest(RequestOption):
    """The Web API endpoint allows users to delete a specified worksheet from a workbook. This function provides a straightforward way to manage workbook structure by removing unnecessary or redundant worksheets."""

    def __init__(
        self,
        spreadsheet: FileSource,
        sheet_name: str,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.spreadsheet = spreadsheet
        self.sheet_name = sheet_name
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/spreadsheet/delete/worksheet"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["sheetName"] = self.sheet_name
        if self.out_path:
            params["outPath"] = self.out_path
        if self.out_storage_name:
            params["outStorageName"] = self.out_storage_name
        if self.region:
            params["region"] = self.region
        if self.password:
            params["password"] = self.password
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"Spreadsheet": self.spreadsheet}
