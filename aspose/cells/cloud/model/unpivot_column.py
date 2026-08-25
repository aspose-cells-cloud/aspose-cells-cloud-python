"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class UnpivotColumn:
    """Unpivot column."""
    unpivot_column_names: Optional[List[str]] = None
    column_map_name: Optional[str] = None
    value_map_name: Optional[str] = None
    applied_operate_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.unpivot_column_names is not None:
            result["UnpivotColumnNames"] = self.unpivot_column_names
        if self.column_map_name is not None:
            result["ColumnMapName"] = self.column_map_name
        if self.value_map_name is not None:
            result["ValueMapName"] = self.value_map_name
        if self.applied_operate_type is not None:
            result["AppliedOperateType"] = self.applied_operate_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
