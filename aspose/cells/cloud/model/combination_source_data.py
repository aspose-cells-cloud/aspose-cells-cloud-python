"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CombinationSourceData:
    """CombinationSourceData."""
    tag: Optional[str] = None
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    worksheet: Optional[str] = None
    table_name: Optional[str] = None
    cell_area: Optional[str] = None
    has_header: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.tag is not None:
            result["Tag"] = self.tag
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.worksheet is not None:
            result["Worksheet"] = self.worksheet
        if self.table_name is not None:
            result["TableName"] = self.table_name
        if self.cell_area is not None:
            result["CellArea"] = self.cell_area
        if self.has_header is not None:
            result["HasHeader"] = self.has_header
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
