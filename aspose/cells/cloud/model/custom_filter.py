"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CustomFilter:
    """Represents the custom filter."""
    criteria: Optional[Any] = None
    filter_operator_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.criteria is not None:
            result["Criteria"] = self.criteria
        if self.filter_operator_type is not None:
            result["FilterOperatorType"] = self.filter_operator_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
