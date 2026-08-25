"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PivotColumn:
    """Represents pivot column for data table."""
    pivot_column_name: Optional[str] = None
    value_column_names: Optional[List[str]] = None
    applied_operate_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.pivot_column_name is not None:
            result["PivotColumnName"] = self.pivot_column_name
        if self.value_column_names is not None:
            result["ValueColumnNames"] = self.value_column_names
        if self.applied_operate_type is not None:
            result["AppliedOperateType"] = self.applied_operate_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
