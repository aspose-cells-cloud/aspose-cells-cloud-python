"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ColorFilter:
    """Color filter."""
    filter_by_fill_color: Optional[bool] = None
    pattern: Optional[str] = None
    color: Optional[CellsColor] = None
    foreground_color_color: Optional[CellsColor] = None
    background_color: Optional[CellsColor] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.filter_by_fill_color is not None:
            result["FilterByFillColor"] = self.filter_by_fill_color
        if self.pattern is not None:
            result["Pattern"] = self.pattern
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.foreground_color_color is not None:
            result["ForegroundColorColor"] = self.foreground_color_color.to_dict()
        if self.background_color is not None:
            result["BackgroundColor"] = self.background_color.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
