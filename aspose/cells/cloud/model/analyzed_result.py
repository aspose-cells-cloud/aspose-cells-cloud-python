"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AnalyzedResult:
    """Represents results of analyzed data."""
    filename: Optional[str] = None
    description: Optional[str] = None
    basic_statistics: Optional[ExcelDataStatistics] = None
    results: Optional[List[AnalyzedTableDescription]] = None
    suggested_file: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.filename is not None:
            result["Filename"] = self.filename
        if self.description is not None:
            result["Description"] = self.description
        if self.basic_statistics is not None:
            result["BasicStatistics"] = self.basic_statistics.to_dict()
        if self.results is not None:
            result["Results"] = [x.to_dict() for x in self.results]
        if self.suggested_file is not None:
            result["SuggestedFile"] = self.suggested_file
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
