"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class SwapRangeRequest(RequestOption):
    """The Swap Ranges for Excel API provides a powerful tool to move any two columns, rows, ranges, or individual cells within an Excel file. This API allows users to re-arrange their tables quickly and efficiently, ensuring that the original data formatting is preserved and all existing formulas continue to function correctly. By leveraging this API, users can streamline their data manipulation tasks and maintain the integrity of their spreadsheets."""

    def __init__(
        self,
        spreadsheet: FileSource,
        worksheet1: str,
        range1: str,
        worksheet2: str,
        range2: str,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not worksheet1:
            raise ValueError("worksheet1 is required")
        if not range1:
            raise ValueError("range1 is required")
        if not worksheet2:
            raise ValueError("worksheet2 is required")
        if not range2:
            raise ValueError("range2 is required")
        self.spreadsheet = spreadsheet
        self.worksheet1 = worksheet1
        self.range1 = range1
        self.worksheet2 = worksheet2
        self.range2 = range2
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/swap/range"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["worksheet1"] = self.worksheet1
        params["range1"] = self.range1
        params["worksheet2"] = self.worksheet2
        params["range2"] = self.range2
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
