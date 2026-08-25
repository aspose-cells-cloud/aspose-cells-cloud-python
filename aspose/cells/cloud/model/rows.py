"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Rows:
    """Collects the  objects that represent the individual rows in a worksheet."""
    max_row: Optional[int] = None
    rows_count: Optional[int] = None
    rows_list: Optional[List[LinkElement]] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.max_row is not None:
            result["MaxRow"] = self.max_row
        if self.rows_count is not None:
            result["RowsCount"] = self.rows_count
        if self.rows_list is not None:
            result["RowsList"] = [x.to_dict() for x in self.rows_list]
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
