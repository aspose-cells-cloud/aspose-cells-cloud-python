"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DateTimeGroupItem:
    """Represents the datetime's group setting."""
    date_time_grouping_type: Optional[str] = None
    day: Optional[int] = None
    hour: Optional[int] = None
    minute: Optional[int] = None
    month: Optional[int] = None
    second: Optional[int] = None
    year: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.date_time_grouping_type is not None:
            result["DateTimeGroupingType"] = self.date_time_grouping_type
        if self.day is not None:
            result["Day"] = self.day
        if self.hour is not None:
            result["Hour"] = self.hour
        if self.minute is not None:
            result["Minute"] = self.minute
        if self.month is not None:
            result["Month"] = self.month
        if self.second is not None:
            result["Second"] = self.second
        if self.year is not None:
            result["Year"] = self.year
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
