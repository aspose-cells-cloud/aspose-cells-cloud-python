"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostDeleteIncompleteRowsRequest(RequestOption):
    """Deleting incomplete rows of spreadsheet files is mainly used to eliminate incomplete rows in tables and ranges."""

    def __init__(
        self,
        delete_incomplete_rows_request: DeleteIncompleteRowsRequest,
    ):
        if delete_incomplete_rows_request is None:
            raise ValueError("deleteIncompleteRowsRequest is required")
        self.delete_incomplete_rows_request = delete_incomplete_rows_request

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/deleteincompleterows"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.delete_incomplete_rows_request.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
