"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class TranslateSpreadsheetRequest(RequestOption):
    """Translates the entire spreadsheet to the specified target language."""

    def __init__(
        self,
        spreadsheet: FileSource,
        target_language: str,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not target_language:
            raise ValueError("targetLanguage is required")
        self.spreadsheet = spreadsheet
        self.target_language = target_language
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/ai/translate/spreadsheet"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["targetLanguage"] = self.target_language
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
