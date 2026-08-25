"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class MergeSpreadsheetsInRemoteFolderRequest(RequestOption):
    """Merge spreadsheet files in folder of cloud storage into a specified format file."""

    def __init__(
        self,
        folder: str,
        file_match_expression: Optional[str] = None,
        out_format: Optional[str] = None,
        merge_in_one_sheet: Optional[bool] = None,
        storage_name: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        fonts_location: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not folder:
            raise ValueError("folder is required")
        self.folder = folder
        self.file_match_expression = file_match_expression
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
        return "/v4.0/cells/merge/remote-spreadsheets"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["folder"] = self.folder
        if self.file_match_expression:
            params["fileMatchExpression"] = self.file_match_expression
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
