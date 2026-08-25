"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class ImportJSONDataIntoSpreadsheetRequest(RequestOption):
    """Import JSON data file into the local spreadsheet."""

    def __init__(
        self,
        datafile: FileSource,
        spreadsheet: FileSource,
        worksheet: str,
        startcell: str,
        insert: Optional[bool] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        fonts_location: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not datafile:
            raise ValueError("datafile is required")
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not worksheet:
            raise ValueError("worksheet is required")
        if not startcell:
            raise ValueError("startcell is required")
        self.datafile = datafile
        self.spreadsheet = spreadsheet
        self.worksheet = worksheet
        self.startcell = startcell
        self.insert = insert
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.fonts_location = fonts_location
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/import/data/json"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["worksheet"] = self.worksheet
        params["startcell"] = self.startcell
        if self.insert is not None:
            params["insert"] = "true" if self.insert else "false"
        if self.out_path:
            params["outPath"] = self.out_path
        if self.out_storage_name:
            params["outStorageName"] = self.out_storage_name
        if self.fonts_location:
            params["fontsLocation"] = self.fonts_location
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
        form = {}
        if self.datafile is not None:
            form["datafile"] = self.datafile
        if self.spreadsheet is not None:
            form["Spreadsheet"] = self.spreadsheet
        return form
