"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class RemoveCharactersInRemoteSpreadsheetRequest(RequestOption):
    """Deletes user-defined characters, predefined symbol sets, or any substring from every cell in the chosen range while preserving formulas, formatting and data-validation for a remote spreadsheet."""

    def __init__(
        self,
        name: str,
        worksheet: str,
        range_: str,
        remove_text_method: Optional[str] = None,
        character_sets: Optional[str] = None,
        remove_custom_value: Optional[str] = None,
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
        self.name = name
        self.worksheet = worksheet
        self.range_ = range_
        self.remove_text_method = remove_text_method
        self.character_sets = character_sets
        self.remove_custom_value = remove_custom_value
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
            "/content/remove/characters"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.remove_text_method:
            params["removeTextMethod"] = self.remove_text_method
        if self.character_sets:
            params["characterSets"] = self.character_sets
        if self.remove_custom_value:
            params["removeCustomValue"] = self.remove_custom_value
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
