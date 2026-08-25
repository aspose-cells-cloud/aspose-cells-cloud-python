"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Series:
    """Encapsulates the object that represents a single data series in a chart."""
    area: Optional[Area] = None
    bar3_d_shape_type: Optional[str] = None
    border: Optional[Line] = None
    bubble_scale: Optional[int] = None
    bubble_sizes: Optional[str] = None
    count_of_data_values: Optional[int] = None
    data_labels: Optional[DataLabels] = None
    display_name: Optional[str] = None
    doughnut_hole_size: Optional[int] = None
    down_bars: Optional[DropBars] = None
    drop_lines: Optional[Line] = None
    explosion: Optional[int] = None
    first_slice_angle: Optional[int] = None
    gap_width: Optional[int] = None
    has3_d_effect: Optional[bool] = None
    has_drop_lines: Optional[bool] = None
    has_hi_lo_lines: Optional[bool] = None
    has_leader_lines: Optional[bool] = None
    has_radar_axis_labels: Optional[bool] = None
    has_series_lines: Optional[bool] = None
    has_up_down_bars: Optional[bool] = None
    hi_lo_lines: Optional[Line] = None
    is_auto_split: Optional[bool] = None
    is_color_varied: Optional[bool] = None
    leader_lines: Optional[Line] = None
    legend_entry: Optional[LegendEntry] = None
    marker: Optional[Marker] = None
    name: Optional[str] = None
    overlap: Optional[int] = None
    plot_on_second_axis: Optional[bool] = None
    points: Optional[LinkElement] = None
    second_plot_size: Optional[int] = None
    series_lines: Optional[Line] = None
    shadow: Optional[bool] = None
    show_negative_bubbles: Optional[bool] = None
    size_represents: Optional[str] = None
    smooth: Optional[bool] = None
    split_type: Optional[str] = None
    split_value: Optional[float] = None
    trend_lines: Optional[Trendlines] = None
    type_: Optional[str] = None
    up_bars: Optional[DropBars] = None
    values: Optional[str] = None
    x_error_bar: Optional[ErrorBar] = None
    x_values: Optional[str] = None
    y_error_bar: Optional[ErrorBar] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.area is not None:
            result["Area"] = self.area.to_dict()
        if self.bar3_d_shape_type is not None:
            result["Bar3DShapeType"] = self.bar3_d_shape_type
        if self.border is not None:
            result["Border"] = self.border.to_dict()
        if self.bubble_scale is not None:
            result["BubbleScale"] = self.bubble_scale
        if self.bubble_sizes is not None:
            result["BubbleSizes"] = self.bubble_sizes
        if self.count_of_data_values is not None:
            result["CountOfDataValues"] = self.count_of_data_values
        if self.data_labels is not None:
            result["DataLabels"] = self.data_labels.to_dict()
        if self.display_name is not None:
            result["DisplayName"] = self.display_name
        if self.doughnut_hole_size is not None:
            result["DoughnutHoleSize"] = self.doughnut_hole_size
        if self.down_bars is not None:
            result["DownBars"] = self.down_bars.to_dict()
        if self.drop_lines is not None:
            result["DropLines"] = self.drop_lines.to_dict()
        if self.explosion is not None:
            result["Explosion"] = self.explosion
        if self.first_slice_angle is not None:
            result["FirstSliceAngle"] = self.first_slice_angle
        if self.gap_width is not None:
            result["GapWidth"] = self.gap_width
        if self.has3_d_effect is not None:
            result["Has3DEffect"] = self.has3_d_effect
        if self.has_drop_lines is not None:
            result["HasDropLines"] = self.has_drop_lines
        if self.has_hi_lo_lines is not None:
            result["HasHiLoLines"] = self.has_hi_lo_lines
        if self.has_leader_lines is not None:
            result["HasLeaderLines"] = self.has_leader_lines
        if self.has_radar_axis_labels is not None:
            result["HasRadarAxisLabels"] = self.has_radar_axis_labels
        if self.has_series_lines is not None:
            result["HasSeriesLines"] = self.has_series_lines
        if self.has_up_down_bars is not None:
            result["HasUpDownBars"] = self.has_up_down_bars
        if self.hi_lo_lines is not None:
            result["HiLoLines"] = self.hi_lo_lines.to_dict()
        if self.is_auto_split is not None:
            result["IsAutoSplit"] = self.is_auto_split
        if self.is_color_varied is not None:
            result["IsColorVaried"] = self.is_color_varied
        if self.leader_lines is not None:
            result["LeaderLines"] = self.leader_lines.to_dict()
        if self.legend_entry is not None:
            result["LegendEntry"] = self.legend_entry.to_dict()
        if self.marker is not None:
            result["Marker"] = self.marker.to_dict()
        if self.name is not None:
            result["Name"] = self.name
        if self.overlap is not None:
            result["Overlap"] = self.overlap
        if self.plot_on_second_axis is not None:
            result["PlotOnSecondAxis"] = self.plot_on_second_axis
        if self.points is not None:
            result["Points"] = self.points.to_dict()
        if self.second_plot_size is not None:
            result["SecondPlotSize"] = self.second_plot_size
        if self.series_lines is not None:
            result["SeriesLines"] = self.series_lines.to_dict()
        if self.shadow is not None:
            result["Shadow"] = self.shadow
        if self.show_negative_bubbles is not None:
            result["ShowNegativeBubbles"] = self.show_negative_bubbles
        if self.size_represents is not None:
            result["SizeRepresents"] = self.size_represents
        if self.smooth is not None:
            result["Smooth"] = self.smooth
        if self.split_type is not None:
            result["SplitType"] = self.split_type
        if self.split_value is not None:
            result["SplitValue"] = self.split_value
        if self.trend_lines is not None:
            result["TrendLines"] = self.trend_lines.to_dict()
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.up_bars is not None:
            result["UpBars"] = self.up_bars.to_dict()
        if self.values is not None:
            result["Values"] = self.values
        if self.x_error_bar is not None:
            result["XErrorBar"] = self.x_error_bar.to_dict()
        if self.x_values is not None:
            result["XValues"] = self.x_values
        if self.y_error_bar is not None:
            result["YErrorBar"] = self.y_error_bar.to_dict()
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
