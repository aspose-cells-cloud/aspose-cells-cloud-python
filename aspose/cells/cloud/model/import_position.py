"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ImportPosition:
    """I can help with that. Just provide me with the features you'd like me to summarize."""
    sheet_name: Optional[str] = None
    row_index: Optional[int] = None
    column_index: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.sheet_name is not None:
            result["SheetName"] = self.sheet_name
        if self.row_index is not None:
            result["RowIndex"] = self.row_index
        if self.column_index is not None:
            result["ColumnIndex"] = self.column_index
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
