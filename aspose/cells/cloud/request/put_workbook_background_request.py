"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class PutWorkbookBackgroundRequest(RequestOption):
    """Set background in the workbook."""

    def __init__(
        self,
        name: str,
        pic_path: Optional[str] = None,
        image_adapt_option: Optional[str] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        file: Optional[FileSource] = None,
    ):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.pic_path = pic_path
        self.image_adapt_option = image_adapt_option
        self.folder = folder
        self.storage_name = storage_name
        self.file = file

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/background"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.pic_path:
            params["picPath"] = self.pic_path
        if self.image_adapt_option:
            params["imageAdaptOption"] = self.image_adapt_option
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return {"File": self.file}
