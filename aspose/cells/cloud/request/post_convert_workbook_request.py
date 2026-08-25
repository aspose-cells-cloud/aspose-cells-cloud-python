"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostConvertWorkbookRequest(RequestOption):
    """PostConvertWorkbookRequest."""

    def __init__(
        self,
        convert_workbook_options: ConvertWorkbookOptions,
        fonts_location: Optional[str] = None,
    ):
        if convert_workbook_options is None:
            raise ValueError("convertWorkbookOptions is required")
        self.convert_workbook_options = convert_workbook_options
        self.fonts_location = fonts_location

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/convertWorkbook"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.fonts_location:
            params["FontsLocation"] = self.fonts_location
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.convert_workbook_options.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
