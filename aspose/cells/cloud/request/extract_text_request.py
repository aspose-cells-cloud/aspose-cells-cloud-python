"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class ExtractTextRequest(RequestOption):
    """Indicates extracting substrings, text characters, and numbers from a spreadsheet cell into another cell without having to use complex FIND, MIN, LEFT, or RIGHT formulas."""

    def __init__(
        self,
        spreadsheet: FileSource,
        extract_text_type: str,
        out_position_range: str,
        before_text: Optional[str] = None,
        after_text: Optional[str] = None,
        before_position: Optional[int] = None,
        after_position: Optional[int] = None,
        worksheet: Optional[str] = None,
        range_: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not extract_text_type:
            raise ValueError("extractTextType is required")
        if not out_position_range:
            raise ValueError("outPositionRange is required")
        self.spreadsheet = spreadsheet
        self.extract_text_type = extract_text_type
        self.out_position_range = out_position_range
        self.before_text = before_text
        self.after_text = after_text
        self.before_position = before_position
        self.after_position = after_position
        self.worksheet = worksheet
        self.range_ = range_
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/content/extract/text"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["extractTextType"] = self.extract_text_type
        params["outPositionRange"] = self.out_position_range
        if self.before_text:
            params["beforeText"] = self.before_text
        if self.after_text:
            params["afterText"] = self.after_text
        if self.before_position is not None:
            params["beforePosition"] = str(self.before_position)
        if self.after_position is not None:
            params["afterPosition"] = str(self.after_position)
        if self.worksheet:
            params["worksheet"] = self.worksheet
        if self.range_:
            params["range"] = self.range_
        if self.out_path:
            params["outPath"] = self.out_path
        if self.out_storage_name:
            params["outStorageName"] = self.out_storage_name
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
