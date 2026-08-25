"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ShadowEffect:
    """This class specifies the shadow effect of the chart element or shape."""
    angle: Optional[float] = None
    blur: Optional[float] = None
    color: Optional[CellsColor] = None
    distance: Optional[float] = None
    preset_type: Optional[str] = None
    size: Optional[float] = None
    transparency: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.angle is not None:
            result["Angle"] = self.angle
        if self.blur is not None:
            result["Blur"] = self.blur
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.distance is not None:
            result["Distance"] = self.distance
        if self.preset_type is not None:
            result["PresetType"] = self.preset_type
        if self.size is not None:
            result["Size"] = self.size
        if self.transparency is not None:
            result["Transparency"] = self.transparency
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
