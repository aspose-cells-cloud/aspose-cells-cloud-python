"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataDeduplicationRequest:
    """DataDeduplicationRequest."""
    file: Optional[FileInfo] = None
    deduplication_region: Optional[DeduplicationRegion] = None
    out_file_format: Optional[str] = None
    check_excel_restriction: Optional[bool] = None
    region: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.file is not None:
            result["File"] = self.file.to_dict()
        if self.deduplication_region is not None:
            result["DeduplicationRegion"] = self.deduplication_region.to_dict()
        if self.out_file_format is not None:
            result["OutFileFormat"] = self.out_file_format
        if self.check_excel_restriction is not None:
            result["CheckExcelRestriction"] = self.check_excel_restriction
        if self.region is not None:
            result["Region"] = self.region
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
