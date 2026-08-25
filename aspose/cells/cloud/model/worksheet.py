"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Worksheet:
    """Encapsulates the object that represents a single worksheet."""
    links: Optional[List[Link]] = None
    display_right_to_left: Optional[bool] = None
    display_zeros: Optional[bool] = None
    first_visible_column: Optional[int] = None
    first_visible_row: Optional[int] = None
    name: Optional[str] = None
    index: Optional[int] = None
    is_gridlines_visible: Optional[bool] = None
    is_outline_shown: Optional[bool] = None
    is_page_break_preview: Optional[bool] = None
    is_visible: Optional[bool] = None
    is_protected: Optional[bool] = None
    is_row_column_headers_visible: Optional[bool] = None
    is_ruler_visible: Optional[bool] = None
    is_selected: Optional[bool] = None
    tab_color: Optional[Color] = None
    transition_entry: Optional[bool] = None
    transition_evaluation: Optional[bool] = None
    type_: Optional[str] = None
    view_type: Optional[str] = None
    visibility_type: Optional[str] = None
    zoom: Optional[int] = None
    cells: Optional[LinkElement] = None
    charts: Optional[LinkElement] = None
    auto_shapes: Optional[LinkElement] = None
    ole_objects: Optional[LinkElement] = None
    comments: Optional[LinkElement] = None
    pictures: Optional[LinkElement] = None
    merged_cells: Optional[LinkElement] = None
    validations: Optional[LinkElement] = None
    conditional_formattings: Optional[LinkElement] = None
    hyperlinks: Optional[LinkElement] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.links is not None:
            result["Links"] = [x.to_dict() for x in self.links]
        if self.display_right_to_left is not None:
            result["DisplayRightToLeft"] = self.display_right_to_left
        if self.display_zeros is not None:
            result["DisplayZeros"] = self.display_zeros
        if self.first_visible_column is not None:
            result["FirstVisibleColumn"] = self.first_visible_column
        if self.first_visible_row is not None:
            result["FirstVisibleRow"] = self.first_visible_row
        if self.name is not None:
            result["Name"] = self.name
        if self.index is not None:
            result["Index"] = self.index
        if self.is_gridlines_visible is not None:
            result["IsGridlinesVisible"] = self.is_gridlines_visible
        if self.is_outline_shown is not None:
            result["IsOutlineShown"] = self.is_outline_shown
        if self.is_page_break_preview is not None:
            result["IsPageBreakPreview"] = self.is_page_break_preview
        if self.is_visible is not None:
            result["IsVisible"] = self.is_visible
        if self.is_protected is not None:
            result["IsProtected"] = self.is_protected
        if self.is_row_column_headers_visible is not None:
            result["IsRowColumnHeadersVisible"] = self.is_row_column_headers_visible
        if self.is_ruler_visible is not None:
            result["IsRulerVisible"] = self.is_ruler_visible
        if self.is_selected is not None:
            result["IsSelected"] = self.is_selected
        if self.tab_color is not None:
            result["TabColor"] = self.tab_color.to_dict()
        if self.transition_entry is not None:
            result["TransitionEntry"] = self.transition_entry
        if self.transition_evaluation is not None:
            result["TransitionEvaluation"] = self.transition_evaluation
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.view_type is not None:
            result["ViewType"] = self.view_type
        if self.visibility_type is not None:
            result["VisibilityType"] = self.visibility_type
        if self.zoom is not None:
            result["Zoom"] = self.zoom
        if self.cells is not None:
            result["Cells"] = self.cells.to_dict()
        if self.charts is not None:
            result["Charts"] = self.charts.to_dict()
        if self.auto_shapes is not None:
            result["AutoShapes"] = self.auto_shapes.to_dict()
        if self.ole_objects is not None:
            result["OleObjects"] = self.ole_objects.to_dict()
        if self.comments is not None:
            result["Comments"] = self.comments.to_dict()
        if self.pictures is not None:
            result["Pictures"] = self.pictures.to_dict()
        if self.merged_cells is not None:
            result["MergedCells"] = self.merged_cells.to_dict()
        if self.validations is not None:
            result["Validations"] = self.validations.to_dict()
        if self.conditional_formattings is not None:
            result["ConditionalFormattings"] = self.conditional_formattings.to_dict()
        if self.hyperlinks is not None:
            result["Hyperlinks"] = self.hyperlinks.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
