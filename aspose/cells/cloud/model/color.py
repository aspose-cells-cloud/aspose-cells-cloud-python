"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Color:
    """Color."""
    a: Optional[bytes] = None
    r: Optional[bytes] = None
    g: Optional[bytes] = None
    b: Optional[bytes] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.a is not None:
            result["A"] = self.a
        if self.r is not None:
            result["R"] = self.r
        if self.g is not None:
            result["G"] = self.g
        if self.b is not None:
            result["B"] = self.b
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
