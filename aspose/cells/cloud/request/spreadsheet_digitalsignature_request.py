"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class SpreadsheetDigitalsignatureRequest(RequestOption):
    """SpreadsheetDigitalsignatureRequest."""

    def __init__(
        self,
        spreadsheet: FileSource,
        password: str,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not password:
            raise ValueError("password is required")
        self.spreadsheet = spreadsheet
        self.password = password
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/digitalsignature/spreadsheet"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["password"] = self.password
        if self.out_path:
            params["outPath"] = self.out_path
        if self.out_storage_name:
            params["outStorageName"] = self.out_storage_name
        if self.region:
            params["region"] = self.region
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"Spreadsheet": self.spreadsheet}
