"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetAddPictureRequest(RequestOption):
    """Add a new picture in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        picture: Optional[Picture] = None,
        upper_left_row: Optional[int] = None,
        upper_left_column: Optional[int] = None,
        lower_right_row: Optional[int] = None,
        lower_right_column: Optional[int] = None,
        picture_path: Optional[str] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        self.name = name
        self.sheet_name = sheet_name
        self.picture = picture
        self.upper_left_row = upper_left_row
        self.upper_left_column = upper_left_column
        self.lower_right_row = lower_right_row
        self.lower_right_column = lower_right_column
        self.picture_path = picture_path
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
            "/pictures"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.upper_left_row is not None:
            params["upperLeftRow"] = str(self.upper_left_row)
        if self.upper_left_column is not None:
            params["upperLeftColumn"] = str(self.upper_left_column)
        if self.lower_right_row is not None:
            params["lowerRightRow"] = str(self.lower_right_row)
        if self.lower_right_column is not None:
            params["lowerRightColumn"] = str(self.lower_right_column)
        if self.picture_path:
            params["picturePath"] = self.picture_path
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        if self.picture is not None:
            return self.picture.to_dict()
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
