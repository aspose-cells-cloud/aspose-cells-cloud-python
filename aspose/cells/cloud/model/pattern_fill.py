"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PatternFill:
    """Encapsulates the object that represents pattern fill format"""
    pattern: Optional[str] = None
    background_cells_color: Optional[CellsColor] = None
    foreground_cells_color: Optional[CellsColor] = None
    foreground_color: Optional[Color] = None
    background_color: Optional[Color] = None
    back_transparency: Optional[float] = None
    fore_transparency: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.pattern is not None:
            result["Pattern"] = self.pattern
        if self.background_cells_color is not None:
            result["BackgroundCellsColor"] = self.background_cells_color.to_dict()
        if self.foreground_cells_color is not None:
            result["ForegroundCellsColor"] = self.foreground_cells_color.to_dict()
        if self.foreground_color is not None:
            result["ForegroundColor"] = self.foreground_color.to_dict()
        if self.background_color is not None:
            result["BackgroundColor"] = self.background_color.to_dict()
        if self.back_transparency is not None:
            result["BackTransparency"] = self.back_transparency
        if self.fore_transparency is not None:
            result["ForeTransparency"] = self.fore_transparency
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
