"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RangeSetOutlineBorderRequest:
    """Indicates range set outline border request."""
    range_: Optional[Range] = None
    border_edge: Optional[str] = None
    border_style: Optional[str] = None
    border_color: Optional[Color] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.range_ is not None:
            result["Range"] = self.range_.to_dict()
        if self.border_edge is not None:
            result["borderEdge"] = self.border_edge
        if self.border_style is not None:
            result["borderStyle"] = self.border_style
        if self.border_color is not None:
            result["borderColor"] = self.border_color.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
