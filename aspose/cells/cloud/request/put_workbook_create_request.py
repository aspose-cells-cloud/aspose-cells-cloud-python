"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorkbookCreateRequest(RequestOption):
    """Create a new workbook using different methods."""

    def __init__(
        self,
        name: str,
        template_file: Optional[str] = None,
        data_file: Optional[str] = None,
        is_write_over: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
    ):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.template_file = template_file
        self.data_file = data_file
        self.is_write_over = is_write_over
        self.folder = folder
        self.storage_name = storage_name
        self.check_excel_restriction = check_excel_restriction

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/")
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.template_file:
            params["templateFile"] = self.template_file
        if self.data_file:
            params["dataFile"] = self.data_file
        if self.is_write_over is not None:
            params["isWriteOver"] = "true" if self.is_write_over else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.check_excel_restriction is not None:
            params["checkExcelRestriction"] = "true" if self.check_excel_restriction else "false"
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
