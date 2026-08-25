"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class DeleteFolderRequest(RequestOption):
    """DeleteFolderRequest."""

    def __init__(
        self,
        path: str,
        storage_name: Optional[str] = None,
        recursive: Optional[bool] = None,
    ):
        if not path:
            raise ValueError("path is required")
        self.path = path
        self.storage_name = storage_name
        self.recursive = recursive

    def get_method(self) -> str:
        return "DELETE"

    def get_path(self) -> str:
        return (
            "/v4.0/cells/storage/folder/" +
            quote(self.path, safe="/")
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.recursive is not None:
            params["recursive"] = "true" if self.recursive else "false"
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
