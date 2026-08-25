"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostUpdateWorksheetOleObjectRequest(RequestOption):
    """Update an OLE object in worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        ole_object_index: int,
        ole: OleObject,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if ole_object_index is None:
            raise ValueError("oleObjectIndex is required")
        if ole is None:
            raise ValueError("ole is required")
        self.name = name
        self.sheet_name = sheet_name
        self.ole_object_index = ole_object_index
        self.ole = ole
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/oleobjects/" +
            quote(str(self.ole_object_index), safe="/")
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
        return self.ole.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
