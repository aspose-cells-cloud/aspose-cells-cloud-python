"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FillFormat:
    """Encapsulates the object that represents fill formatting for a shape."""
    type_: Optional[str] = None
    solid_fill: Optional[SolidFill] = None
    pattern_fill: Optional[PatternFill] = None
    texture_fill: Optional[TextureFill] = None
    gradient_fill: Optional[GradientFill] = None
    image_data: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.solid_fill is not None:
            result["SolidFill"] = self.solid_fill.to_dict()
        if self.pattern_fill is not None:
            result["PatternFill"] = self.pattern_fill.to_dict()
        if self.texture_fill is not None:
            result["TextureFill"] = self.texture_fill.to_dict()
        if self.gradient_fill is not None:
            result["GradientFill"] = self.gradient_fill.to_dict()
        if self.image_data is not None:
            result["ImageData"] = self.image_data
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
