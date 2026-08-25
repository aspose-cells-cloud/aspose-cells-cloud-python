"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostCopyWorksheetRequest(RequestOption):
    """Copy contents and formats from another worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        source_sheet: str,
        options: CopyOptions,
        source_workbook: Optional[str] = None,
        source_folder: Optional[str] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if not source_sheet:
            raise ValueError("sourceSheet is required")
        if options is None:
            raise ValueError("options is required")
        self.name = name
        self.sheet_name = sheet_name
        self.source_sheet = source_sheet
        self.options = options
        self.source_workbook = source_workbook
        self.source_folder = source_folder
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/copy"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["sourceSheet"] = self.source_sheet
        if self.source_workbook:
            params["sourceWorkbook"] = self.source_workbook
        if self.source_folder:
            params["sourceFolder"] = self.source_folder
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
