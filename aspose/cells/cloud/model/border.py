"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Border:
    """Encapsulates the object that represents the cell border."""
    line_style: Optional[str] = None
    color: Optional[Color] = None
    border_type: Optional[str] = None
    theme_color: Optional[ThemeColor] = None
    argb_color: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.line_style is not None:
            result["LineStyle"] = self.line_style
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.border_type is not None:
            result["BorderType"] = self.border_type
        if self.theme_color is not None:
            result["ThemeColor"] = self.theme_color.to_dict()
        if self.argb_color is not None:
            result["ArgbColor"] = self.argb_color
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
