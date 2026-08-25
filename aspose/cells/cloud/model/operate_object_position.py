"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class OperateObjectPosition:
    """Represents operate object position."""
    data_source: Optional[DataSource] = None
    workbook: Optional[FileSource] = None
    sheet_name: Optional[str] = None
    chart_index: Optional[int] = None
    shape_index: Optional[int] = None
    cell_name: Optional[str] = None
    list_object_index: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.workbook is not None:
            result["Workbook"] = self.workbook.to_dict()
        if self.sheet_name is not None:
            result["SheetName"] = self.sheet_name
        if self.chart_index is not None:
            result["ChartIndex"] = self.chart_index
        if self.shape_index is not None:
            result["ShapeIndex"] = self.shape_index
        if self.cell_name is not None:
            result["CellName"] = self.cell_name
        if self.list_object_index is not None:
            result["ListObjectIndex"] = self.list_object_index
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
