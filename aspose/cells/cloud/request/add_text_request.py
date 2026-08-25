"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class AddTextRequest(RequestOption):
    """Specify appending text to multiple cells at once, allowing you to add prefixes, suffixes, labels, or any specific characters. You can choose the exact position of the text—in the beginning, at the end, or before or after certain characters in the cell."""

    def __init__(
        self,
        spreadsheet: FileSource,
        text: str,
        position: str,
        select_text: Optional[str] = None,
        skip_empty_cells: Optional[bool] = None,
        worksheet: Optional[str] = None,
        range_: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not text:
            raise ValueError("text is required")
        if not position:
            raise ValueError("position is required")
        self.spreadsheet = spreadsheet
        self.text = text
        self.position = position
        self.select_text = select_text
        self.skip_empty_cells = skip_empty_cells
        self.worksheet = worksheet
        self.range_ = range_
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/content/add/text"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["text"] = self.text
        params["position"] = self.position
        if self.select_text:
            params["selectText"] = self.select_text
        if self.skip_empty_cells is not None:
            params["skipEmptyCells"] = "true" if self.skip_empty_cells else "false"
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
