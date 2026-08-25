"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class StyleFormatCondition:
    """Represents style format condition."""
    priority: Optional[int] = None
    type_: Optional[str] = None
    stop_if_true: Optional[bool] = None
    above_average: Optional[AboveAverage] = None
    color_scale: Optional[ColorScale] = None
    data_bar: Optional[DataBar] = None
    formula1: Optional[str] = None
    formula2: Optional[str] = None
    icon_set: Optional[IconSet] = None
    operator: Optional[str] = None
    style: Optional[Style] = None
    text: Optional[str] = None
    time_period: Optional[str] = None
    top10: Optional[Top10] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.priority is not None:
            result["Priority"] = self.priority
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.stop_if_true is not None:
            result["StopIfTrue"] = self.stop_if_true
        if self.above_average is not None:
            result["AboveAverage"] = self.above_average.to_dict()
        if self.color_scale is not None:
            result["ColorScale"] = self.color_scale.to_dict()
        if self.data_bar is not None:
            result["DataBar"] = self.data_bar.to_dict()
        if self.formula1 is not None:
            result["Formula1"] = self.formula1
        if self.formula2 is not None:
            result["Formula2"] = self.formula2
        if self.icon_set is not None:
            result["IconSet"] = self.icon_set.to_dict()
        if self.operator is not None:
            result["Operator"] = self.operator
        if self.style is not None:
            result["Style"] = self.style.to_dict()
        if self.text is not None:
            result["Text"] = self.text
        if self.time_period is not None:
            result["TimePeriod"] = self.time_period
        if self.top10 is not None:
            result["Top10"] = self.top10.to_dict()
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
