"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Line:
    """Encapsulates the object that represents the line format."""
    begin_arrow_length: Optional[str] = None
    begin_arrow_width: Optional[str] = None
    begin_type: Optional[str] = None
    cap_type: Optional[str] = None
    color: Optional[Color] = None
    compound_type: Optional[str] = None
    dash_type: Optional[str] = None
    end_arrow_length: Optional[str] = None
    end_arrow_width: Optional[str] = None
    end_type: Optional[str] = None
    gradient_fill: Optional[GradientFill] = None
    is_auto: Optional[bool] = None
    is_automatic_color: Optional[bool] = None
    is_visible: Optional[bool] = None
    join_type: Optional[str] = None
    style: Optional[str] = None
    transparency: Optional[float] = None
    weight: Optional[str] = None
    weight_pt: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.begin_arrow_length is not None:
            result["BeginArrowLength"] = self.begin_arrow_length
        if self.begin_arrow_width is not None:
            result["BeginArrowWidth"] = self.begin_arrow_width
        if self.begin_type is not None:
            result["BeginType"] = self.begin_type
        if self.cap_type is not None:
            result["CapType"] = self.cap_type
        if self.color is not None:
            result["Color"] = self.color.to_dict()
        if self.compound_type is not None:
            result["CompoundType"] = self.compound_type
        if self.dash_type is not None:
            result["DashType"] = self.dash_type
        if self.end_arrow_length is not None:
            result["EndArrowLength"] = self.end_arrow_length
        if self.end_arrow_width is not None:
            result["EndArrowWidth"] = self.end_arrow_width
        if self.end_type is not None:
            result["EndType"] = self.end_type
        if self.gradient_fill is not None:
            result["GradientFill"] = self.gradient_fill.to_dict()
        if self.is_auto is not None:
            result["IsAuto"] = self.is_auto
        if self.is_automatic_color is not None:
            result["IsAutomaticColor"] = self.is_automatic_color
        if self.is_visible is not None:
            result["IsVisible"] = self.is_visible
        if self.join_type is not None:
            result["JoinType"] = self.join_type
        if self.style is not None:
            result["Style"] = self.style
        if self.transparency is not None:
            result["Transparency"] = self.transparency
        if self.weight is not None:
            result["Weight"] = self.weight
        if self.weight_pt is not None:
            result["WeightPt"] = self.weight_pt
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
