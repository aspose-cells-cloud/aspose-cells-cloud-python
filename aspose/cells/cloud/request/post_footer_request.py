"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostFooterRequest(RequestOption):
    """Update page footer in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        section: int,
        script: str,
        is_first_page: bool,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if section is None:
            raise ValueError("section is required")
        if not script:
            raise ValueError("script is required")
        if is_first_page is None:
            raise ValueError("isFirstPage is required")
        self.name = name
        self.sheet_name = sheet_name
        self.section = section
        self.script = script
        self.is_first_page = is_first_page
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/pagesetup/footer"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["section"] = str(self.section)
        params["script"] = self.script
        params["isFirstPage"] = "true" if self.is_first_page else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
