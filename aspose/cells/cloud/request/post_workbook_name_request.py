"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorkbookNameRequest(RequestOption):
    """Update a named range in the workbook."""

    def __init__(
        self,
        name: str,
        name_name: str,
        new_name: Name,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not name_name:
            raise ValueError("nameName is required")
        if new_name is None:
            raise ValueError("newName is required")
        self.name = name
        self.name_name = name_name
        self.new_name = new_name
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/names/" +
            quote(self.name_name, safe="/")
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.new_name.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
