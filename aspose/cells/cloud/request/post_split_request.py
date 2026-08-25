"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class PostSplitRequest(RequestOption):
    """Split Excel spreadsheet files based on worksheets and create output files in various formats."""

    def __init__(
        self,
        file: FileSource,
        out_format: str,
        password: Optional[str] = None,
        from_: Optional[int] = None,
        to: Optional[int] = None,
        check_excel_restriction: Optional[bool] = None,
        region: Optional[str] = None,
    ):
        if not file:
            raise ValueError("File is required")
        if not out_format:
            raise ValueError("outFormat is required")
        self.file = file
        self.out_format = out_format
        self.password = password
        self.from_ = from_
        self.to = to
        self.check_excel_restriction = check_excel_restriction
        self.region = region

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/split"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["outFormat"] = self.out_format
        if self.password:
            params["password"] = self.password
        if self.from_ is not None:
            params["from"] = str(self.from_)
        if self.to is not None:
            params["to"] = str(self.to)
        if self.check_excel_restriction is not None:
            params["checkExcelRestriction"] = "true" if self.check_excel_restriction else "false"
        if self.region:
            params["region"] = self.region
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"File": self.file}
