"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorkbookExportXMLRequest(RequestOption):
    """Export XML data from an Excel file. When there are XML Maps in an Excel file, export XML data. When there is no XML map in the Excel file, convert the Excel file to an XML file."""

    def __init__(
        self,
        name: str,
        password: Optional[str] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        out_path: Optional[str] = None,
        out_storage_name: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
        region: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        self.name = name
        self.password = password
        self.folder = folder
        self.storage_name = storage_name
        self.out_path = out_path
        self.out_storage_name = out_storage_name
        self.check_excel_restriction = check_excel_restriction
        self.region = region

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/exportxml"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.password:
            params["password"] = self.password
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.out_path:
            params["outPath"] = self.out_path
        if self.out_storage_name:
            params["outStorageName"] = self.out_storage_name
        if self.check_excel_restriction is not None:
            params["checkExcelRestriction"] = "true" if self.check_excel_restriction else "false"
        if self.region:
            params["region"] = self.region
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
