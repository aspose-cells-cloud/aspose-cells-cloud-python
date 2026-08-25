"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class HorizontalPageBreak:
    """Encapsulates the object that represents a horizontal page break."""
    row: Optional[int] = None
    end_column: Optional[int] = None
    start_column: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.row is not None:
            result["Row"] = self.row
        if self.end_column is not None:
            result["EndColumn"] = self.end_column
        if self.start_column is not None:
            result["StartColumn"] = self.start_column
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
