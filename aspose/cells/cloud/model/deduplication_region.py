"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DeduplicationRegion:
    """Represents data deduplication region."""
    ranges: Optional[List[Range]] = None
    worksheet_name_list: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.ranges is not None:
            result["Ranges"] = [x.to_dict() for x in self.ranges]
        if self.worksheet_name_list is not None:
            result["WorksheetNameList"] = self.worksheet_name_list
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
