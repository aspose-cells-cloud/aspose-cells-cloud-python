"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetCustomFilterRequest(RequestOption):
    """Filter a list with custom criteria in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        range_: str,
        field_index: int,
        operator_type1: str,
        criteria1: str,
        is_and: Optional[bool] = None,
        operator_type2: Optional[str] = None,
        criteria2: Optional[str] = None,
        match_blanks: Optional[bool] = None,
        refresh: Optional[bool] = None,
        folder: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if not range_:
            raise ValueError("range is required")
        if field_index is None:
            raise ValueError("fieldIndex is required")
        if not operator_type1:
            raise ValueError("operatorType1 is required")
        if not criteria1:
            raise ValueError("criteria1 is required")
        self.name = name
        self.sheet_name = sheet_name
        self.range_ = range_
        self.field_index = field_index
        self.operator_type1 = operator_type1
        self.criteria1 = criteria1
        self.is_and = is_and
        self.operator_type2 = operator_type2
        self.criteria2 = criteria2
        self.match_blanks = match_blanks
        self.refresh = refresh
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
            "/autoFilter/custom"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["range"] = self.range_
        params["fieldIndex"] = str(self.field_index)
        params["operatorType1"] = self.operator_type1
        params["criteria1"] = self.criteria1
        if self.is_and is not None:
            params["isAnd"] = "true" if self.is_and else "false"
        if self.operator_type2:
            params["operatorType2"] = self.operator_type2
        if self.criteria2:
            params["criteria2"] = self.criteria2
        if self.match_blanks is not None:
            params["matchBlanks"] = "true" if self.match_blanks else "false"
        if self.refresh is not None:
            params["refresh"] = "true" if self.refresh else "false"
        if self.folder:
            params["folder"] = self.folder
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
