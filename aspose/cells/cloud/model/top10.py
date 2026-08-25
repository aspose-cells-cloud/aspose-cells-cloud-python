"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Top10:
    """Describe the Top10 conditional formatting rule. This conditional formatting rule highlights cells whose values fall in the top N or bottom N bracket, as specified."""
    is_bottom: Optional[bool] = None
    is_percent: Optional[bool] = None
    rank: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.is_bottom is not None:
            result["IsBottom"] = self.is_bottom
        if self.is_percent is not None:
            result["IsPercent"] = self.is_percent
        if self.rank is not None:
            result["Rank"] = self.rank
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
