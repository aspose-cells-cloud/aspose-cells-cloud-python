"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PivotTableFieldRequest:
    """Indicates pivot table field request"""
    data: Optional[List[int]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data is not None:
            result["Data"] = self.data
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
