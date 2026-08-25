"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataBar:
    """Describe the DataBar conditional formatting rule. This conditional formatting rule displays a gradated data bar in the range of cells."""
    axis_color: Optional[Color] = None
    axis_position: Optional[str] = None
    bar_border: Optional[DataBarBorder] = None
    bar_fill_type: Optional[str] = None
    color: Optional[Color] = None
    direction: Optional[str] = None
    max_cfvo: Optional[ConditionalFormattingValue] = None
    max_length: Optional[int] = None
    min_cfvo: Optional[ConditionalFormattingValue] = None
    min_length: Optional[int] = None
    negative_bar_format: Optional[NegativeBarFormat] = None
    show_value: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.axis_color is not None:
            result["AxisColor"] = self.axis_color.to_dict()
        if self.axis_position is not None:
            result["AxisPosition"] = self.axis_position
        if self.bar_border is not None:
            result["BarBorder"] = self.bar_border.to_dict()
        if self.bar_fill_type is not None:
            result["BarFillType"] = self.bar_fill_type
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.direction is not None:
            result["Direction"] = self.direction
        if self.max_cfvo is not None:
            result["MaxCfvo"] = self.max_cfvo.to_dict()
        if self.max_length is not None:
            result["MaxLength"] = self.max_length
        if self.min_cfvo is not None:
            result["MinCfvo"] = self.min_cfvo.to_dict()
        if self.min_length is not None:
            result["MinLength"] = self.min_length
        if self.negative_bar_format is not None:
            result["NegativeBarFormat"] = self.negative_bar_format.to_dict()
        if self.show_value is not None:
            result["ShowValue"] = self.show_value
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
