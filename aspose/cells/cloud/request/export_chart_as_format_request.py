"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class ExportChartAsFormatRequest(RequestOption):
    """Converts a chart of spreadsheet in cloud storage to the specified format."""

    def __init__(
        self,
        name: str,
        worksheet: str,
        chart_index: int,
        format_: str,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        fonts_location: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not worksheet:
            raise ValueError("worksheet is required")
        if chart_index is None:
            raise ValueError("chartIndex is required")
        if not format_:
            raise ValueError("format is required")
        self.name = name
        self.worksheet = worksheet
        self.chart_index = chart_index
        self.format_ = format_
        self.folder = folder
        self.storage_name = storage_name
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.fonts_location = fonts_location
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return (
            "/v4.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.worksheet, safe="/") +
            "/charts/" +
            quote(str(self.chart_index), safe="/")
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["format"] = self.format_
        if self.folder:
            params["folder"] = self.folder
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
