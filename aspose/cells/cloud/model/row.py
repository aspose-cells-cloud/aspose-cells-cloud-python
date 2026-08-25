"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Row:
    """Represents a single row in a worksheet."""
    group_level: Optional[int] = None
    height: Optional[float] = None
    index: Optional[int] = None
    is_blank: Optional[bool] = None
    is_height_matched: Optional[bool] = None
    is_hidden: Optional[bool] = None
    style: Optional[LinkElement] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.group_level is not None:
            result["GroupLevel"] = self.group_level
        if self.height is not None:
            result["Height"] = self.height
        if self.index is not None:
            result["Index"] = self.index
        if self.is_blank is not None:
            result["IsBlank"] = self.is_blank
        if self.is_height_matched is not None:
            result["IsHeightMatched"] = self.is_height_matched
        if self.is_hidden is not None:
            result["IsHidden"] = self.is_hidden
        if self.style is not None:
            result["Style"] = self.style.to_dict()
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
