"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class RemoveDuplicateSubstringsInRemoteSpreadsheetRequest(RequestOption):
    """Finds and removes repeated substrings inside every cell of the chosen range, using user-defined or preset delimiters, while preserving formulas, formatting and data-validation."""

    def __init__(
        self,
        name: str,
        worksheet: str,
        range_: str,
        delimiters: str,
        treat_consecutive_delimiters_as_one: Optional[bool] = None,
        case_sensitive: Optional[bool] = None,
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
        if not delimiters:
            raise ValueError("delimiters is required")
        self.name = name
        self.worksheet = worksheet
        self.range_ = range_
        self.delimiters = delimiters
        self.treat_consecutive_delimiters_as_one = treat_consecutive_delimiters_as_one
        self.case_sensitive = case_sensitive
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
            "/content/remove/duplicate-substrings"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["delimiters"] = self.delimiters
        if self.treat_consecutive_delimiters_as_one is not None:
            params["treatConsecutiveDelimitersAsOne"] = "true" if self.treat_consecutive_delimiters_as_one else "false"
        if self.case_sensitive is not None:
            params["caseSensitive"] = "true" if self.case_sensitive else "false"
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
