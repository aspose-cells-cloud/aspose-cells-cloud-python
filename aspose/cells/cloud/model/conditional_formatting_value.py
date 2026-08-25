"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ConditionalFormattingValue:
    """Describes the values of the interpolation points in a gradient scale, dataBar or iconSet."""
    is_gte: Optional[bool] = None
    type_: Optional[str] = None
    value: Optional[Any] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.is_gte is not None:
            result["IsGTE"] = self.is_gte
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.value is not None:
            result["Value"] = self.value
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
