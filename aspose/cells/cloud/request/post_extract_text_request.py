"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostExtractTextRequest(RequestOption):
    """Effortlessly extract text and numbers from Excel cells with precise options. This API allows extraction of first/last characters, text between delimiters, and numbers from strings, with output as static values or formulas."""

    def __init__(
        self,
        extract_text_options: ExtractTextOptions,
    ):
        if extract_text_options is None:
            raise ValueError("extractTextOptions is required")
        self.extract_text_options = extract_text_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/extracttext"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.extract_text_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
