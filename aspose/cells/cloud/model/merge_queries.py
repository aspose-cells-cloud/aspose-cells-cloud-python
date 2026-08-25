"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class MergeQueries:
    """Represents merge quesies."""
    data_query_name_a: Optional[str] = None
    data_a_index_field: Optional[str] = None
    data_query_name_b: Optional[str] = None
    data_b_index_field: Optional[str] = None
    join_type: Optional[str] = None
    applied_operate_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_query_name_a is not None:
            result["DataQueryNameA"] = self.data_query_name_a
        if self.data_a_index_field is not None:
            result["DataAIndexField"] = self.data_a_index_field
        if self.data_query_name_b is not None:
            result["DataQueryNameB"] = self.data_query_name_b
        if self.data_b_index_field is not None:
            result["DataBIndexField"] = self.data_b_index_field
        if self.join_type is not None:
            result["JoinType"] = self.join_type
        if self.applied_operate_type is not None:
            result["AppliedOperateType"] = self.applied_operate_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
