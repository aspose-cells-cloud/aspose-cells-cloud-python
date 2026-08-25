"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ListColumn:
    """Represents a column in a Table."""
    name: Optional[str] = None
    range_: Optional[Range] = None
    totals_calculation: Optional[str] = None
    formula: Optional[str] = None
    totals_row_label: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.range_ is not None:
            result["Range"] = self.range_.to_dict()
        if self.totals_calculation is not None:
            result["TotalsCalculation"] = self.totals_calculation
        if self.formula is not None:
            result["Formula"] = self.formula
        if self.totals_row_label is not None:
            result["TotalsRowLabel"] = self.totals_row_label
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
