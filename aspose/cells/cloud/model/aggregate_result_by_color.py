"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AggregateResultByColor:
    """AggregateResultByColor."""
    aggregate_operation: Optional[str] = None
    color_name: Optional[str] = None
    count: Optional[int] = None
    sum_: Optional[float] = None
    max_value: Optional[float] = None
    min_value: Optional[float] = None
    average_value: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.aggregate_operation is not None:
            result["AggregateOperation"] = self.aggregate_operation
        if self.color_name is not None:
            result["ColorName"] = self.color_name
        if self.count is not None:
            result["Count"] = self.count
        if self.sum_ is not None:
            result["Sum"] = self.sum_
        if self.max_value is not None:
            result["MaxValue"] = self.max_value
        if self.min_value is not None:
            result["MinValue"] = self.min_value
        if self.average_value is not None:
            result["AverageValue"] = self.average_value
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
