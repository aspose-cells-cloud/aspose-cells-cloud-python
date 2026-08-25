"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostDigitalSignatureRequest(RequestOption):
    """Excel file digital signature."""

    def __init__(
        self,
        name: str,
        digitalsignaturefile: str,
        password: str,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not digitalsignaturefile:
            raise ValueError("digitalsignaturefile is required")
        if not password:
            raise ValueError("password is required")
        self.name = name
        self.digitalsignaturefile = digitalsignaturefile
        self.password = password
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/digitalsignature"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["digitalsignaturefile"] = self.digitalsignaturefile
        params["password"] = self.password
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
