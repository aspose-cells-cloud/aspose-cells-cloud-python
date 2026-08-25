"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PivotItem:
    """Represents a item in a PivotField report."""
    index: Optional[int] = None
    is_hidden: Optional[bool] = None
    name: Optional[str] = None
    value: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.index is not None:
            result["Index"] = self.index
        if self.is_hidden is not None:
            result["IsHidden"] = self.is_hidden
        if self.name is not None:
            result["Name"] = self.name
        if self.value is not None:
            result["Value"] = self.value
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
