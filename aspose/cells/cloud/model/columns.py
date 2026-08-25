"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Columns:
    """Columns"""
    max_column: Optional[int] = None
    columns_count: Optional[int] = None
    columns_list: Optional[List[LinkElement]] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.max_column is not None:
            result["MaxColumn"] = self.max_column
        if self.columns_count is not None:
            result["ColumnsCount"] = self.columns_count
        if self.columns_list is not None:
            result["ColumnsList"] = [x.to_dict() for x in self.columns_list]
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
