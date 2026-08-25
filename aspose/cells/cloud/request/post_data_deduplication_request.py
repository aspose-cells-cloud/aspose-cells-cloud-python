"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostDataDeduplicationRequest(RequestOption):
    """Data deduplication of spreadsheet files is mainly used to eliminate duplicate data in tables and ranges."""

    def __init__(
        self,
        data_deduplication_request: DataDeduplicationRequest,
    ):
        if data_deduplication_request is None:
            raise ValueError("dataDeduplicationRequest is required")
        self.data_deduplication_request = data_deduplication_request

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/datadeduplication"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.data_deduplication_request.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
