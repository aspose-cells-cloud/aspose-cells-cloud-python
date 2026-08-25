"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostAutofitWorkbookRowsRequest(RequestOption):
    """Autofit rows in the workbook."""

    def __init__(
        self,
        name: str,
        start_row: Optional[int] = None,
        end_row: Optional[int] = None,
        only_auto: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        first_column: Optional[int] = None,
        last_column: Optional[int] = None,
    ):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.start_row = start_row
        self.end_row = end_row
        self.only_auto = only_auto
        self.folder = folder
        self.storage_name = storage_name
        self.first_column = first_column
        self.last_column = last_column

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/autofitrows"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.start_row is not None:
            params["startRow"] = str(self.start_row)
        if self.end_row is not None:
            params["endRow"] = str(self.end_row)
        if self.only_auto is not None:
            params["onlyAuto"] = "true" if self.only_auto else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.first_column is not None:
            params["firstColumn"] = str(self.first_column)
        if self.last_column is not None:
            params["lastColumn"] = str(self.last_column)
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
