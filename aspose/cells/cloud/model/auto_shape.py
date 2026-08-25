"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AutoShape:
    """Represents an AutoShape."""
    name: Optional[str] = None
    mso_drawing_type: Optional[str] = None
    auto_shape_type: Optional[str] = None
    placement: Optional[str] = None
    upper_left_row: Optional[int] = None
    top: Optional[int] = None
    upper_left_column: Optional[int] = None
    left: Optional[int] = None
    lower_right_row: Optional[int] = None
    bottom: Optional[int] = None
    lower_right_column: Optional[int] = None
    right: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    x: Optional[int] = None
    y: Optional[int] = None
    rotation_angle: Optional[float] = None
    html_text: Optional[str] = None
    text: Optional[str] = None
    alternative_text: Optional[str] = None
    text_horizontal_alignment: Optional[str] = None
    text_horizontal_overflow: Optional[str] = None
    text_orientation_type: Optional[str] = None
    text_vertical_alignment: Optional[str] = None
    text_vertical_overflow: Optional[str] = None
    is_group: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_lock_aspect_ratio: Optional[bool] = None
    is_locked: Optional[bool] = None
    is_printable: Optional[bool] = None
    is_text_wrapped: Optional[bool] = None
    is_word_art: Optional[bool] = None
    linked_cell: Optional[str] = None
    z_order_position: Optional[int] = None
    font: Optional[Font] = None
    hyperlink: Optional[str] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.mso_drawing_type is not None:
            result["MsoDrawingType"] = self.mso_drawing_type
        if self.auto_shape_type is not None:
            result["AutoShapeType"] = self.auto_shape_type
        if self.placement is not None:
            result["Placement"] = self.placement
        if self.upper_left_row is not None:
            result["UpperLeftRow"] = self.upper_left_row
        if self.top is not None:
            result["Top"] = self.top
        if self.upper_left_column is not None:
            result["UpperLeftColumn"] = self.upper_left_column
        if self.left is not None:
            result["Left"] = self.left
        if self.lower_right_row is not None:
            result["LowerRightRow"] = self.lower_right_row
        if self.bottom is not None:
            result["Bottom"] = self.bottom
        if self.lower_right_column is not None:
            result["LowerRightColumn"] = self.lower_right_column
        if self.right is not None:
            result["Right"] = self.right
        if self.width is not None:
            result["Width"] = self.width
        if self.height is not None:
            result["Height"] = self.height
        if self.x is not None:
            result["X"] = self.x
        if self.y is not None:
            result["Y"] = self.y
        if self.rotation_angle is not None:
            result["RotationAngle"] = self.rotation_angle
        if self.html_text is not None:
            result["HtmlText"] = self.html_text
        if self.text is not None:
            result["Text"] = self.text
        if self.alternative_text is not None:
            result["AlternativeText"] = self.alternative_text
        if self.text_horizontal_alignment is not None:
            result["TextHorizontalAlignment"] = self.text_horizontal_alignment
        if self.text_horizontal_overflow is not None:
            result["TextHorizontalOverflow"] = self.text_horizontal_overflow
        if self.text_orientation_type is not None:
            result["TextOrientationType"] = self.text_orientation_type
        if self.text_vertical_alignment is not None:
            result["TextVerticalAlignment"] = self.text_vertical_alignment
        if self.text_vertical_overflow is not None:
            result["TextVerticalOverflow"] = self.text_vertical_overflow
        if self.is_group is not None:
            result["IsGroup"] = self.is_group
        if self.is_hidden is not None:
            result["IsHidden"] = self.is_hidden
        if self.is_lock_aspect_ratio is not None:
            result["IsLockAspectRatio"] = self.is_lock_aspect_ratio
        if self.is_locked is not None:
            result["IsLocked"] = self.is_locked
        if self.is_printable is not None:
            result["IsPrintable"] = self.is_printable
        if self.is_text_wrapped is not None:
            result["IsTextWrapped"] = self.is_text_wrapped
        if self.is_word_art is not None:
            result["IsWordArt"] = self.is_word_art
        if self.linked_cell is not None:
            result["LinkedCell"] = self.linked_cell
        if self.z_order_position is not None:
            result["ZOrderPosition"] = self.z_order_position
        if self.font is not None:
            result["Font"] = self.font.to_dict()
        if self.hyperlink is not None:
            result["Hyperlink"] = self.hyperlink
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
