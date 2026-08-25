"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RenderingFont:
    """RenderingFont."""
    name: Optional[str] = None
    size: Optional[float] = None
    bold: Optional[bool] = None
    italic: Optional[bool] = None
    color: Optional[Color] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.size is not None:
            result["Size"] = self.size
        if self.bold is not None:
            result["Bold"] = self.bold
        if self.italic is not None:
            result["Italic"] = self.italic
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
