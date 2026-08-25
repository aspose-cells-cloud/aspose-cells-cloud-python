"""Request classes for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import os
from typing import Any, Dict, List, Optional
from urllib.parse import quote

from aspose.cells.cloud.request_option import RequestOption


class PutWorksheetChartRequest(RequestOption):
    """Add a new chart in the worksheet."""

    def __init__(
        self,
        name: str,
        sheet_name: str,
        chart_type: str,
        upper_left_row: Optional[int] = None,
        upper_left_column: Optional[int] = None,
        lower_right_row: Optional[int] = None,
        lower_right_column: Optional[int] = None,
        area: Optional[str] = None,
        is_vertical: Optional[bool] = None,
        category_data: Optional[str] = None,
        is_auto_get_serial_name: Optional[bool] = None,
        title: Optional[str] = None,
        folder: Optional[str] = None,
        data_labels: Optional[bool] = None,
        data_labels_position: Optional[str] = None,
        pivot_table_sheet: Optional[str] = None,
        pivot_table_name: Optional[str] = None,
        storage_name: Optional[str] = None,
    ):
        if not name:
            raise ValueError("name is required")
        if not sheet_name:
            raise ValueError("sheetName is required")
        if not chart_type:
            raise ValueError("chartType is required")
        self.name = name
        self.sheet_name = sheet_name
        self.chart_type = chart_type
        self.upper_left_row = upper_left_row
        self.upper_left_column = upper_left_column
        self.lower_right_row = lower_right_row
        self.lower_right_column = lower_right_column
        self.area = area
        self.is_vertical = is_vertical
        self.category_data = category_data
        self.is_auto_get_serial_name = is_auto_get_serial_name
        self.title = title
        self.folder = folder
        self.data_labels = data_labels
        self.data_labels_position = data_labels_position
        self.pivot_table_sheet = pivot_table_sheet
        self.pivot_table_name = pivot_table_name
        self.storage_name = storage_name

    def get_method(self) -> str:
        return "PUT"

    def get_path(self) -> str:
        return (
            "/v3.0/cells/" +
            quote(self.name, safe="/") +
            "/worksheets/" +
            quote(self.sheet_name, safe="/") +
            "/charts"
        )

    def get_query_parameters(self) -> Dict[str, str]:
        params: Dict[str, str] = {}
        params["chartType"] = self.chart_type
        if self.upper_left_row is not None:
            params["upperLeftRow"] = str(self.upper_left_row)
        if self.upper_left_column is not None:
            params["upperLeftColumn"] = str(self.upper_left_column)
        if self.lower_right_row is not None:
            params["lowerRightRow"] = str(self.lower_right_row)
        if self.lower_right_column is not None:
            params["lowerRightColumn"] = str(self.lower_right_column)
        if self.area:
            params["area"] = self.area
        if self.is_vertical is not None:
            params["isVertical"] = "true" if self.is_vertical else "false"
        if self.category_data:
            params["categoryData"] = self.category_data
        if self.is_auto_get_serial_name is not None:
            params["isAutoGetSerialName"] = "true" if self.is_auto_get_serial_name else "false"
        if self.title:
            params["title"] = self.title
        if self.folder:
            params["folder"] = self.folder
        if self.data_labels is not None:
            params["dataLabels"] = "true" if self.data_labels else "false"
        if self.data_labels_position:
            params["dataLabelsPosition"] = self.data_labels_position
        if self.pivot_table_sheet:
            params["pivotTableSheet"] = self.pivot_table_sheet
        if self.pivot_table_name:
            params["pivotTableName"] = self.pivot_table_name
        if self.storage_name:
            params["storageName"] = self.storage_name
        return params

    def get_header_parameters(self) -> Dict[str, str]:
        return {}

    def get_json_body(self) -> Optional[Any]:
        return None

    def get_multipart_form(self) -> Optional[dict]:
        return None
