"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Cell:
    """Encapsulates the object that represents a single Workbook cell."""
    name: Optional[str] = None
    row: Optional[int] = None
    column: Optional[int] = None
    value: Optional[str] = None
    type_: Optional[str] = None
    formula: Optional[str] = None
    is_formula: Optional[bool] = None
    is_merged: Optional[bool] = None
    is_array_header: Optional[bool] = None
    is_in_array: Optional[bool] = None
    is_error_value: Optional[bool] = None
    is_in_table: Optional[bool] = None
    is_style_set: Optional[bool] = None
    html_string: Optional[str] = None
    style: Optional[LinkElement] = None
    worksheet: Optional[str] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.row is not None:
            result["Row"] = self.row
        if self.column is not None:
            result["Column"] = self.column
        if self.value is not None:
            result["Value"] = self.value
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.formula is not None:
            result["Formula"] = self.formula
        if self.is_formula is not None:
            result["IsFormula"] = self.is_formula
        if self.is_merged is not None:
            result["IsMerged"] = self.is_merged
        if self.is_array_header is not None:
            result["IsArrayHeader"] = self.is_array_header
        if self.is_in_array is not None:
            result["IsInArray"] = self.is_in_array
        if self.is_error_value is not None:
            result["IsErrorValue"] = self.is_error_value
        if self.is_in_table is not None:
            result["IsInTable"] = self.is_in_table
        if self.is_style_set is not None:
            result["IsStyleSet"] = self.is_style_set
        if self.html_string is not None:
            result["HtmlString"] = self.html_string
        if self.style is not None:
            result["Style"] = self.style.to_dict()
        if self.worksheet is not None:
            result["Worksheet"] = self.worksheet
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
