"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PageBreakOperateParameter:
    """Represents page break operate parameter."""
    page_break_type: Optional[str] = None
    index: Optional[int] = None
    row: Optional[int] = None
    column: Optional[int] = None
    start_index: Optional[int] = None
    end_index: Optional[int] = None
    operate_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.page_break_type is not None:
            result["PageBreakType"] = self.page_break_type
        if self.index is not None:
            result["Index"] = self.index
        if self.row is not None:
            result["Row"] = self.row
        if self.column is not None:
            result["Column"] = self.column
        if self.start_index is not None:
            result["StartIndex"] = self.start_index
        if self.end_index is not None:
            result["EndIndex"] = self.end_index
        if self.operate_type is not None:
            result["OperateType"] = self.operate_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
