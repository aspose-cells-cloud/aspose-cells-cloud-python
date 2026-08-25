"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ChartPoints:
    """Represents a collection that contains all the points in one series."""
    chart_point_list: Optional[List[ChartPoint]] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.chart_point_list is not None:
            result["ChartPointList"] = [x.to_dict() for x in self.chart_point_list]
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
