"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption

from aspose.cells.cloud.file_source import FileSource


class PostMetadataRequest(RequestOption):
    """Update document properties in Excel file, and save them is various formats."""

    def __init__(
        self,
        file: FileSource,
        cells_documents: List[CellsDocumentProperty],
        password: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
        out_format: Optional[str] = None,
        region: Optional[str] = None,
    ):
        if not file:
            raise ValueError("File is required")
        if cells_documents is None:
            raise ValueError("cellsDocuments is required")
        self.file = file
        self.cells_documents = cells_documents
        self.password = password
        self.check_excel_restriction = check_excel_restriction
        self.out_format = out_format
        self.region = region

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return "/v3.0/cells/metadata/update"

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.password:
            params["password"] = self.password
        if self.check_excel_restriction is not None:
            params["checkExcelRestriction"] = "true" if self.check_excel_restriction else "false"
        if self.out_format:
            params["outFormat"] = self.out_format
        if self.region:
            params["region"] = self.region
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "multipart/form-data"}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        form = {}
        if self.file is not None:
            form["File"] = self.file
        if self.cells_documents is not None:
            form["cellsDocuments"] = json.dumps([x.to_dict() for x in self.cells_documents], default=str)
        return form
