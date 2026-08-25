"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Marker:
    """Represents the marker in a line chart, scatter chart, or radar chart."""
    border: Optional[Line] = None
    area: Optional[Area] = None
    marker_size: Optional[int] = None
    marker_style: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.border is not None:
            result["Border"] = self.border.to_dict()
        if self.area is not None:
            result["Area"] = self.area.to_dict()
        if self.marker_size is not None:
            result["MarkerSize"] = self.marker_size
        if self.marker_style is not None:
            result["MarkerStyle"] = self.marker_style
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
