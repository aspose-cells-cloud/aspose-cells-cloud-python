"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class CreateSpreadsheetRequest(RequestOption):
    """The Web API allows users to create a new spreadsheet with a specified name. Optionally, a template can be provided to initialize the spreadsheet with predefined content or formatting."""

    def __init__(
        self,
        format_: Optional[str] = None,
        template: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        self.format_ = format_
        self.template = template
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/spreadsheet/create"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.format_:
            params["format"] = self.format_
        if self.template:
            params["template"] = self.template
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
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
