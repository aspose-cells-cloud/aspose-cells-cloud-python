"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataSorterKey:
    """Represents the key of the data sorter."""
    order: Optional[str] = None
    index: Optional[int] = None
    type_: Optional[str] = None
    icon_set_type: Optional[str] = None
    icon_id: Optional[int] = None
    color: Optional[Color] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.order is not None:
            result["Order"] = self.order
        if self.index is not None:
            result["Index"] = self.index
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.icon_set_type is not None:
            result["IconSetType"] = self.icon_set_type
        if self.icon_id is not None:
            result["IconId"] = self.icon_id
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
