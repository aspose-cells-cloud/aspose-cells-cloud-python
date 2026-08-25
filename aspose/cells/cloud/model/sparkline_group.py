"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SparklineGroup:
    """is organized into sparkline group. A SparklineGroup contains a variable number of sparkline items.             A sparkline group specifies the type, display settings and axis settings for the sparklines."""
    display_hidden: Optional[bool] = None
    first_point_color: Optional[CellsColor] = None
    high_point_color: Optional[CellsColor] = None
    horizontal_axis_color: Optional[CellsColor] = None
    horizontal_axis_date_range: Optional[str] = None
    last_point_color: Optional[CellsColor] = None
    line_weight: Optional[float] = None
    low_point_color: Optional[CellsColor] = None
    markers_color: Optional[CellsColor] = None
    negative_points_color: Optional[CellsColor] = None
    plot_empty_cells_type: Optional[str] = None
    plot_right_to_left: Optional[bool] = None
    preset_style: Optional[str] = None
    series_color: Optional[CellsColor] = None
    show_first_point: Optional[bool] = None
    show_high_point: Optional[bool] = None
    show_horizontal_axis: Optional[bool] = None
    show_last_point: Optional[bool] = None
    show_low_point: Optional[bool] = None
    show_markers: Optional[bool] = None
    show_negative_points: Optional[bool] = None
    sparkline_collection: Optional[List[Sparkline]] = None
    type_: Optional[str] = None
    vertical_axis_max_value: Optional[float] = None
    vertical_axis_max_value_type: Optional[str] = None
    vertical_axis_min_value: Optional[float] = None
    vertical_axis_min_value_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.display_hidden is not None:
            result["DisplayHidden"] = self.display_hidden
        if self.first_point_color is not None:
            result["FirstPointColor"] = self.first_point_color.to_dict()
        if self.high_point_color is not None:
            result["HighPointColor"] = self.high_point_color.to_dict()
        if self.horizontal_axis_color is not None:
            result["HorizontalAxisColor"] = self.horizontal_axis_color.to_dict()
        if self.horizontal_axis_date_range is not None:
            result["HorizontalAxisDateRange"] = self.horizontal_axis_date_range
        if self.last_point_color is not None:
            result["LastPointColor"] = self.last_point_color.to_dict()
        if self.line_weight is not None:
            result["LineWeight"] = self.line_weight
        if self.low_point_color is not None:
            result["LowPointColor"] = self.low_point_color.to_dict()
        if self.markers_color is not None:
            result["MarkersColor"] = self.markers_color.to_dict()
        if self.negative_points_color is not None:
            result["NegativePointsColor"] = self.negative_points_color.to_dict()
        if self.plot_empty_cells_type is not None:
            result["PlotEmptyCellsType"] = self.plot_empty_cells_type
        if self.plot_right_to_left is not None:
            result["PlotRightToLeft"] = self.plot_right_to_left
        if self.preset_style is not None:
            result["PresetStyle"] = self.preset_style
        if self.series_color is not None:
            result["SeriesColor"] = self.series_color.to_dict()
        if self.show_first_point is not None:
            result["ShowFirstPoint"] = self.show_first_point
        if self.show_high_point is not None:
            result["ShowHighPoint"] = self.show_high_point
        if self.show_horizontal_axis is not None:
            result["ShowHorizontalAxis"] = self.show_horizontal_axis
        if self.show_last_point is not None:
            result["ShowLastPoint"] = self.show_last_point
        if self.show_low_point is not None:
            result["ShowLowPoint"] = self.show_low_point
        if self.show_markers is not None:
            result["ShowMarkers"] = self.show_markers
        if self.show_negative_points is not None:
            result["ShowNegativePoints"] = self.show_negative_points
        if self.sparkline_collection is not None:
            result["SparklineCollection"] = [x.to_dict() for x in self.sparkline_collection]
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.vertical_axis_max_value is not None:
            result["VerticalAxisMaxValue"] = self.vertical_axis_max_value
        if self.vertical_axis_max_value_type is not None:
            result["VerticalAxisMaxValueType"] = self.vertical_axis_max_value_type
        if self.vertical_axis_min_value is not None:
            result["VerticalAxisMinValue"] = self.vertical_axis_min_value
        if self.vertical_axis_min_value_type is not None:
            result["VerticalAxisMinValueType"] = self.vertical_axis_min_value_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
