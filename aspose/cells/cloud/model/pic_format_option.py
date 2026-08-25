"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PicFormatOption:
    """Represents picture format option"""
    type_: Optional[str] = None
    scale: Optional[float] = None
    left: Optional[float] = None
    right: Optional[float] = None
    top: Optional[float] = None
    bottom: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.scale is not None:
            result["Scale"] = self.scale
        if self.left is not None:
            result["Left"] = self.left
        if self.right is not None:
            result["Right"] = self.right
        if self.top is not None:
            result["Top"] = self.top
        if self.bottom is not None:
            result["Bottom"] = self.bottom
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
