"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class AddTextInRemoteSpreadsheetRequest(RequestOption):
    """Specify appending text to multiple cells at once, allowing you to add prefixes, suffixes, labels, or any specific characters. You can choose the exact position of the text—in the beginning, at the end, or before or after certain characters in the cell."""

    def __init__(
        self,
        name: str,
        worksheet: str,
        range_: str,
        text: str,
        position: str,
        select_text: Optional[str] = None,
        skip_empty_cells: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not worksheet:
            raise ValueError("worksheet is required")
        if not range_:
            raise ValueError("range is required")
        if not text:
            raise ValueError("text is required")
        if not position:
            raise ValueError("position is required")
        self.name = name
        self.worksheet = worksheet
        self.range_ = range_
        self.text = text
        self.position = position
        self.select_text = select_text
        self.skip_empty_cells = skip_empty_cells
        self.folder = folder
        self.storage_name = storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v4.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.worksheet, safe="/") +
            "/range/" +
            quote(self.range_, safe="/") +
            "/content/add/text"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["text"] = self.text
        params["position"] = self.position
        if self.select_text:
            params["selectText"] = self.select_text
        if self.skip_empty_cells is not None:
            params["skipEmptyCells"] = "true" if self.skip_empty_cells else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.region:
            params["region"] = self.region
        if self.password:
            params["password"] = self.password
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
