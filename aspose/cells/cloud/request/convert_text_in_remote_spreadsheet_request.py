"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class ConvertTextInRemoteSpreadsheetRequest(RequestOption):
    """Indicates converting the numbers stored as text into the correct number format, replacing unwanted characters and line breaks with the desired characters, and converting accented characters to their equivalent characters without accents."""

    def __init__(
        self,
        name: str,
        worksheet: str,
        range_: str,
        convert_text_type: str,
        source_characters: Optional[str] = None,
        target_characters: Optional[str] = None,
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
        if not convert_text_type:
            raise ValueError("convertTextType is required")
        self.name = name
        self.worksheet = worksheet
        self.range_ = range_
        self.convert_text_type = convert_text_type
        self.source_characters = source_characters
        self.target_characters = target_characters
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
            "/content/convert/text"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["convertTextType"] = self.convert_text_type
        if self.source_characters:
            params["sourceCharacters"] = self.source_characters
        if self.target_characters:
            params["targetCharacters"] = self.target_characters
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
