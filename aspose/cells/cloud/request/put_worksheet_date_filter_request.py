"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetDateFilterRequest(RequestOption):
    """Apply a date filter in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        range_: str,
        field_index: int,
        date_time_grouping_type: str,
        year: Optional[int] = None,
        month: Optional[int] = None,
        day: Optional[int] = None,
        hour: Optional[int] = None,
        minute: Optional[int] = None,
        second: Optional[int] = None,
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
        if not date_time_grouping_type:
            raise ValueError("dateTimeGroupingType is required")
        self.name = name
        self.sheet_name = sheet_name
        self.range_ = range_
        self.field_index = field_index
        self.date_time_grouping_type = date_time_grouping_type
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second
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
            "/autoFilter/dateFilter"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["range"] = self.range_
        params["fieldIndex"] = str(self.field_index)
        params["dateTimeGroupingType"] = self.date_time_grouping_type
        if self.year is not None:
            params["year"] = str(self.year)
        if self.month is not None:
            params["month"] = str(self.month)
        if self.day is not None:
            params["day"] = str(self.day)
        if self.hour is not None:
            params["hour"] = str(self.hour)
        if self.minute is not None:
            params["minute"] = str(self.minute)
        if self.second is not None:
            params["second"] = str(self.second)
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
