"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DiscoverPivotTable:
    """Represents a pivot table, which is a pivot table created based on data analysis of a table."""
    name: Optional[str] = None
    title: Optional[str] = None
    data_range: Optional[str] = None
    pivot_field_rows: Optional[List[int]] = None
    pivot_field_columns: Optional[List[int]] = None
    pivot_field_data: Optional[List[int]] = None
    thumbnail: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.title is not None:
            result["Title"] = self.title
        if self.data_range is not None:
            result["DataRange"] = self.data_range
        if self.pivot_field_rows is not None:
            result["PivotFieldRows"] = self.pivot_field_rows
        if self.pivot_field_columns is not None:
            result["PivotFieldColumns"] = self.pivot_field_columns
        if self.pivot_field_data is not None:
            result["PivotFieldData"] = self.pivot_field_data
        if self.thumbnail is not None:
            result["Thumbnail"] = self.thumbnail
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
