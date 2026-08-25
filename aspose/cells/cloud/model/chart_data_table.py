"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ChartDataTable:
    """Represents a chart data table."""
    auto_scale_font: Optional[bool] = None
    background_mode: Optional[str] = None
    border: Optional[Line] = None
    font: Optional[Font] = None
    has_border_horizontal: Optional[bool] = None
    has_border_outline: Optional[bool] = None
    has_border_vertical: Optional[bool] = None
    show_legend_key: Optional[bool] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.auto_scale_font is not None:
            result["AutoScaleFont"] = self.auto_scale_font
        if self.background_mode is not None:
            result["BackgroundMode"] = self.background_mode
        if self.border is not None:
            result["Border"] = self.border.to_dict()
        if self.font is not None:
            result["Font"] = self.font.to_dict()
        if self.has_border_horizontal is not None:
            result["HasBorderHorizontal"] = self.has_border_horizontal
        if self.has_border_outline is not None:
            result["HasBorderOutline"] = self.has_border_outline
        if self.has_border_vertical is not None:
            result["HasBorderVertical"] = self.has_border_vertical
        if self.show_legend_key is not None:
            result["ShowLegendKey"] = self.show_legend_key
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
