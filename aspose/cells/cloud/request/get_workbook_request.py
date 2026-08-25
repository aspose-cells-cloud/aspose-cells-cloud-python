"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class GetWorkbookRequest(RequestOption):
    """Retrieve workbooks in various formats."""

    def __init__(
        self,
        name: str,
        format_: Optional[str] = None,
        password: Optional[str] = None,
        is_auto_fit: Optional[bool] = None,
        only_save_table: Optional[bool] = None,
        folder: Optional[str] = None,
        out_path: Optional[str] = None,
        storage_name: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
        region: Optional[str] = None,
        page_wide_fit_on_per_sheet: Optional[bool] = None,
        page_tall_fit_on_per_sheet: Optional[bool] = None,
        one_page_per_sheet: Optional[bool] = None,
        only_autofit_table: Optional[bool] = None,
        fonts_location: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.format_ = format_
        self.password = password
        self.is_auto_fit = is_auto_fit
        self.only_save_table = only_save_table
        self.folder = folder
        self.out_path = out_path
        self.storage_name = storage_name
        self.out_storage_name = out_storage_name
        self.check_excel_restriction = check_excel_restriction
        self.region = region
        self.page_wide_fit_on_per_sheet = page_wide_fit_on_per_sheet
        self.page_tall_fit_on_per_sheet = page_tall_fit_on_per_sheet
        self.one_page_per_sheet = one_page_per_sheet
        self.only_autofit_table = only_autofit_table
        self.fonts_location = fonts_location

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/")
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.format_:
            params["format"] = self.format_
        if self.password:
            params["password"] = self.password
        if self.is_auto_fit is not None:
            params["isAutoFit"] = "true" if self.is_auto_fit else "false"
        if self.only_save_table is not None:
            params["onlySaveTable"] = "true" if self.only_save_table else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.out_path:
            params["outPath"] = self.out_path
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
        if self.only_autofit_table is not None:
            params["onlyAutofitTable"] = "true" if self.only_autofit_table else "false"
        if self.fonts_location:
            params["FontsLocation"] = self.fonts_location
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
