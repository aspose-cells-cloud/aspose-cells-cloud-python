"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class GradientFillStop:
    """Class summary: Understanding the various features and tools available in Adobe Illustrator to create dynamic and professional vector graphics, including shapes, text, brushes, gradients, and layers."""
    color: Optional[Color] = None
    position: Optional[float] = None
    transparency: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.position is not None:
            result["Position"] = self.position
        if self.transparency is not None:
            result["Transparency"] = self.transparency
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
