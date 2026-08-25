"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TableTotalRequest:
    """Indicates table total request"""
    list_column_index: Optional[int] = None
    totals_calculation: Optional[str] = None
    custom_formula: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.list_column_index is not None:
            result["ListColumnIndex"] = self.list_column_index
        if self.totals_calculation is not None:
            result["TotalsCalculation"] = self.totals_calculation
        if self.custom_formula is not None:
            result["CustomFormula"] = self.custom_formula
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
