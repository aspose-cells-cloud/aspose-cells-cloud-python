"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class ConvertSpreadsheetToPdfRequest(RequestOption):
    """Converts a spreadsheet on a local drive to the pdf file."""

    def __init__(
        self,
        spreadsheet: FileSource,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        fonts_location: Optional[str] = None,
        auto_rows_fit: Optional[bool] = None,
        auto_columns_fit: Optional[bool] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        self.spreadsheet = spreadsheet
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.fonts_location = fonts_location
        self.auto_rows_fit = auto_rows_fit
        self.auto_columns_fit = auto_columns_fit
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/convert/spreadsheet/pdf"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.out_path:
            params["outPath"] = self.out_path
        if self.out_storage_name:
            params["outStorageName"] = self.out_storage_name
        if self.fonts_location:
            params["fontsLocation"] = self.fonts_location
        if self.auto_rows_fit is not None:
            params["AutoRowsFit"] = "true" if self.auto_rows_fit else "false"
        if self.auto_columns_fit is not None:
            params["AutoColumnsFit"] = "true" if self.auto_columns_fit else "false"
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
