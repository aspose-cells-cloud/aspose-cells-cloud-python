"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CheckExternalReferenceOptions:
    """CheckExternalReferenceOptions."""
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    worksheet: Optional[str] = None
    ranged__table: Optional[str] = None
    chart_index: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.worksheet is not None:
            result["Worksheet"] = self.worksheet
        if self.ranged__table is not None:
            result["Ranged_Table"] = self.ranged__table
        if self.chart_index is not None:
            result["ChartIndex"] = self.chart_index
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
