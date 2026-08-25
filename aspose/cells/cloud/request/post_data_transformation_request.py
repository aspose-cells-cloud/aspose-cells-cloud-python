"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostDataTransformationRequest(RequestOption):
    """Transform spreadsheet data is mainly used to pivot columns, unpivot columns."""

    def __init__(
        self,
        data_transformation_request: DataTransformationRequest,
    ):
        if data_transformation_request is None:
            raise ValueError("dataTransformationRequest is required")
        self.data_transformation_request = data_transformation_request

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/datatransformation"

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.data_transformation_request.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
