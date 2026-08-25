"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RangeSortRequest:
    """Indicates range sort request"""
    data_sorter: Optional[DataSorter] = None
    cell_area: Optional[Range] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_sorter is not None:
            result["DataSorter"] = self.data_sorter.to_dict()
        if self.cell_area is not None:
            result["CellArea"] = self.cell_area.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
