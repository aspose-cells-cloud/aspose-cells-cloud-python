"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FilterColumn:
    """Represents a filter for a single column. The Filter object is a member of the Filters collection"""
    field_index: Optional[int] = None
    filter_type: Optional[str] = None
    multiple_filters: Optional[MultipleFilters] = None
    color_filter: Optional[ColorFilter] = None
    custom_filters: Optional[List[CustomFilter]] = None
    dynamic_filter: Optional[DynamicFilter] = None
    icon_filter: Optional[IconFilter] = None
    top10_filter: Optional[Top10Filter] = None
    visibledropdown: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.field_index is not None:
            result["FieldIndex"] = self.field_index
        if self.filter_type is not None:
            result["FilterType"] = self.filter_type
        if self.multiple_filters is not None:
            result["MultipleFilters"] = self.multiple_filters.to_dict()
        if self.color_filter is not None:
            result["ColorFilter"] = self.color_filter.to_dict()
        if self.custom_filters is not None:
            result["CustomFilters"] = [x.to_dict() for x in self.custom_filters]
        if self.dynamic_filter is not None:
            result["DynamicFilter"] = self.dynamic_filter.to_dict()
        if self.icon_filter is not None:
            result["IconFilter"] = self.icon_filter.to_dict()
        if self.top10_filter is not None:
            result["Top10Filter"] = self.top10_filter.to_dict()
        if self.visibledropdown is not None:
            result["Visibledropdown"] = self.visibledropdown
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
