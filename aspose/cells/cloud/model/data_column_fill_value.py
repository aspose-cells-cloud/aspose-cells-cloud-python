"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataColumnFillValue:
    """Represents that the data column is populated with the specified value."""
    column_index: Optional[int] = None
    data_fill_value: Optional[DataFillValue] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.column_index is not None:
            result["ColumnIndex"] = self.column_index
        if self.data_fill_value is not None:
            result["DataFillValue"] = self.data_fill_value.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
