"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataFillRequest:
    """I'm happy to help! Please provide the features you would like me to summarize."""
    file: Optional[FileInfo] = None
    out_file_format: Optional[str] = None
    check_excel_restriction: Optional[bool] = None
    region: Optional[str] = None
    data_fill: Optional[DataFill] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.file is not None:
            result["File"] = self.file.to_dict()
        if self.out_file_format is not None:
            result["OutFileFormat"] = self.out_file_format
        if self.check_excel_restriction is not None:
            result["CheckExcelRestriction"] = self.check_excel_restriction
        if self.region is not None:
            result["Region"] = self.region
        if self.data_fill is not None:
            result["DataFill"] = self.data_fill.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
