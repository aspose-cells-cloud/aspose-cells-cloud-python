"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class NegativeBarFormat:
    """Represents the color settings of the data bars for negative values that are defined by a data bar conditional formating rule."""
    border_color: Optional[Color] = None
    border_color_type: Optional[str] = None
    color: Optional[Color] = None
    color_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.border_color is not None:
            result["BorderColor"] = self.border_color.to_dict()
        if self.border_color_type is not None:
            result["BorderColorType"] = self.border_color_type
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.color_type is not None:
            result["ColorType"] = self.color_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
