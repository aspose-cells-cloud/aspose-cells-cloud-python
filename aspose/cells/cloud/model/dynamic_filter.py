"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DynamicFilter:
    """Represents the dynamic filter."""
    dynamic_filter_type: Optional[str] = None
    max_value: Optional[Any] = None
    value: Optional[Any] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.dynamic_filter_type is not None:
            result["DynamicFilterType"] = self.dynamic_filter_type
        if self.max_value is not None:
            result["MaxValue"] = self.max_value
        if self.value is not None:
            result["Value"] = self.value
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
