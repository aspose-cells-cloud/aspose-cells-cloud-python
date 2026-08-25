"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CellValue:
    """Represents the cell value and corresponding type."""
    row_index: Optional[int] = None
    column_index: Optional[int] = None
    type_: Optional[str] = None
    value: Optional[str] = None
    formula: Optional[str] = None
    style: Optional[Style] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.row_index is not None:
            result["rowIndex"] = self.row_index
        if self.column_index is not None:
            result["columnIndex"] = self.column_index
        if self.type_ is not None:
            result["type"] = self.type_
        if self.value is not None:
            result["value"] = self.value
        if self.formula is not None:
            result["formula"] = self.formula
        if self.style is not None:
            result["style"] = self.style.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
