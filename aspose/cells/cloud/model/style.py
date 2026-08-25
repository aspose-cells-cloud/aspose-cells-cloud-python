"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Style:
    """Represents display style of excel document,such as font,color,alignment,border,etc.            The Style object contains all style attributes (font, number format, alignment, and so on) as properties."""
    font: Optional[Font] = None
    name: Optional[str] = None
    culture_custom: Optional[str] = None
    custom: Optional[str] = None
    background_color: Optional[Color] = None
    foreground_color: Optional[Color] = None
    is_formula_hidden: Optional[bool] = None
    is_date_time: Optional[bool] = None
    is_text_wrapped: Optional[bool] = None
    is_gradient: Optional[bool] = None
    is_locked: Optional[bool] = None
    is_percent: Optional[bool] = None
    shrink_to_fit: Optional[bool] = None
    indent_level: Optional[int] = None
    number: Optional[int] = None
    rotation_angle: Optional[int] = None
    pattern: Optional[str] = None
    text_direction: Optional[str] = None
    vertical_alignment: Optional[str] = None
    horizontal_alignment: Optional[str] = None
    border_collection: Optional[List[Border]] = None
    background_theme_color: Optional[ThemeColor] = None
    foreground_theme_color: Optional[ThemeColor] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.font is not None:
            result["Font"] = self.font.to_dict()
        if self.name is not None:
            result["Name"] = self.name
        if self.culture_custom is not None:
            result["CultureCustom"] = self.culture_custom
        if self.custom is not None:
            result["Custom"] = self.custom
        if self.background_color is not None:
            result["BackgroundColor"] = self.background_color.to_dict()
        if self.foreground_color is not None:
            result["ForegroundColor"] = self.foreground_color.to_dict()
        if self.is_formula_hidden is not None:
            result["IsFormulaHidden"] = self.is_formula_hidden
        if self.is_date_time is not None:
            result["IsDateTime"] = self.is_date_time
        if self.is_text_wrapped is not None:
            result["IsTextWrapped"] = self.is_text_wrapped
        if self.is_gradient is not None:
            result["IsGradient"] = self.is_gradient
        if self.is_locked is not None:
            result["IsLocked"] = self.is_locked
        if self.is_percent is not None:
            result["IsPercent"] = self.is_percent
        if self.shrink_to_fit is not None:
            result["ShrinkToFit"] = self.shrink_to_fit
        if self.indent_level is not None:
            result["IndentLevel"] = self.indent_level
        if self.number is not None:
            result["Number"] = self.number
        if self.rotation_angle is not None:
            result["RotationAngle"] = self.rotation_angle
        if self.pattern is not None:
            result["Pattern"] = self.pattern
        if self.text_direction is not None:
            result["TextDirection"] = self.text_direction
        if self.vertical_alignment is not None:
            result["VerticalAlignment"] = self.vertical_alignment
        if self.horizontal_alignment is not None:
            result["HorizontalAlignment"] = self.horizontal_alignment
        if self.border_collection is not None:
            result["BorderCollection"] = [x.to_dict() for x in self.border_collection]
        if self.background_theme_color is not None:
            result["BackgroundThemeColor"] = self.background_theme_color.to_dict()
        if self.foreground_theme_color is not None:
            result["ForegroundThemeColor"] = self.foreground_theme_color.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
