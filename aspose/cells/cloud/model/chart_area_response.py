"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ChartAreaResponse:
    """Represents the ChartArea Response."""
    chart_area: Optional[ChartArea] = None
    code: Optional[int] = None
    status: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.chart_area is not None:
            result["ChartArea"] = self.chart_area.to_dict()
        if self.code is not None:
            result["Code"] = self.code
        if self.status is not None:
            result["Status"] = self.status
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
