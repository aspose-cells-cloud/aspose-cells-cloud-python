"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AbstractCalculationMonitor:
    """Monitor for user to track the progress of formula calculation."""
    original_value: Optional[Any] = None
    value_changed: Optional[bool] = None
    calculated_value: Optional[Any] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.original_value is not None:
            result["OriginalValue"] = self.original_value
        if self.value_changed is not None:
            result["ValueChanged"] = self.value_changed
        if self.calculated_value is not None:
            result["CalculatedValue"] = self.calculated_value
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
