"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class PostCompressRequest(RequestOption):
    """Compress files and generate target files in various formats, supported file formats are include Xls, Xlsx, Xlsm, Xlsb, Ods and more."""

    def __init__(
        self,
        file: FileSource,
        compress_level: Optional[int] = None,
        password: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
    ):
        if not file:
            raise ValueError("File is required")
        self.file = file
        self.compress_level = compress_level
        self.password = password
        self.check_excel_restriction = check_excel_restriction

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/compress"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.compress_level is not None:
            params["CompressLevel"] = str(self.compress_level)
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
