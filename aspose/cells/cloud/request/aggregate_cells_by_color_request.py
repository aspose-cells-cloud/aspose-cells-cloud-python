"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class AggregateCellsByColorRequest(RequestOption):
    """The Aggregate by Color API provides a convenient way to perform calculations on cells that share the same fill or font color. This API supports a range of aggregate operations, including count, sum, maximum value, minimum value, and average value, enabling you to analyze and summarize data based on color distinctions."""

    def __init__(
        self,
        spreadsheet: FileSource,
        worksheet: Optional[str] = None,
        range_: Optional[str] = None,
        operation: Optional[str] = None,
        color_position: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        self.spreadsheet = spreadsheet
        self.worksheet = worksheet
        self.range_ = range_
        self.operation = operation
        self.color_position = color_position
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/calculate/aggergate/color"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.worksheet:
            params["worksheet"] = self.worksheet
        if self.range_:
            params["range"] = self.range_
        if self.operation:
            params["operation"] = self.operation
        if self.color_position:
            params["colorPosition"] = self.color_position
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
