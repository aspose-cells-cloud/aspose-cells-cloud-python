"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CellsColor:
    """Represents all types of color."""
    color: Optional[Color] = None
    color_index: Optional[int] = None
    is_shape_color: Optional[bool] = None
    tint: Optional[float] = None
    argb: Optional[int] = None
    theme_color: Optional[ThemeColor] = None
    type_: Optional[str] = None
    transparency: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.color_index is not None:
            result["ColorIndex"] = self.color_index
        if self.is_shape_color is not None:
            result["IsShapeColor"] = self.is_shape_color
        if self.tint is not None:
            result["tint"] = self.tint
        if self.argb is not None:
            result["Argb"] = self.argb
        if self.theme_color is not None:
            result["ThemeColor"] = self.theme_color.to_dict()
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.transparency is not None:
            result["Transparency"] = self.transparency
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
