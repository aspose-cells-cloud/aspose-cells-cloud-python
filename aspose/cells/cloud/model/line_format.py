"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class LineFormat:
    """Represents all setting of the line."""
    begin_arrowhead_length: Optional[str] = None
    begin_arrowhead_style: Optional[str] = None
    begin_arrowhead_width: Optional[str] = None
    cap_type: Optional[str] = None
    compound_type: Optional[str] = None
    dash_style: Optional[str] = None
    end_arrowhead_length: Optional[str] = None
    end_arrowhead_style: Optional[str] = None
    end_arrowhead_width: Optional[str] = None
    join_type: Optional[str] = None
    weight: Optional[float] = None
    type_: Optional[str] = None
    solid_fill: Optional[SolidFill] = None
    pattern_fill: Optional[PatternFill] = None
    texture_fill: Optional[TextureFill] = None
    gradient_fill: Optional[GradientFill] = None
    image_data: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.begin_arrowhead_length is not None:
            result["BeginArrowheadLength"] = self.begin_arrowhead_length
        if self.begin_arrowhead_style is not None:
            result["BeginArrowheadStyle"] = self.begin_arrowhead_style
        if self.begin_arrowhead_width is not None:
            result["BeginArrowheadWidth"] = self.begin_arrowhead_width
        if self.cap_type is not None:
            result["CapType"] = self.cap_type
        if self.compound_type is not None:
            result["CompoundType"] = self.compound_type
        if self.dash_style is not None:
            result["DashStyle"] = self.dash_style
        if self.end_arrowhead_length is not None:
            result["EndArrowheadLength"] = self.end_arrowhead_length
        if self.end_arrowhead_style is not None:
            result["EndArrowheadStyle"] = self.end_arrowhead_style
        if self.end_arrowhead_width is not None:
            result["EndArrowheadWidth"] = self.end_arrowhead_width
        if self.join_type is not None:
            result["JoinType"] = self.join_type
        if self.weight is not None:
            result["Weight"] = self.weight
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.solid_fill is not None:
            result["SolidFill"] = self.solid_fill.to_dict()
        if self.pattern_fill is not None:
            result["PatternFill"] = self.pattern_fill.to_dict()
        if self.texture_fill is not None:
            result["TextureFill"] = self.texture_fill.to_dict()
        if self.gradient_fill is not None:
            result["GradientFill"] = self.gradient_fill.to_dict()
        if self.image_data is not None:
            result["ImageData"] = self.image_data
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
