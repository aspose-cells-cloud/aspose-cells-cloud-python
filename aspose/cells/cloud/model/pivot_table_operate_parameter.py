"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PivotTableOperateParameter:
    """Represents pivot table operate parameter."""
    source_data: Optional[str] = None
    dest_cell_name: Optional[str] = None
    table_name: Optional[str] = None
    use_same_source: Optional[bool] = None
    pivot_table_index: Optional[int] = None
    pivot_field_rows: Optional[List[int]] = None
    pivot_field_columns: Optional[List[int]] = None
    pivot_field_data: Optional[List[int]] = None
    operate_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.source_data is not None:
            result["SourceData"] = self.source_data
        if self.dest_cell_name is not None:
            result["DestCellName"] = self.dest_cell_name
        if self.table_name is not None:
            result["TableName"] = self.table_name
        if self.use_same_source is not None:
            result["UseSameSource"] = self.use_same_source
        if self.pivot_table_index is not None:
            result["PivotTableIndex"] = self.pivot_table_index
        if self.pivot_field_rows is not None:
            result["PivotFieldRows"] = self.pivot_field_rows
        if self.pivot_field_columns is not None:
            result["PivotFieldColumns"] = self.pivot_field_columns
        if self.pivot_field_data is not None:
            result["PivotFieldData"] = self.pivot_field_data
        if self.operate_type is not None:
            result["OperateType"] = self.operate_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
