"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class PutConvertWorkbookRequest(RequestOption):
    """Convert the workbook from the requested content into files in different formats."""

    def __init__(
        self,
        file: FileSource,
        format_: str,
        password: Optional[str] = None,
        out_path: Optional[str] = None,
        storage_name: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
        stream_format: Optional[str] = None,
        region: Optional[str] = None,
        page_wide_fit_on_per_sheet: Optional[bool] = None,
        page_tall_fit_on_per_sheet: Optional[bool] = None,
        sheet_name: Optional[str] = None,
        page_index: Optional[int] = None,
        one_page_per_sheet: Optional[bool] = None,
        auto_rows_fit: Optional[bool] = None,
        auto_columns_fit: Optional[bool] = None,
        fonts_location: Optional[str] = None,
    ):
        if not file:
            raise ValueError("File is required")
        if not format_:
            raise ValueError("format is required")
        self.file = file
        self.format_ = format_
        self.password = password
        self.out_path = out_path
        self.storage_name = storage_name
        self.check_excel_restriction = check_excel_restriction
        self.stream_format = stream_format
        self.region = region
        self.page_wide_fit_on_per_sheet = page_wide_fit_on_per_sheet
        self.page_tall_fit_on_per_sheet = page_tall_fit_on_per_sheet
        self.sheet_name = sheet_name
        self.page_index = page_index
        self.one_page_per_sheet = one_page_per_sheet
        self.auto_rows_fit = auto_rows_fit
        self.auto_columns_fit = auto_columns_fit
        self.fonts_location = fonts_location

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v3.0/cells/convert"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["format"] = self.format_
        if self.password:
            params["password"] = self.password
        if self.out_path:
            params["outPath"] = self.out_path
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.check_excel_restriction is not None:
            params["checkExcelRestriction"] = "true" if self.check_excel_restriction else "false"
        if self.stream_format:
            params["streamFormat"] = self.stream_format
        if self.region:
            params["region"] = self.region
        if self.page_wide_fit_on_per_sheet is not None:
            params["pageWideFitOnPerSheet"] = "true" if self.page_wide_fit_on_per_sheet else "false"
        if self.page_tall_fit_on_per_sheet is not None:
            params["pageTallFitOnPerSheet"] = "true" if self.page_tall_fit_on_per_sheet else "false"
        if self.sheet_name:
            params["sheetName"] = self.sheet_name
        if self.page_index is not None:
            params["pageIndex"] = str(self.page_index)
        if self.one_page_per_sheet is not None:
            params["onePagePerSheet"] = "true" if self.one_page_per_sheet else "false"
        if self.auto_rows_fit is not None:
            params["AutoRowsFit"] = "true" if self.auto_rows_fit else "false"
        if self.auto_columns_fit is not None:
            params["AutoColumnsFit"] = "true" if self.auto_columns_fit else "false"
        if self.fonts_location:
            params["FontsLocation"] = self.fonts_location
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"File": self.file}
