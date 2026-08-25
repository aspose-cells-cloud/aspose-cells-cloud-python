"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class LoadTo:
    """A description of the location to which the data is mounted."""
    worksheet: Optional[str] = None
    begin_row_index: Optional[int] = None
    begin_column_index: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.worksheet is not None:
            result["Worksheet"] = self.worksheet
        if self.begin_row_index is not None:
            result["beginRowIndex"] = self.begin_row_index
        if self.begin_column_index is not None:
            result["beginColumnIndex"] = self.begin_column_index
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
