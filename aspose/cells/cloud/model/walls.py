"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Walls:
    """Encapsulates the object that represents the walls of a 3-D chart."""
    center_x: Optional[int] = None
    center_y: Optional[int] = None
    depth: Optional[int] = None
    height: Optional[int] = None
    width: Optional[int] = None
    border: Optional[Line] = None
    background_color: Optional[Color] = None
    fill_format: Optional[FillFormat] = None
    foreground_color: Optional[Color] = None
    format_: Optional[str] = None
    invert_if_negative: Optional[bool] = None
    transparency: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.center_x is not None:
            result["CenterX"] = self.center_x
        if self.center_y is not None:
            result["CenterY"] = self.center_y
        if self.depth is not None:
            result["Depth"] = self.depth
        if self.height is not None:
            result["Height"] = self.height
        if self.width is not None:
            result["Width"] = self.width
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
