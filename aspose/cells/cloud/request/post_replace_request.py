"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class PostReplaceRequest(RequestOption):
    """Replace specified text with new text in Excel files."""

    def __init__(
        self,
        file: FileSource,
        text: str,
        newtext: str,
        password: Optional[str] = None,
        sheetname: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
    ):
        if not file:
            raise ValueError("File is required")
        if not text:
            raise ValueError("text is required")
        if not newtext:
            raise ValueError("newtext is required")
        self.file = file
        self.text = text
        self.newtext = newtext
        self.password = password
        self.sheetname = sheetname
        self.check_excel_restriction = check_excel_restriction

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/replace"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["text"] = self.text
        params["newtext"] = self.newtext
        if self.password:
            params["password"] = self.password
        if self.sheetname:
            params["sheetname"] = self.sheetname
        if self.check_excel_restriction is not None:
            params["checkExcelRestriction"] = "true" if self.check_excel_restriction else "false"
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"File": self.file}
