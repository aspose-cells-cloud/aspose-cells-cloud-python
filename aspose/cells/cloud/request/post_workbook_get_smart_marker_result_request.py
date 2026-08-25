"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorkbookGetSmartMarkerResultRequest(RequestOption):
    """Smart marker processing."""

    def __init__(
        self,
        name: str,
        xml_file: Optional[str] = None,
        folder: Optional[str] = None,
        out_path: Optional[str] = None,
        storage_name: Optional[str] = None,
        out_storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.xml_file = xml_file
        self.folder = folder
        self.out_path = out_path
        self.storage_name = storage_name
        self.out_storage_name = out_storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/smartmarker"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.xml_file:
            params["xmlFile"] = self.xml_file
        if self.folder:
            params["folder"] = self.folder
        if self.out_path:
            params["outPath"] = self.out_path
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.out_storage_name:
            params["outStorageName"] = self.out_storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
