"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetChartTitleRequest(RequestOption):
    """Set chart title in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        chart_index: int,
        title: Optional[Title] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if chart_index is None:
            raise ValueError("chartIndex is required")
        self.name = name
        self.sheet_name = sheet_name
        self.chart_index = chart_index
        self.title = title
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/charts/" +
            quote(str(self.chart_index), safe="/") +
            "/title"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        if self.title is not None:
            return self.title.to_dict()
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
