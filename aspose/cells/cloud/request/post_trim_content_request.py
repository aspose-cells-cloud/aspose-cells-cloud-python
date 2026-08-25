"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostTrimContentRequest(RequestOption):
    """The PostTrimContent API is designed to process and trim content within a specified range in a spreadsheet. This API allows users to remove extra spaces, line breaks, or other unnecessary characters from the content of selected cells. It is particularly useful for cleaning up data entries and ensuring consistency in spreadsheet formatting"""

    def __init__(
        self,
        trim_content_options: TrimContentOptions,
    ):
        if trim_content_options is None:
            raise ValueError("trimContentOptions is required")
        self.trim_content_options = trim_content_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/trimcontent"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.trim_content_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
