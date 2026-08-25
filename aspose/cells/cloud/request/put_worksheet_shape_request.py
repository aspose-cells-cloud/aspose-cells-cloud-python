"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetShapeRequest(RequestOption):
    """Add a shape in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        shape_dto: Optional[Shape] = None,
        drawing_type: Optional[str] = None,
        upper_left_row: Optional[int] = None,
        upper_left_column: Optional[int] = None,
        top: Optional[int] = None,
        left: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.shape_dto = shape_dto
        self.drawing_type = drawing_type
        self.upper_left_row = upper_left_row
        self.upper_left_column = upper_left_column
        self.top = top
        self.left = left
        self.width = width
        self.height = height
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
            "/shapes"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.drawing_type:
            params["DrawingType"] = self.drawing_type
        if self.upper_left_row is not None:
            params["upperLeftRow"] = str(self.upper_left_row)
        if self.upper_left_column is not None:
            params["upperLeftColumn"] = str(self.upper_left_column)
        if self.top is not None:
            params["top"] = str(self.top)
        if self.left is not None:
            params["left"] = str(self.left)
        if self.width is not None:
            params["width"] = str(self.width)
        if self.height is not None:
            params["height"] = str(self.height)
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        if self.shape_dto is not None:
            return self.shape_dto.to_dict()
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
