"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SingleValue:
    """Represents single value."""
    value: Optional[str] = None
    value_type: Optional[Any] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.value is not None:
            result["Value"] = self.value
        if self.value_type is not None:
            result["ValueType"] = self.value_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
