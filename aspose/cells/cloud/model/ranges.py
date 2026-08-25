"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Ranges:
    """Encapsulates a collection of  objects."""
    range_list: Optional[List[Range]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.range_list is not None:
            result["RangeList"] = [x.to_dict() for x in self.range_list]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
