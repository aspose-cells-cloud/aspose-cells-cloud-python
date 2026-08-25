"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CellArea:
    """CellArea."""
    end_column: Optional[int] = None
    end_row: Optional[int] = None
    start_column: Optional[int] = None
    start_row: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.end_column is not None:
            result["EndColumn"] = self.end_column
        if self.end_row is not None:
            result["EndRow"] = self.end_row
        if self.start_column is not None:
            result["StartColumn"] = self.start_column
        if self.start_row is not None:
            result["StartRow"] = self.start_row
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
