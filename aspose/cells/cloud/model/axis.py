"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Axis:
    """Encapsulates the object that represents an axis of chart."""
    area: Optional[Area] = None
    axis_between_categories: Optional[bool] = None
    axis_line: Optional[Line] = None
    base_unit_scale: Optional[str] = None
    category_type: Optional[str] = None
    cross_at: Optional[float] = None
    cross_type: Optional[str] = None
    display_unit: Optional[str] = None
    display_unit_label: Optional[DisplayUnitLabel] = None
    has_multi_level_labels: Optional[bool] = None
    is_automatic_major_unit: Optional[bool] = None
    is_automatic_max_value: Optional[bool] = None
    is_automatic_minor_unit: Optional[bool] = None
    is_automatic_min_value: Optional[bool] = None
    is_display_unit_label_shown: Optional[bool] = None
    is_logarithmic: Optional[bool] = None
    is_plot_order_reversed: Optional[bool] = None
    is_visible: Optional[bool] = None
    log_base: Optional[float] = None
    major_grid_lines: Optional[Line] = None
    major_tick_mark: Optional[str] = None
    major_unit: Optional[float] = None
    major_unit_scale: Optional[str] = None
    max_value: Optional[float] = None
    minor_grid_lines: Optional[Line] = None
    minor_tick_mark: Optional[str] = None
    minor_unit: Optional[float] = None
    minor_unit_scale: Optional[str] = None
    min_value: Optional[float] = None
    tick_label_position: Optional[str] = None
    tick_labels: Optional[TickLabels] = None
    tick_label_spacing: Optional[int] = None
    tick_mark_spacing: Optional[int] = None
    title: Optional[Title] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.area is not None:
            result["Area"] = self.area.to_dict()
        if self.axis_between_categories is not None:
            result["AxisBetweenCategories"] = self.axis_between_categories
        if self.axis_line is not None:
            result["AxisLine"] = self.axis_line.to_dict()
        if self.base_unit_scale is not None:
            result["BaseUnitScale"] = self.base_unit_scale
        if self.category_type is not None:
            result["CategoryType"] = self.category_type
        if self.cross_at is not None:
            result["CrossAt"] = self.cross_at
        if self.cross_type is not None:
            result["CrossType"] = self.cross_type
        if self.display_unit is not None:
            result["DisplayUnit"] = self.display_unit
        if self.display_unit_label is not None:
            result["DisplayUnitLabel"] = self.display_unit_label.to_dict()
        if self.has_multi_level_labels is not None:
            result["HasMultiLevelLabels"] = self.has_multi_level_labels
        if self.is_automatic_major_unit is not None:
            result["IsAutomaticMajorUnit"] = self.is_automatic_major_unit
        if self.is_automatic_max_value is not None:
            result["IsAutomaticMaxValue"] = self.is_automatic_max_value
        if self.is_automatic_minor_unit is not None:
            result["IsAutomaticMinorUnit"] = self.is_automatic_minor_unit
        if self.is_automatic_min_value is not None:
            result["IsAutomaticMinValue"] = self.is_automatic_min_value
        if self.is_display_unit_label_shown is not None:
            result["IsDisplayUnitLabelShown"] = self.is_display_unit_label_shown
        if self.is_logarithmic is not None:
            result["IsLogarithmic"] = self.is_logarithmic
        if self.is_plot_order_reversed is not None:
            result["IsPlotOrderReversed"] = self.is_plot_order_reversed
        if self.is_visible is not None:
            result["IsVisible"] = self.is_visible
        if self.log_base is not None:
            result["LogBase"] = self.log_base
        if self.major_grid_lines is not None:
            result["MajorGridLines"] = self.major_grid_lines.to_dict()
        if self.major_tick_mark is not None:
            result["MajorTickMark"] = self.major_tick_mark
        if self.major_unit is not None:
            result["MajorUnit"] = self.major_unit
        if self.major_unit_scale is not None:
            result["MajorUnitScale"] = self.major_unit_scale
        if self.max_value is not None:
            result["MaxValue"] = self.max_value
        if self.minor_grid_lines is not None:
            result["MinorGridLines"] = self.minor_grid_lines.to_dict()
        if self.minor_tick_mark is not None:
            result["MinorTickMark"] = self.minor_tick_mark
        if self.minor_unit is not None:
            result["MinorUnit"] = self.minor_unit
        if self.minor_unit_scale is not None:
            result["MinorUnitScale"] = self.minor_unit_scale
        if self.min_value is not None:
            result["MinValue"] = self.min_value
        if self.tick_label_position is not None:
            result["TickLabelPosition"] = self.tick_label_position
        if self.tick_labels is not None:
            result["TickLabels"] = self.tick_labels.to_dict()
        if self.tick_label_spacing is not None:
            result["TickLabelSpacing"] = self.tick_label_spacing
        if self.tick_mark_spacing is not None:
            result["TickMarkSpacing"] = self.tick_mark_spacing
        if self.title is not None:
            result["Title"] = self.title.to_dict()
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
