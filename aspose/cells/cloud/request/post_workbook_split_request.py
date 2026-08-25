"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorkbookSplitRequest(RequestOption):
    """Split the workbook with a specific format."""

    def __init__(
        self,
        name: str,
        format_: Optional[str] = None,
        out_folder: Optional[str] = None,
        from_: Optional[int] = None,
        to: Optional[int] = None,
        horizontal_resolution: Optional[int] = None,
        vertical_resolution: Optional[int] = None,
        split_name_rule: Optional[str] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        out_storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.format_ = format_
        self.out_folder = out_folder
        self.from_ = from_
        self.to = to
        self.horizontal_resolution = horizontal_resolution
        self.vertical_resolution = vertical_resolution
        self.split_name_rule = split_name_rule
        self.folder = folder
        self.storage_name = storage_name
        self.out_storage_name = out_storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/split"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.format_:
            params["format"] = self.format_
        if self.out_folder:
            params["outFolder"] = self.out_folder
        if self.from_ is not None:
            params["from"] = str(self.from_)
        if self.to is not None:
            params["to"] = str(self.to)
        if self.horizontal_resolution is not None:
            params["horizontalResolution"] = str(self.horizontal_resolution)
        if self.vertical_resolution is not None:
            params["verticalResolution"] = str(self.vertical_resolution)
        if self.split_name_rule:
            params["splitNameRule"] = self.split_name_rule
        if self.folder:
            params["folder"] = self.folder
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
