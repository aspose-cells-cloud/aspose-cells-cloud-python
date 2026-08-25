"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataLabels:
    """Encapsulates a collection of all the DataLabel objects for the specified Series."""
    is_auto_text: Optional[bool] = None
    is_deleted: Optional[bool] = None
    linked_source: Optional[str] = None
    number: Optional[int] = None
    number_format: Optional[str] = None
    number_format_linked: Optional[bool] = None
    position: Optional[str] = None
    rotation_angle: Optional[int] = None
    separator: Optional[str] = None
    show_bubble_size: Optional[bool] = None
    show_category_name: Optional[bool] = None
    show_legend_key: Optional[bool] = None
    show_percentage: Optional[bool] = None
    show_series_name: Optional[bool] = None
    show_value: Optional[bool] = None
    text: Optional[str] = None
    text_direction: Optional[str] = None
    text_horizontal_alignment: Optional[str] = None
    text_vertical_alignment: Optional[str] = None
    area: Optional[Area] = None
    auto_scale_font: Optional[bool] = None
    background_mode: Optional[str] = None
    border: Optional[Line] = None
    font: Optional[Font] = None
    is_automatic_size: Optional[bool] = None
    is_inner_mode: Optional[bool] = None
    shadow: Optional[bool] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.is_auto_text is not None:
            result["IsAutoText"] = self.is_auto_text
        if self.is_deleted is not None:
            result["IsDeleted"] = self.is_deleted
        if self.linked_source is not None:
            result["LinkedSource"] = self.linked_source
        if self.number is not None:
            result["Number"] = self.number
        if self.number_format is not None:
            result["NumberFormat"] = self.number_format
        if self.number_format_linked is not None:
            result["NumberFormatLinked"] = self.number_format_linked
        if self.position is not None:
            result["Position"] = self.position
        if self.rotation_angle is not None:
            result["RotationAngle"] = self.rotation_angle
        if self.separator is not None:
            result["Separator"] = self.separator
        if self.show_bubble_size is not None:
            result["ShowBubbleSize"] = self.show_bubble_size
        if self.show_category_name is not None:
            result["ShowCategoryName"] = self.show_category_name
        if self.show_legend_key is not None:
            result["ShowLegendKey"] = self.show_legend_key
        if self.show_percentage is not None:
            result["ShowPercentage"] = self.show_percentage
        if self.show_series_name is not None:
            result["ShowSeriesName"] = self.show_series_name
        if self.show_value is not None:
            result["ShowValue"] = self.show_value
        if self.text is not None:
            result["Text"] = self.text
        if self.text_direction is not None:
            result["TextDirection"] = self.text_direction
        if self.text_horizontal_alignment is not None:
            result["TextHorizontalAlignment"] = self.text_horizontal_alignment
        if self.text_vertical_alignment is not None:
            result["TextVerticalAlignment"] = self.text_vertical_alignment
        if self.area is not None:
            result["Area"] = self.area.to_dict()
        if self.auto_scale_font is not None:
            result["AutoScaleFont"] = self.auto_scale_font
        if self.background_mode is not None:
            result["BackgroundMode"] = self.background_mode
        if self.border is not None:
            result["Border"] = self.border.to_dict()
        if self.font is not None:
            result["Font"] = self.font.to_dict()
        if self.is_automatic_size is not None:
            result["IsAutomaticSize"] = self.is_automatic_size
        if self.is_inner_mode is not None:
            result["IsInnerMode"] = self.is_inner_mode
        if self.shadow is not None:
            result["Shadow"] = self.shadow
        if self.width is not None:
            result["Width"] = self.width
        if self.height is not None:
            result["Height"] = self.height
        if self.x is not None:
            result["X"] = self.x
        if self.y is not None:
            result["Y"] = self.y
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
