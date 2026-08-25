"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostImportDataRequest(RequestOption):
    """Import data into the Excel file."""

    def __init__(
        self,
        name: str,
        import_option: Optional[ImportOption] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        region: Optional[str] = None,
        fonts_location: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.import_option = import_option
        self.folder = folder
        self.storage_name = storage_name
        self.region = region
        self.fonts_location = fonts_location

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/importdata"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.region:
            params["region"] = self.region
        if self.fonts_location:
            params["FontsLocation"] = self.fonts_location
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        if self.import_option is not None:
            return self.import_option.to_dict()
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
