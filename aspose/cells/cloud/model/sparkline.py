"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Sparkline:
    """A sparkline represents a tiny chart or graphic in a worksheet cell that provides a visual representation of data."""
    column: Optional[int] = None
    data_range: Optional[str] = None
    row: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.column is not None:
            result["Column"] = self.column
        if self.data_range is not None:
            result["DataRange"] = self.data_range
        if self.row is not None:
            result["Row"] = self.row
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
