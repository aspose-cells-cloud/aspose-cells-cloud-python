"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class AddWorksheetToSpreadsheetRequest(RequestOption):
    """The Web API enables users to add a new worksheet to a workbook, specifying the worksheet's type, position, and name. This function provides flexibility in managing workbook structure by allowing detailed control over worksheet addition."""

    def __init__(
        self,
        spreadsheet: FileSource,
        sheet_type: Optional[str] = None,
        position: Optional[int] = None,
        sheet_name: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        self.spreadsheet = spreadsheet
        self.sheet_type = sheet_type
        self.position = position
        self.sheet_name = sheet_name
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/spreadsheet/add/worksheet"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.sheet_type:
            params["sheetType"] = self.sheet_type
        if self.position is not None:
            params["position"] = str(self.position)
        if self.sheet_name:
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
