"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RangeSetStyleRequest:
    """Indicates range set style request."""
    range_: Optional[Range] = None
    style: Optional[Style] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.range_ is not None:
            result["Range"] = self.range_.to_dict()
        if self.style is not None:
            result["Style"] = self.style.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
