"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Validation:
    """Represents data validation.settings."""
    alert_style: Optional[str] = None
    area_list: Optional[List[CellArea]] = None
    error_message: Optional[str] = None
    error_title: Optional[str] = None
    formula1: Optional[str] = None
    formula2: Optional[str] = None
    ignore_blank: Optional[bool] = None
    in_cell_drop_down: Optional[bool] = None
    input_message: Optional[str] = None
    input_title: Optional[str] = None
    operator: Optional[str] = None
    show_error: Optional[bool] = None
    show_input: Optional[bool] = None
    type_: Optional[str] = None
    value1: Optional[str] = None
    value2: Optional[str] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.alert_style is not None:
            result["AlertStyle"] = self.alert_style
        if self.area_list is not None:
            result["AreaList"] = [x.to_dict() for x in self.area_list]
        if self.error_message is not None:
            result["ErrorMessage"] = self.error_message
        if self.error_title is not None:
            result["ErrorTitle"] = self.error_title
        if self.formula1 is not None:
            result["Formula1"] = self.formula1
        if self.formula2 is not None:
            result["Formula2"] = self.formula2
        if self.ignore_blank is not None:
            result["IgnoreBlank"] = self.ignore_blank
        if self.in_cell_drop_down is not None:
            result["InCellDropDown"] = self.in_cell_drop_down
        if self.input_message is not None:
            result["InputMessage"] = self.input_message
        if self.input_title is not None:
            result["InputTitle"] = self.input_title
        if self.operator is not None:
            result["Operator"] = self.operator
        if self.show_error is not None:
            result["ShowError"] = self.show_error
        if self.show_input is not None:
            result["ShowInput"] = self.show_input
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.value1 is not None:
            result["Value1"] = self.value1
        if self.value2 is not None:
            result["Value2"] = self.value2
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
