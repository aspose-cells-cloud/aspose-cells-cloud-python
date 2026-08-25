"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SolidFill:
    """Encapsulates the object that represents solid fill format"""
    color: Optional[Color] = None
    cells_color: Optional[CellsColor] = None
    transparency: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.cells_color is not None:
            result["CellsColor"] = self.cells_color.to_dict()
        if self.transparency is not None:
            result["Transparency"] = self.transparency
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
