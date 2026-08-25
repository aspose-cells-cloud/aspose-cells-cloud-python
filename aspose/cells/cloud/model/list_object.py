"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ListObject:
    """Represents a list object on a worksheet.            The ListObject object is a member of the ListObjects collection.             The ListObjects collection contains all the list objects on a worksheet."""
    auto_filter: Optional[AutoFilter] = None
    display_name: Optional[str] = None
    start_column: Optional[int] = None
    start_row: Optional[int] = None
    end_column: Optional[int] = None
    end_row: Optional[int] = None
    list_columns: Optional[List[ListColumn]] = None
    show_header_row: Optional[bool] = None
    show_table_style_column_stripes: Optional[bool] = None
    show_table_style_first_column: Optional[bool] = None
    show_table_style_last_column: Optional[bool] = None
    show_table_style_row_stripes: Optional[bool] = None
    show_totals: Optional[bool] = None
    table_style_name: Optional[str] = None
    table_style_type: Optional[str] = None
    data_range: Optional[Range] = None
    data_source_type: Optional[str] = None
    comment: Optional[str] = None
    xml_map: Optional[XmlMap] = None
    alternative_text: Optional[str] = None
    alternative_description: Optional[str] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.auto_filter is not None:
            result["AutoFilter"] = self.auto_filter.to_dict()
        if self.display_name is not None:
            result["DisplayName"] = self.display_name
        if self.start_column is not None:
            result["StartColumn"] = self.start_column
        if self.start_row is not None:
            result["StartRow"] = self.start_row
        if self.end_column is not None:
            result["EndColumn"] = self.end_column
        if self.end_row is not None:
            result["EndRow"] = self.end_row
        if self.list_columns is not None:
            result["ListColumns"] = [x.to_dict() for x in self.list_columns]
        if self.show_header_row is not None:
            result["ShowHeaderRow"] = self.show_header_row
        if self.show_table_style_column_stripes is not None:
            result["ShowTableStyleColumnStripes"] = self.show_table_style_column_stripes
        if self.show_table_style_first_column is not None:
            result["ShowTableStyleFirstColumn"] = self.show_table_style_first_column
        if self.show_table_style_last_column is not None:
            result["ShowTableStyleLastColumn"] = self.show_table_style_last_column
        if self.show_table_style_row_stripes is not None:
            result["ShowTableStyleRowStripes"] = self.show_table_style_row_stripes
        if self.show_totals is not None:
            result["ShowTotals"] = self.show_totals
        if self.table_style_name is not None:
            result["TableStyleName"] = self.table_style_name
        if self.table_style_type is not None:
            result["TableStyleType"] = self.table_style_type
        if self.data_range is not None:
            result["DataRange"] = self.data_range.to_dict()
        if self.data_source_type is not None:
            result["DataSourceType"] = self.data_source_type
        if self.comment is not None:
            result["Comment"] = self.comment
        if self.xml_map is not None:
            result["XmlMap"] = self.xml_map.to_dict()
        if self.alternative_text is not None:
            result["AlternativeText"] = self.alternative_text
        if self.alternative_description is not None:
            result["AlternativeDescription"] = self.alternative_description
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
