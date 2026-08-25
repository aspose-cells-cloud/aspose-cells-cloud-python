"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataFill:
    """Represents data filling."""
    ranges: Optional[List[Range]] = None
    data_fill_default_value: Optional[DataFillValue] = None
    data_column_fill_value_list: Optional[List[DataColumnFillValue]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.ranges is not None:
            result["Ranges"] = [x.to_dict() for x in self.ranges]
        if self.data_fill_default_value is not None:
            result["DataFillDefaultValue"] = self.data_fill_default_value.to_dict()
        if self.data_column_fill_value_list is not None:
            result["DataColumnFillValueList"] = [x.to_dict() for x in self.data_column_fill_value_list]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
