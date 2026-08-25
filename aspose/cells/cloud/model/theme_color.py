"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ThemeColor:
    """Represents a theme color."""
    color_type: Optional[str] = None
    tint: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.color_type is not None:
            result["ColorType"] = self.color_type
        if self.tint is not None:
            result["Tint"] = self.tint
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
