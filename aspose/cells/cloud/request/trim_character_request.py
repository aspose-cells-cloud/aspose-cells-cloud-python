"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class TrimCharacterRequest(RequestOption):
    """The TrimSpreadsheetContent API is designed to process and trim content within a remote spreadsheet. This API allows users to remove extra spaces, line breaks, or other unnecessary characters from the content of selected cells. It is particularly useful for cleaning up data entries and ensuring consistency in spreadsheet formatting"""

    def __init__(
        self,
        spreadsheet: FileSource,
        trim_content: Optional[str] = None,
        trim_leading: Optional[bool] = None,
        trim_trailing: Optional[bool] = None,
        trim_space_between_word_to1: Optional[bool] = None,
        trim_non_breaking_spaces: Optional[bool] = None,
        remove_extra_line_breaks: Optional[bool] = None,
        remove_all_line_breaks: Optional[bool] = None,
        worksheet: Optional[str] = None,
        range_: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        region: Optional[str] = None,
        password: Optional[str] = None,
    ):
        if not spreadsheet:
            raise ValueError("Spreadsheet is required")
        self.spreadsheet = spreadsheet
        self.trim_content = trim_content
        self.trim_leading = trim_leading
        self.trim_trailing = trim_trailing
        self.trim_space_between_word_to1 = trim_space_between_word_to1
        self.trim_non_breaking_spaces = trim_non_breaking_spaces
        self.remove_extra_line_breaks = remove_extra_line_breaks
        self.remove_all_line_breaks = remove_all_line_breaks
        self.worksheet = worksheet
        self.range_ = range_
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.region = region
        self.password = password

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return "/v4.0/cells/content/trim"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.trim_content:
            params["trimContent"] = self.trim_content
        if self.trim_leading is not None:
            params["trimLeading"] = "true" if self.trim_leading else "false"
        if self.trim_trailing is not None:
            params["trimTrailing"] = "true" if self.trim_trailing else "false"
        if self.trim_space_between_word_to1 is not None:
            params["trimSpaceBetweenWordTo1"] = "true" if self.trim_space_between_word_to1 else "false"
        if self.trim_non_breaking_spaces is not None:
            params["trimNonBreakingSpaces"] = "true" if self.trim_non_breaking_spaces else "false"
        if self.remove_extra_line_breaks is not None:
            params["removeExtraLineBreaks"] = "true" if self.remove_extra_line_breaks else "false"
        if self.remove_all_line_breaks is not None:
            params["removeAllLineBreaks"] = "true" if self.remove_all_line_breaks else "false"
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
