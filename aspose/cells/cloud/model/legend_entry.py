"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class LegendEntry:
    """Represents a legend entry in a chart legend."""
    auto_scale_font: Optional[bool] = None
    background_mode: Optional[str] = None
    font: Optional[Font] = None
    is_deleted: Optional[bool] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.auto_scale_font is not None:
            result["AutoScaleFont"] = self.auto_scale_font
        if self.background_mode is not None:
            result["BackgroundMode"] = self.background_mode
        if self.font is not None:
            result["Font"] = self.font.to_dict()
        if self.is_deleted is not None:
            result["IsDeleted"] = self.is_deleted
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
