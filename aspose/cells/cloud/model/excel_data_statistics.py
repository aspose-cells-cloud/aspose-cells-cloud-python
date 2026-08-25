"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ExcelDataStatistics:
    """Represents Excel data statistics."""
    worksheet_data_statistics: Optional[List[WorksheetDataStatistics]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.worksheet_data_statistics is not None:
            result["WorksheetDataStatistics"] = [x.to_dict() for x in self.worksheet_data_statistics]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
