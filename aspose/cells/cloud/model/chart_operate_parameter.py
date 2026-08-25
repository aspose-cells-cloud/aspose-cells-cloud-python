"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ChartOperateParameter:
    """Represents chart operate parameter."""
    chart_index: Optional[int] = None
    chart_type: Optional[str] = None
    upper_left_row: Optional[int] = None
    upper_left_column: Optional[int] = None
    lower_right_row: Optional[int] = None
    lower_right_column: Optional[int] = None
    area: Optional[str] = None
    is_vertical: Optional[bool] = None
    category_data: Optional[str] = None
    is_auto_get_serial_name: Optional[bool] = None
    title: Optional[str] = None
    operate_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.chart_index is not None:
            result["ChartIndex"] = self.chart_index
        if self.chart_type is not None:
            result["ChartType"] = self.chart_type
        if self.upper_left_row is not None:
            result["UpperLeftRow"] = self.upper_left_row
        if self.upper_left_column is not None:
            result["UpperLeftColumn"] = self.upper_left_column
        if self.lower_right_row is not None:
            result["LowerRightRow"] = self.lower_right_row
        if self.lower_right_column is not None:
            result["LowerRightColumn"] = self.lower_right_column
        if self.area is not None:
            result["Area"] = self.area
        if self.is_vertical is not None:
            result["IsVertical"] = self.is_vertical
        if self.category_data is not None:
            result["CategoryData"] = self.category_data
        if self.is_auto_get_serial_name is not None:
            result["IsAutoGetSerialName"] = self.is_auto_get_serial_name
        if self.title is not None:
            result["Title"] = self.title
        if self.operate_type is not None:
            result["OperateType"] = self.operate_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
