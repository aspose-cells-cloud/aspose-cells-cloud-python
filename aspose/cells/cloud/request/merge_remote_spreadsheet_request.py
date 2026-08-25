"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class MergeRemoteSpreadsheetRequest(RequestOption):
    """Merge a spreadsheet file into other spreadsheet in cloud storage, and output a specified format file."""

    def __init__(
        self,
        name: str,
        merged_spreadsheet: str,
        folder: Optional[str] = None,
        out_format: Optional[str] = None,
        merge_in_one_sheet: Optional[bool] = None,
        storage_name: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        fonts_location: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not merged_spreadsheet:
            raise ValueError("mergedSpreadsheet is required")
        self.name = name
        self.merged_spreadsheet = merged_spreadsheet
        self.folder = folder
        self.out_format = out_format
        self.merge_in_one_sheet = merge_in_one_sheet
        self.storage_name = storage_name
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.fonts_location = fonts_location
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v4.0/cells/" +
            quote(self.name, safe="/") +
            "/merge/spreadsheet"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["mergedSpreadsheet"] = self.merged_spreadsheet
        if self.folder:
            params["folder"] = self.folder
        if self.out_format:
            params["outFormat"] = self.out_format
        if self.merge_in_one_sheet is not None:
            params["mergeInOneSheet"] = "true" if self.merge_in_one_sheet else "false"
        if self.storage_name:
            params["storageName"] = self.storage_name
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
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
