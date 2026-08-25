"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostUpdateWordCaseRequest(RequestOption):
    """Managing inconsistent text case in spreadsheets (Excel, Google Sheets, CSV) can be frustrating, especially with large datasets. The PostUpdateWordCase WEB API solves this by automating text case conversions, ensuring clean and standardized data."""

    def __init__(
        self,
        word_case_options: WordCaseOptions,
    ):
        if word_case_options is None:
            raise ValueError("wordCaseOptions is required")
        self.word_case_options = word_case_options

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/updatewordcase"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.word_case_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
