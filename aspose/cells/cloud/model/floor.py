"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Floor:
    """Encapsulates the object that represents the floor of a 3-D chart."""
    border: Optional[Line] = None
    background_color: Optional[Color] = None
    fill_format: Optional[FillFormat] = None
    foreground_color: Optional[Color] = None
    format_: Optional[str] = None
    invert_if_negative: Optional[bool] = None
    transparency: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.border is not None:
            result["Border"] = self.border.to_dict()
        if self.background_color is not None:
            result["BackgroundColor"] = self.background_color.to_dict()
        if self.fill_format is not None:
            result["FillFormat"] = self.fill_format.to_dict()
        if self.foreground_color is not None:
            result["ForegroundColor"] = self.foreground_color.to_dict()
        if self.format_ is not None:
            result["Format"] = self.format_
        if self.invert_if_negative is not None:
            result["InvertIfNegative"] = self.invert_if_negative
        if self.transparency is not None:
            result["Transparency"] = self.transparency
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
