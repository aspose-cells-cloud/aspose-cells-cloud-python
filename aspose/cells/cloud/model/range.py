"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Range:
    """Range."""
    column_count: Optional[int] = None
    column_width: Optional[float] = None
    first_column: Optional[int] = None
    first_row: Optional[int] = None
    name: Optional[str] = None
    refers_to: Optional[str] = None
    row_count: Optional[int] = None
    row_height: Optional[float] = None
    worksheet: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.column_count is not None:
            result["ColumnCount"] = self.column_count
        if self.column_width is not None:
            result["ColumnWidth"] = self.column_width
        if self.first_column is not None:
            result["FirstColumn"] = self.first_column
        if self.first_row is not None:
            result["FirstRow"] = self.first_row
        if self.name is not None:
            result["Name"] = self.name
        if self.refers_to is not None:
            result["RefersTo"] = self.refers_to
        if self.row_count is not None:
            result["RowCount"] = self.row_count
        if self.row_height is not None:
            result["RowHeight"] = self.row_height
        if self.worksheet is not None:
            result["Worksheet"] = self.worksheet
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
