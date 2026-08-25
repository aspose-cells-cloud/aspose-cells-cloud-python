"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class GradientFill:
    """Represents the gradient fill."""
    fill_type: Optional[str] = None
    direction_type: Optional[str] = None
    angle: Optional[float] = None
    gradient_stops: Optional[List[GradientFillStop]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.fill_type is not None:
            result["FillType"] = self.fill_type
        if self.direction_type is not None:
            result["DirectionType"] = self.direction_type
        if self.angle is not None:
            result["Angle"] = self.angle
        if self.gradient_stops is not None:
            result["GradientStops"] = [x.to_dict() for x in self.gradient_stops]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
