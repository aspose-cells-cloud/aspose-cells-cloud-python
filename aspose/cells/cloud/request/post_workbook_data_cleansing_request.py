"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PostWorkbookDataCleansingRequest(RequestOption):
    """Data cleaning of spreadsheet files is a data management process used to identify, correct, and remove errors, incompleteness, duplicates, or inaccuracies in tables and ranges."""

    def __init__(
        self,
        name: str,
        data_cleansing: DataCleansing,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
        password: Optional[str] = None,
        region: Optional[str] = None,
        check_excel_restriction: Optional[bool] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if data_cleansing is None:
            raise ValueError("dataCleansing is required")
        self.name = name
        self.data_cleansing = data_cleansing
        self.folder = folder
        self.storage_name = storage_name
        self.password = password
        self.region = region
        self.check_excel_restriction = check_excel_restriction

    def get_method(self) -> str:
        return "POST"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/datacleansing"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        if self.password:
            params["password"] = self.password
        if self.region:
            params["region"] = self.region
        if self.check_excel_restriction is not None:
            params["checkExcelRestriction"] = "true" if self.check_excel_restriction else "false"
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {"Content-Type": "application/json"}

    def get_json_body(self) -> Optional[Any]:
        return self.data_cleansing.to_dict()

    def get_multipart_form(self) -> Optional[dict]:
        return None
