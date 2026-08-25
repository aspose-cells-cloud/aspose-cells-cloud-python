"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Comment:
    """Encapsulates the object that represents a cell comment."""
    cell_name: Optional[str] = None
    author: Optional[str] = None
    html_note: Optional[str] = None
    note: Optional[str] = None
    auto_size: Optional[bool] = None
    is_visible: Optional[bool] = None
    width: Optional[int] = None
    height: Optional[int] = None
    text_horizontal_alignment: Optional[str] = None
    text_orientation_type: Optional[str] = None
    text_vertical_alignment: Optional[str] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.cell_name is not None:
            result["CellName"] = self.cell_name
        if self.author is not None:
            result["Author"] = self.author
        if self.html_note is not None:
            result["HtmlNote"] = self.html_note
        if self.note is not None:
            result["Note"] = self.note
        if self.auto_size is not None:
            result["AutoSize"] = self.auto_size
        if self.is_visible is not None:
            result["IsVisible"] = self.is_visible
        if self.width is not None:
            result["Width"] = self.width
        if self.height is not None:
            result["Height"] = self.height
        if self.text_horizontal_alignment is not None:
            result["TextHorizontalAlignment"] = self.text_horizontal_alignment
        if self.text_orientation_type is not None:
            result["TextOrientationType"] = self.text_orientation_type
        if self.text_vertical_alignment is not None:
            result["TextVerticalAlignment"] = self.text_vertical_alignment
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
