"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorksheetPictureRequest(RequestOption):
    """Update a picture by index in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        picture_index: int,
        picture: Picture,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if picture_index is None:
            raise ValueError("pictureIndex is required")
        if picture is None:
            raise ValueError("picture is required")
        self.name = name
        self.sheet_name = sheet_name
        self.picture_index = picture_index
        self.picture = picture
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
            "/pictures/" +
            quote(str(self.picture_index), safe="/")
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
        return self.picture.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
