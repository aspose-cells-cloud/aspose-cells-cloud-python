"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetOleObjectRequest(RequestOption):
    """Add an OLE object in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        upper_left_row: Optional[int] = None,
        upper_left_column: Optional[int] = None,
        height: Optional[int] = None,
        width: Optional[int] = None,
        ole_file: Optional[str] = None,
        image_file: Optional[str] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.upper_left_row = upper_left_row
        self.upper_left_column = upper_left_column
        self.height = height
        self.width = width
        self.ole_file = ole_file
        self.image_file = image_file
        self.folder = folder
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/oleobjects"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.upper_left_row is not None:
            params["upperLeftRow"] = str(self.upper_left_row)
        if self.upper_left_column is not None:
            params["upperLeftColumn"] = str(self.upper_left_column)
        if self.height is not None:
            params["height"] = str(self.height)
        if self.width is not None:
            params["width"] = str(self.width)
        if self.ole_file:
            params["oleFile"] = self.ole_file
        if self.image_file:
            params["imageFile"] = self.image_file
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
