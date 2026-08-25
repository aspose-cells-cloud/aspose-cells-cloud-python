"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ColorFilterRequest:
    """Indicates color filter request"""
    pattern: Optional[str] = None
    foreground_color: Optional[CellsColor] = None
    background_color: Optional[CellsColor] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.pattern is not None:
            result["Pattern"] = self.pattern
        if self.foreground_color is not None:
            result["ForegroundColor"] = self.foreground_color.to_dict()
        if self.background_color is not None:
            result["BackgroundColor"] = self.background_color.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
