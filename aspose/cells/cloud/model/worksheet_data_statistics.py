"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class WorksheetDataStatistics:
    """Represents worksheet data statistics."""
    name: Optional[str] = None
    charts_count: Optional[int] = None
    tables_count: Optional[int] = None
    pivot_tables_count: Optional[int] = None
    shapes_count: Optional[int] = None
    hyperlinks_count: Optional[int] = None
    query_tables_count: Optional[int] = None
    cells_count: Optional[int] = None
    cells_count_in_table: Optional[int] = None
    cells_count_is_formula: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.charts_count is not None:
            result["ChartsCount"] = self.charts_count
        if self.tables_count is not None:
            result["TablesCount"] = self.tables_count
        if self.pivot_tables_count is not None:
            result["PivotTablesCount"] = self.pivot_tables_count
        if self.shapes_count is not None:
            result["ShapesCount"] = self.shapes_count
        if self.hyperlinks_count is not None:
            result["HyperlinksCount"] = self.hyperlinks_count
        if self.query_tables_count is not None:
            result["QueryTablesCount"] = self.query_tables_count
        if self.cells_count is not None:
            result["CellsCount"] = self.cells_count
        if self.cells_count_in_table is not None:
            result["CellsCountInTable"] = self.cells_count_in_table
        if self.cells_count_is_formula is not None:
            result["CellsCountIsFormula"] = self.cells_count_is_formula
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
