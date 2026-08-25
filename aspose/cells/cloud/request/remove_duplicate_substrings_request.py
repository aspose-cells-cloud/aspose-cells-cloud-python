"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class RemoveDuplicateSubstringsRequest(RequestOption):
    """Finds and removes repeated substrings inside every cell of the chosen range, using user-defined or preset delimiters, while preserving formulas, formatting and data-validation."""

    def __init__(
        self,
        spreadsheet: FileSource,
        delimiters: str,
        treat_consecutive_delimiters_as_one: Optional[bool] = None,
        case_sensitive: Optional[bool] = None,
        worksheet: Optional[str] = None,
        range_: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not delimiters:
            raise ValueError("delimiters is required")
        self.spreadsheet = spreadsheet
        self.delimiters = delimiters
        self.treat_consecutive_delimiters_as_one = treat_consecutive_delimiters_as_one
        self.case_sensitive = case_sensitive
        self.worksheet = worksheet
        self.range_ = range_
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/content/remove/duplicate-substrings"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["delimiters"] = self.delimiters
        if self.treat_consecutive_delimiters_as_one is not None:
            params["treatConsecutiveDelimitersAsOne"] = "true" if self.treat_consecutive_delimiters_as_one else "false"
        if self.case_sensitive is not None:
            params["caseSensitive"] = "true" if self.case_sensitive else "false"
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
