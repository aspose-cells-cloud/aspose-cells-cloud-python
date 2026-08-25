"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PivotFilter:
    """Represents a PivotFilter in PivotFilter Collection."""
    auto_filter: Optional[AutoFilter] = None
    evaluation_order: Optional[int] = None
    field_index: Optional[int] = None
    filter_type: Optional[str] = None
    value_field_index: Optional[int] = None
    member_property_field_index: Optional[int] = None
    name: Optional[str] = None
    value1: Optional[str] = None
    value2: Optional[str] = None
    top10_filter: Optional[Top10Filter] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.auto_filter is not None:
            result["AutoFilter"] = self.auto_filter.to_dict()
        if self.evaluation_order is not None:
            result["EvaluationOrder"] = self.evaluation_order
        if self.field_index is not None:
            result["FieldIndex"] = self.field_index
        if self.filter_type is not None:
            result["FilterType"] = self.filter_type
        if self.value_field_index is not None:
            result["ValueFieldIndex"] = self.value_field_index
        if self.member_property_field_index is not None:
            result["MemberPropertyFieldIndex"] = self.member_property_field_index
        if self.name is not None:
            result["Name"] = self.name
        if self.value1 is not None:
            result["Value1"] = self.value1
        if self.value2 is not None:
            result["Value2"] = self.value2
        if self.top10_filter is not None:
            result["Top10Filter"] = self.top10_filter.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
