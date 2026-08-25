"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ChartPoint:
    """Represents a single point in a series in a chart."""
    area: Optional[Area] = None
    border: Optional[Line] = None
    data_labels: Optional[DataLabels] = None
    explosion: Optional[int] = None
    marker: Optional[Marker] = None
    shadow: Optional[bool] = None
    x_value: Optional[Any] = None
    y_value: Optional[Any] = None
    is_in_secondary_plot: Optional[bool] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.area is not None:
            result["Area"] = self.area.to_dict()
        if self.border is not None:
            result["Border"] = self.border.to_dict()
        if self.data_labels is not None:
            result["DataLabels"] = self.data_labels.to_dict()
        if self.explosion is not None:
            result["Explosion"] = self.explosion
        if self.marker is not None:
            result["Marker"] = self.marker.to_dict()
        if self.shadow is not None:
            result["Shadow"] = self.shadow
        if self.x_value is not None:
            result["XValue"] = self.x_value
        if self.y_value is not None:
            result["YValue"] = self.y_value
        if self.is_in_secondary_plot is not None:
            result["IsInSecondaryPlot"] = self.is_in_secondary_plot
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
