"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ScopeItem:
    """Define the specific range in your Excel worksheet where you want the spreadsheet operations to be performed. This ensures that only the cells within the selected range are processed, and any operations are confined to this area."""
    worksheet: Optional[str] = None
    ranges: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.worksheet is not None:
            result["Worksheet"] = self.worksheet
        if self.ranges is not None:
            result["Ranges"] = self.ranges
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
