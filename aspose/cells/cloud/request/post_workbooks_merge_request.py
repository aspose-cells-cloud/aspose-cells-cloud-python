"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorkbooksMergeRequest(RequestOption):
    """Merge a workbook into the existing workbook."""

    def __init__(
        self,
        name: str,
        merge_with: str,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        merged_storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not merge_with:
            raise ValueError("mergeWith is required")
        self.name = name
        self.merge_with = merge_with
        self.folder = folder
        self.storage_name = storage_name
        self.merged_storage_name = merged_storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/merge"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["mergeWith"] = self.merge_with
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.merged_storage_name:
            params["mergedStorageName"] = self.merged_storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
