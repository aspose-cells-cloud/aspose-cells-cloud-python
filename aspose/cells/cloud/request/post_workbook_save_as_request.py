"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorkbookSaveAsRequest(RequestOption):
    """Save an Excel file in various formats."""

    def __init__(
        self,
        name: str,
        newfilename: str,
        save_options: Optional[SaveOptions] = None,
        is_auto_fit_rows: Optional[bool] = None,
        is_auto_fit_columns: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
        region: Optional[str] = None,
        page_wide_fit_on_per_sheet: Optional[bool] = None,
        page_tall_fit_on_per_sheet: Optional[bool] = None,
        one_page_per_sheet: Optional[bool] = None,
        fonts_location: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not newfilename:
            raise ValueError("newfilename is required")
        self.name = name
        self.newfilename = newfilename
        self.save_options = save_options
        self.is_auto_fit_rows = is_auto_fit_rows
        self.is_auto_fit_columns = is_auto_fit_columns
        self.folder = folder
        self.storage_name = storage_name
        self.out_storage_name = out_storage_name
        self.check_excel_restriction = check_excel_restriction
        self.region = region
        self.page_wide_fit_on_per_sheet = page_wide_fit_on_per_sheet
        self.page_tall_fit_on_per_sheet = page_tall_fit_on_per_sheet
        self.one_page_per_sheet = one_page_per_sheet
        self.fonts_location = fonts_location

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/SaveAs"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["newfilename"] = self.newfilename
        if self.is_auto_fit_rows is not None:
            params["isAutoFitRows"] = "true" if self.is_auto_fit_rows else "false"
        if self.is_auto_fit_columns is not None:
            params["isAutoFitColumns"] = "true" if self.is_auto_fit_columns else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.out_storage_name:
            params["outStorageName"] = self.out_storage_name
        if self.check_excel_restriction is not None:
            params["checkExcelRestriction"] = "true" if self.check_excel_restriction else "false"
        if self.region:
            params["region"] = self.region
        if self.page_wide_fit_on_per_sheet is not None:
            params["pageWideFitOnPerSheet"] = "true" if self.page_wide_fit_on_per_sheet else "false"
        if self.page_tall_fit_on_per_sheet is not None:
            params["pageTallFitOnPerSheet"] = "true" if self.page_tall_fit_on_per_sheet else "false"
        if self.one_page_per_sheet is not None:
            params["onePagePerSheet"] = "true" if self.one_page_per_sheet else "false"
        if self.fonts_location:
            params["FontsLocation"] = self.fonts_location
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        if self.save_options is not None:
            return self.save_options.to_dict()
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
