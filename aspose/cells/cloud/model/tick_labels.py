"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TickLabels:
    """Represents the tick-mark labels associated with tick marks on a chart axis."""
    auto_scale_font: Optional[bool] = None
    background_mode: Optional[str] = None
    font: Optional[Font] = None
    number: Optional[int] = None
    number_format: Optional[str] = None
    number_format_linked: Optional[bool] = None
    offset: Optional[int] = None
    rotation_angle: Optional[int] = None
    text_direction: Optional[str] = None
    reading_order: Optional[str] = None
    direction_type: Optional[str] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.auto_scale_font is not None:
            result["AutoScaleFont"] = self.auto_scale_font
        if self.background_mode is not None:
            result["BackgroundMode"] = self.background_mode
        if self.font is not None:
            result["Font"] = self.font.to_dict()
        if self.number is not None:
            result["Number"] = self.number
        if self.number_format is not None:
            result["NumberFormat"] = self.number_format
        if self.number_format_linked is not None:
            result["NumberFormatLinked"] = self.number_format_linked
        if self.offset is not None:
            result["Offset"] = self.offset
        if self.rotation_angle is not None:
            result["RotationAngle"] = self.rotation_angle
        if self.text_direction is not None:
            result["TextDirection"] = self.text_direction
        if self.reading_order is not None:
            result["ReadingOrder"] = self.reading_order
        if self.direction_type is not None:
            result["DirectionType"] = self.direction_type
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
