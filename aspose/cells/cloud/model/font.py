"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Font:
    """Encapsulates the font object used in a spreadsheet."""
    color: Optional[Color] = None
    double_size: Optional[float] = None
    is_bold: Optional[bool] = None
    is_italic: Optional[bool] = None
    is_strikeout: Optional[bool] = None
    is_subscript: Optional[bool] = None
    is_superscript: Optional[bool] = None
    name: Optional[str] = None
    size: Optional[int] = None
    underline: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.double_size is not None:
            result["DoubleSize"] = self.double_size
        if self.is_bold is not None:
            result["IsBold"] = self.is_bold
        if self.is_italic is not None:
            result["IsItalic"] = self.is_italic
        if self.is_strikeout is not None:
            result["IsStrikeout"] = self.is_strikeout
        if self.is_subscript is not None:
            result["IsSubscript"] = self.is_subscript
        if self.is_superscript is not None:
            result["IsSuperscript"] = self.is_superscript
        if self.name is not None:
            result["Name"] = self.name
        if self.size is not None:
            result["Size"] = self.size
        if self.underline is not None:
            result["Underline"] = self.underline
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
