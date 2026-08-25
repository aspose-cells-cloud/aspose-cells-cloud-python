"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class DeleteMetadataRequest(RequestOption):
    """Delete cells document properties in Excel file, and save them is various formats."""

    def __init__(
        self,
        file: FileSource,
        type_: Optional[str] = None,
        out_format: Optional[str] = None,
        password: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
    ):
        if not file:
            raise ValueError("File is required")
        self.file = file
        self.type_ = type_
        self.out_format = out_format
        self.password = password
        self.check_excel_restriction = check_excel_restriction

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/metadata/delete"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.type_:
            params["type"] = self.type_
        if self.out_format:
            params["outFormat"] = self.out_format
        if self.password:
            params["password"] = self.password
        if self.check_excel_restriction is not None:
            params["checkExcelRestriction"] = "true" if self.check_excel_restriction else "false"
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"File": self.file}
