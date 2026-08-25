"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CheckFormulaErrorOptions:
    """CheckFormulaErrorOptions."""
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    sheet_name: Optional[str] = None
    chart_index: Optional[int] = None
    names: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.sheet_name is not None:
            result["SheetName"] = self.sheet_name
        if self.chart_index is not None:
            result["ChartIndex"] = self.chart_index
        if self.names is not None:
            result["Names"] = self.names
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
