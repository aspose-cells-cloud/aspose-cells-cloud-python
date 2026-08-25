"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostDataCleansingRequest(RequestOption):
    """Data cleansing of spreadsheet files is a data management process used to identify, correct, and remove errors, incompleteness, duplicates, or inaccuracies in tables and ranges."""

    def __init__(
        self,
        data_cleansing_request: DataCleansingRequest,
    ):
        if data_cleansing_request is None:
            raise ValueError("dataCleansingRequest is required")
        self.data_cleansing_request = data_cleansing_request

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/datacleansing"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.data_cleansing_request.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
