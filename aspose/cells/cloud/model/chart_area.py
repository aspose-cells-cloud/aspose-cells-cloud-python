"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ChartArea:
    """Encapsulates the object that represents the chart area in the worksheet."""
    area: Optional[Area] = None
    auto_scale_font: Optional[bool] = None
    background_mode: Optional[str] = None
    border: Optional[Line] = None
    font: Optional[Font] = None
    is_automatic_size: Optional[bool] = None
    is_inner_mode: Optional[bool] = None
    shadow: Optional[bool] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.area is not None:
            result["Area"] = self.area.to_dict()
        if self.auto_scale_font is not None:
            result["AutoScaleFont"] = self.auto_scale_font
        if self.background_mode is not None:
            result["BackgroundMode"] = self.background_mode
        if self.border is not None:
            result["Border"] = self.border.to_dict()
        if self.font is not None:
            result["Font"] = self.font.to_dict()
        if self.is_automatic_size is not None:
            result["IsAutomaticSize"] = self.is_automatic_size
        if self.is_inner_mode is not None:
            result["IsInnerMode"] = self.is_inner_mode
        if self.shadow is not None:
            result["Shadow"] = self.shadow
        if self.width is not None:
            result["Width"] = self.width
        if self.height is not None:
            result["Height"] = self.height
        if self.x is not None:
            result["X"] = self.x
        if self.y is not None:
            result["Y"] = self.y
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
