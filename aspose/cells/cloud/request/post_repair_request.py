"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class PostRepairRequest(RequestOption):
    """Repair abnormal files and generate files in various formats."""

    def __init__(
        self,
        file: FileSource,
        out_format: Optional[str] = None,
    ):
        if not file:
            raise ValueError("File is required")
        self.file = file
        self.out_format = out_format

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/repair"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.out_format:
            params["outFormat"] = self.out_format
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"File": self.file}
