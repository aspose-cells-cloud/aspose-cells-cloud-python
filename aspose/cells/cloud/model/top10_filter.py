"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Top10Filter:
    """Represents the top 10 filter."""
    field_index: Optional[int] = None
    criteria: Optional[str] = None
    is_percent: Optional[bool] = None
    is_top: Optional[bool] = None
    items: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.field_index is not None:
            result["FieldIndex"] = self.field_index
        if self.criteria is not None:
            result["Criteria"] = self.criteria
        if self.is_percent is not None:
            result["IsPercent"] = self.is_percent
        if self.is_top is not None:
            result["IsTop"] = self.is_top
        if self.items is not None:
            result["Items"] = self.items
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
