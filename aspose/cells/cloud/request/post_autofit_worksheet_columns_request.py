"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostAutofitWorksheetColumnsRequest(RequestOption):
    """Autofit columns in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        start_column: Optional[int] = None,
        end_column: Optional[int] = None,
        only_auto: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.start_column = start_column
        self.end_column = end_column
        self.only_auto = only_auto
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
            "/autofitcolumns"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.start_column is not None:
            params["startColumn"] = str(self.start_column)
        if self.end_column is not None:
            params["endColumn"] = str(self.end_column)
        if self.only_auto is not None:
            params["onlyAuto"] = "true" if self.only_auto else "false"
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
