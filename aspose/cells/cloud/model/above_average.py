"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AboveAverage:
    """Describe the AboveAverage conditional formatting rule. This conditional formatting rule highlights cells that are above or below the average for all values in the range."""
    is_above_average: Optional[bool] = None
    is_equal_average: Optional[bool] = None
    std_dev: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.is_above_average is not None:
            result["IsAboveAverage"] = self.is_above_average
        if self.is_equal_average is not None:
            result["IsEqualAverage"] = self.is_equal_average
        if self.std_dev is not None:
            result["StdDev"] = self.std_dev
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
