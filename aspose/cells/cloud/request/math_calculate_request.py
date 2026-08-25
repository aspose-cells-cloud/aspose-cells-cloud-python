"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class MathCalculateRequest(RequestOption):
    """MathCalculateRequest."""

    def __init__(
        self,
        spreadsheet: FileSource,
        operation: str,
        value: str,
        worksheet: Optional[str] = None,
        range_: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not operation:
            raise ValueError("operation is required")
        if not value:
            raise ValueError("value is required")
        self.spreadsheet = spreadsheet
        self.operation = operation
        self.value = value
        self.worksheet = worksheet
        self.range_ = range_
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/calculate/math"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["operation"] = self.operation
        params["value"] = self.value
        if self.worksheet:
            params["worksheet"] = self.worksheet
        if self.range_:
            params["range"] = self.range_
        if self.region:
            params["region"] = self.region
        if self.password:
            params["password"] = self.password
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"Spreadsheet": self.spreadsheet}
