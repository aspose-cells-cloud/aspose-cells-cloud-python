"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class SplitTableRequest(RequestOption):
    """Split an Excel worksheet tale into multiple sheets by column value."""

    def __init__(
        self,
        spreadsheet: FileSource,
        worksheet: str,
        table_name: str,
        split_column_name: str,
        save_split_column: bool,
        split_row_number: int,
        to_new_workbook: bool,
        to_multiple_files: bool,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        fonts_location: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not worksheet:
            raise ValueError("worksheet is required")
        if not table_name:
            raise ValueError("tableName is required")
        if not split_column_name:
            raise ValueError("splitColumnName is required")
        if save_split_column is None:
            raise ValueError("saveSplitColumn is required")
        if split_row_number is None:
            raise ValueError("splitRowNumber is required")
        if to_new_workbook is None:
            raise ValueError("toNewWorkbook is required")
        if to_multiple_files is None:
            raise ValueError("toMultipleFiles is required")
        self.spreadsheet = spreadsheet
        self.worksheet = worksheet
        self.table_name = table_name
        self.split_column_name = split_column_name
        self.save_split_column = save_split_column
        self.split_row_number = split_row_number
        self.to_new_workbook = to_new_workbook
        self.to_multiple_files = to_multiple_files
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.fonts_location = fonts_location
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/split/table"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["worksheet"] = self.worksheet
        params["tableName"] = self.table_name
        params["splitColumnName"] = self.split_column_name
        params["saveSplitColumn"] = "true" if self.save_split_column else "false"
        params["splitRowNumber"] = str(self.split_row_number)
        params["toNewWorkbook"] = "true" if self.to_new_workbook else "false"
        params["toMultipleFiles"] = "true" if self.to_multiple_files else "false"
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
        return {"Spreadsheet": self.spreadsheet}
