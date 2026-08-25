"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostConvertTextRequest(RequestOption):
    """Enhance Excel data through essential text conversions: convert text to numbers, replace characters and line breaks, and remove accents."""

    def __init__(
        self,
        convert_text_options: ConvertTextOptions,
    ):
        if convert_text_options is None:
            raise ValueError("convertTextOptions is required")
        self.convert_text_options = convert_text_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/converttext"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.convert_text_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
