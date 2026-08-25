"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Chart:
    """Encapsulates the object that represents a single Excel chart."""
    auto_scaling: Optional[bool] = None
    back_wall: Optional[Walls] = None
    category_axis: Optional[Axis] = None
    chart_area: Optional[ChartArea] = None
    chart_data_table: Optional[ChartDataTable] = None
    chart_object: Optional[LinkElement] = None
    depth_percent: Optional[int] = None
    elevation: Optional[int] = None
    first_slice_angle: Optional[int] = None
    floor: Optional[Floor] = None
    gap_depth: Optional[int] = None
    gap_width: Optional[int] = None
    height_percent: Optional[int] = None
    hide_pivot_field_buttons: Optional[bool] = None
    is3_d: Optional[bool] = None
    is_rectangular_cornered: Optional[bool] = None
    legend: Optional[Legend] = None
    name: Optional[str] = None
    n_series: Optional[SeriesItems] = None
    page_setup: Optional[LinkElement] = None
    perspective: Optional[int] = None
    pivot_source: Optional[str] = None
    placement: Optional[str] = None
    plot_area: Optional[PlotArea] = None
    plot_empty_cells_type: Optional[str] = None
    plot_visible_cells: Optional[bool] = None
    print_size: Optional[str] = None
    right_angle_axes: Optional[bool] = None
    rotation_angle: Optional[int] = None
    second_category_axis: Optional[LinkElement] = None
    second_value_axis: Optional[LinkElement] = None
    series_axis: Optional[LinkElement] = None
    shapes: Optional[LinkElement] = None
    show_data_table: Optional[bool] = None
    show_legend: Optional[bool] = None
    side_wall: Optional[LinkElement] = None
    size_with_window: Optional[bool] = None
    style: Optional[int] = None
    title: Optional[LinkElement] = None
    type_: Optional[str] = None
    value_axis: Optional[Axis] = None
    walls: Optional[LinkElement] = None
    walls_and_gridlines2_d: Optional[bool] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.auto_scaling is not None:
            result["AutoScaling"] = self.auto_scaling
        if self.back_wall is not None:
            result["BackWall"] = self.back_wall.to_dict()
        if self.category_axis is not None:
            result["CategoryAxis"] = self.category_axis.to_dict()
        if self.chart_area is not None:
            result["ChartArea"] = self.chart_area.to_dict()
        if self.chart_data_table is not None:
            result["ChartDataTable"] = self.chart_data_table.to_dict()
        if self.chart_object is not None:
            result["ChartObject"] = self.chart_object.to_dict()
        if self.depth_percent is not None:
            result["DepthPercent"] = self.depth_percent
        if self.elevation is not None:
            result["Elevation"] = self.elevation
        if self.first_slice_angle is not None:
            result["FirstSliceAngle"] = self.first_slice_angle
        if self.floor is not None:
            result["Floor"] = self.floor.to_dict()
        if self.gap_depth is not None:
            result["GapDepth"] = self.gap_depth
        if self.gap_width is not None:
            result["GapWidth"] = self.gap_width
        if self.height_percent is not None:
            result["HeightPercent"] = self.height_percent
        if self.hide_pivot_field_buttons is not None:
            result["HidePivotFieldButtons"] = self.hide_pivot_field_buttons
        if self.is3_d is not None:
            result["Is3D"] = self.is3_d
        if self.is_rectangular_cornered is not None:
            result["IsRectangularCornered"] = self.is_rectangular_cornered
        if self.legend is not None:
            result["Legend"] = self.legend.to_dict()
        if self.name is not None:
            result["Name"] = self.name
        if self.n_series is not None:
            result["NSeries"] = self.n_series.to_dict()
        if self.page_setup is not None:
            result["PageSetup"] = self.page_setup.to_dict()
        if self.perspective is not None:
            result["Perspective"] = self.perspective
        if self.pivot_source is not None:
            result["PivotSource"] = self.pivot_source
        if self.placement is not None:
            result["Placement"] = self.placement
        if self.plot_area is not None:
            result["PlotArea"] = self.plot_area.to_dict()
        if self.plot_empty_cells_type is not None:
            result["PlotEmptyCellsType"] = self.plot_empty_cells_type
        if self.plot_visible_cells is not None:
            result["PlotVisibleCells"] = self.plot_visible_cells
        if self.print_size is not None:
            result["PrintSize"] = self.print_size
        if self.right_angle_axes is not None:
            result["RightAngleAxes"] = self.right_angle_axes
        if self.rotation_angle is not None:
            result["RotationAngle"] = self.rotation_angle
        if self.second_category_axis is not None:
            result["SecondCategoryAxis"] = self.second_category_axis.to_dict()
        if self.second_value_axis is not None:
            result["SecondValueAxis"] = self.second_value_axis.to_dict()
        if self.series_axis is not None:
            result["SeriesAxis"] = self.series_axis.to_dict()
        if self.shapes is not None:
            result["Shapes"] = self.shapes.to_dict()
        if self.show_data_table is not None:
            result["ShowDataTable"] = self.show_data_table
        if self.show_legend is not None:
            result["ShowLegend"] = self.show_legend
        if self.side_wall is not None:
            result["SideWall"] = self.side_wall.to_dict()
        if self.size_with_window is not None:
            result["SizeWithWindow"] = self.size_with_window
        if self.style is not None:
            result["Style"] = self.style
        if self.title is not None:
            result["Title"] = self.title.to_dict()
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.value_axis is not None:
            result["ValueAxis"] = self.value_axis.to_dict()
        if self.walls is not None:
            result["Walls"] = self.walls.to_dict()
        if self.walls_and_gridlines2_d is not None:
            result["WallsAndGridlines2D"] = self.walls_and_gridlines2_d
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
