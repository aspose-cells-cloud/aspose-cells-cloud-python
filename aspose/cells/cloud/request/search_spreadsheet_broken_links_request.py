"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class SearchSpreadsheetBrokenLinksRequest(RequestOption):
    """Search broken links in the local spreadsheet."""

    def __init__(
        self,
        spreadsheet: FileSource,
        worksheet: Optional[str] = None,
        cell_area: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        self.spreadsheet = spreadsheet
        self.worksheet = worksheet
        self.cell_area = cell_area
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/search/broken-links"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.worksheet:
            params["worksheet"] = self.worksheet
        if self.cell_area:
            params["cellArea"] = self.cell_area
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
