"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class ConvertTextRequest(RequestOption):
    """Indicates converting the numbers stored as text into the correct number format, replacing unwanted characters and line breaks with the desired characters, and converting accented characters to their equivalent characters without accents."""

    def __init__(
        self,
        spreadsheet: FileSource,
        convert_text_type: str,
        source_characters: Optional[str] = None,
        target_characters: Optional[str] = None,
        worksheet: Optional[str] = None,
        range_: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        if not convert_text_type:
            raise ValueError("convertTextType is required")
        self.spreadsheet = spreadsheet
        self.convert_text_type = convert_text_type
        self.source_characters = source_characters
        self.target_characters = target_characters
        self.worksheet = worksheet
        self.range_ = range_
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/content/convert/text"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["convertTextType"] = self.convert_text_type
        if self.source_characters:
            params["sourceCharacters"] = self.source_characters
        if self.target_characters:
            params["targetCharacters"] = self.target_characters
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
