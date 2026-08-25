"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class StorageExistsRequest(RequestOption):
    """StorageExistsRequest."""

    def __init__(
        self,
        storage_name: str,
    ):
        if not storage_name:
            raise ValueError("storageName is required")
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "GET"

    def get_path(self) -> str:
        return (
            "/v4.0/cells/storage/" +
            quote(self.storage_name, safe="/") +
            "/exist"
        )

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
