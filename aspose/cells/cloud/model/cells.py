"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Cells:
    """Encapsulates a collection of cell relevant objects, such as Aspose.Cells.Cell, Aspose.Cells.Row, ...etc."""
    max_row: Optional[int] = None
    max_column: Optional[int] = None
    cell_count: Optional[int] = None
    rows: Optional[LinkElement] = None
    columns: Optional[LinkElement] = None
    cell_list: Optional[List[LinkElement]] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.max_row is not None:
            result["MaxRow"] = self.max_row
        if self.max_column is not None:
            result["MaxColumn"] = self.max_column
        if self.cell_count is not None:
            result["CellCount"] = self.cell_count
        if self.rows is not None:
            result["Rows"] = self.rows.to_dict()
        if self.columns is not None:
            result["Columns"] = self.columns.to_dict()
        if self.cell_list is not None:
            result["CellList"] = [x.to_dict() for x in self.cell_list]
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
