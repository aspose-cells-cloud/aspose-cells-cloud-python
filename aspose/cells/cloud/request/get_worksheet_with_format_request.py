"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class GetWorksheetWithFormatRequest(RequestOption):
    """Retrieve the worksheet in a specified format from the workbook."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        format_: Optional[str] = None,
        vertical_resolution: Optional[int] = None,
        horizontal_resolution: Optional[int] = None,
        area: Optional[str] = None,
        page_index: Optional[int] = None,
        one_page_per_sheet: Optional[bool] = None,
        print_headings: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.format_ = format_
        self.vertical_resolution = vertical_resolution
        self.horizontal_resolution = horizontal_resolution
        self.area = area
        self.page_index = page_index
        self.one_page_per_sheet = one_page_per_sheet
        self.print_headings = print_headings
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/")
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.format_:
            params["format"] = self.format_
        if self.vertical_resolution is not None:
            params["verticalResolution"] = str(self.vertical_resolution)
        if self.horizontal_resolution is not None:
            params["horizontalResolution"] = str(self.horizontal_resolution)
        if self.area:
            params["area"] = self.area
        if self.page_index is not None:
            params["pageIndex"] = str(self.page_index)
        if self.one_page_per_sheet is not None:
            params["onePagePerSheet"] = "true" if self.one_page_per_sheet else "false"
        if self.print_headings is not None:
            params["printHeadings"] = "true" if self.print_headings else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
