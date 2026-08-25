"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataBarBorder:
    """Represents the border of the data bars specified by a conditional formatting rule."""
    color: Optional[Color] = None
    type_: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.type_ is not None:
            result["Type"] = self.type_
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
