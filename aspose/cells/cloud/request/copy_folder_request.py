"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class CopyFolderRequest(RequestOption):
    """CopyFolderRequest."""

    def __init__(
        self,
        src_path: str,
        dest_path: str,
        src_storage_name: Optional[str] = None,
        dest_storage_name: Optional[str] = None,
    ):
        if not src_path:
            raise ValueError("srcPath is required")
        if not dest_path:
            raise ValueError("destPath is required")
        self.src_path = src_path
        self.dest_path = dest_path
        self.src_storage_name = src_storage_name
        self.dest_storage_name = dest_storage_name

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v4.0/cells/storage/folder/copy/" +
            quote(self.src_path, safe="/")
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["destPath"] = self.dest_path
        if self.src_storage_name:
            params["srcStorageName"] = self.src_storage_name
        if self.dest_storage_name:
            params["destStorageName"] = self.dest_storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
