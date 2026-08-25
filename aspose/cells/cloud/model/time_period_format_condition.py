"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TimePeriodFormatCondition:
    """Represents time period format condition."""
    time_period: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.time_period is not None:
            result["TimePeriod"] = self.time_period
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
