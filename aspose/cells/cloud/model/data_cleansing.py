"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataCleansing:
    """Represents data cleansing."""
    ranges: Optional[List[Range]] = None
    need_fill_data: Optional[bool] = None
    data_fill: Optional[DataFill] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.ranges is not None:
            result["Ranges"] = [x.to_dict() for x in self.ranges]
        if self.need_fill_data is not None:
            result["NeedFillData"] = self.need_fill_data
        if self.data_fill is not None:
            result["DataFill"] = self.data_fill.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
