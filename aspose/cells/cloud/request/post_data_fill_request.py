"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostDataFillRequest(RequestOption):
    """Data filling for spreadsheet files is primarily used to fill empty data in tables and ranges."""

    def __init__(
        self,
        data_fill_request: DataFillRequest,
    ):
        if data_fill_request is None:
            raise ValueError("dataFillRequest is required")
        self.data_fill_request = data_fill_request

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/datafill"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.data_fill_request.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
