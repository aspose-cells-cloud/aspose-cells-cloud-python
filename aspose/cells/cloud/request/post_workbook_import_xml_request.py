"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorkbookImportXMLRequest(RequestOption):
    """Import an XML data file into an Excel file. The XML data file can either be a cloud file or data from an HTTP URI."""

    def __init__(
        self,
        name: str,
        import_xml_request: ImportXMLRequest,
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
        if import_xml_request is None:
            raise ValueError("importXMLRequest is required")
        self.name = name
        self.import_xml_request = import_xml_request
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
            "/importxml"
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
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.import_xml_request.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
