"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class GlobalizationSettings:
    """Represents the globalization settings."""
    chart_settings: Optional[ChartGlobalizationSettings] = None
    pivot_settings: Optional[PivotGlobalizationSettings] = None
    list_separator: Optional[str] = None
    row_separator_of_formula_array: Optional[str] = None
    column_separator_of_formula_array: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.chart_settings is not None:
            result["ChartSettings"] = self.chart_settings.to_dict()
        if self.pivot_settings is not None:
            result["PivotSettings"] = self.pivot_settings.to_dict()
        if self.list_separator is not None:
            result["ListSeparator"] = self.list_separator
        if self.row_separator_of_formula_array is not None:
            result["RowSeparatorOfFormulaArray"] = self.row_separator_of_formula_array
        if self.column_separator_of_formula_array is not None:
            result["ColumnSeparatorOfFormulaArray"] = self.column_separator_of_formula_array
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
