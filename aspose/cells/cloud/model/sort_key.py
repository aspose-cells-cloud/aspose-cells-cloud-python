"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SortKey:
    """Represents sort key."""
    key: Optional[int] = None
    sort_order: Optional[str] = None
    custom_list: Optional[List[str]] = None
    order: Optional[str] = None
    index: Optional[int] = None
    type_: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.key is not None:
            result["Key"] = self.key
        if self.sort_order is not None:
            result["SortOrder"] = self.sort_order
        if self.custom_list is not None:
            result["CustomList"] = self.custom_list
        if self.order is not None:
            result["Order"] = self.order
        if self.index is not None:
            result["Index"] = self.index
        if self.type_ is not None:
            result["Type"] = self.type_
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
