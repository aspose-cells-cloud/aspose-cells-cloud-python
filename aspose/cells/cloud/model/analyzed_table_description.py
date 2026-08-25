"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AnalyzedTableDescription:
    """Represents analyzed table description."""
    name: Optional[str] = None
    sheet_name: Optional[str] = None
    columns: Optional[List[AnalyzedColumnDescription]] = None
    date_columns: Optional[List[int]] = None
    number_columns: Optional[List[int]] = None
    text_columns: Optional[List[int]] = None
    exception_columns: Optional[List[int]] = None
    has_table_header_row: Optional[bool] = None
    has_table_total_row: Optional[bool] = None
    start_data_column_index: Optional[int] = None
    end_data_column_index: Optional[int] = None
    start_data_row_index: Optional[int] = None
    end_data_row_index: Optional[int] = None
    thumbnail: Optional[str] = None
    discover_charts: Optional[List[DiscoverChart]] = None
    discover_pivot_tables: Optional[List[DiscoverPivotTable]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.sheet_name is not None:
            result["SheetName"] = self.sheet_name
        if self.columns is not None:
            result["Columns"] = [x.to_dict() for x in self.columns]
        if self.date_columns is not None:
            result["DateColumns"] = self.date_columns
        if self.number_columns is not None:
            result["NumberColumns"] = self.number_columns
        if self.text_columns is not None:
            result["TextColumns"] = self.text_columns
        if self.exception_columns is not None:
            result["ExceptionColumns"] = self.exception_columns
        if self.has_table_header_row is not None:
            result["HasTableHeaderRow"] = self.has_table_header_row
        if self.has_table_total_row is not None:
            result["HasTableTotalRow"] = self.has_table_total_row
        if self.start_data_column_index is not None:
            result["StartDataColumnIndex"] = self.start_data_column_index
        if self.end_data_column_index is not None:
            result["EndDataColumnIndex"] = self.end_data_column_index
        if self.start_data_row_index is not None:
            result["StartDataRowIndex"] = self.start_data_row_index
        if self.end_data_row_index is not None:
            result["EndDataRowIndex"] = self.end_data_row_index
        if self.thumbnail is not None:
            result["Thumbnail"] = self.thumbnail
        if self.discover_charts is not None:
            result["DiscoverCharts"] = [x.to_dict() for x in self.discover_charts]
        if self.discover_pivot_tables is not None:
            result["DiscoverPivotTables"] = [x.to_dict() for x in self.discover_pivot_tables]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
