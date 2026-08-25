"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorkbookCalculateFormulaRequest(RequestOption):
    """Calculate all formulas in the workbook."""

    def __init__(
        self,
        name: str,
        options: Optional[CalculationOptions] = None,
        ignore_error: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.options = options
        self.ignore_error = ignore_error
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/calculateformula"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.ignore_error is not None:
            params["ignoreError"] = "true" if self.ignore_error else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        if self.options is not None:
            return self.options.to_dict()
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
