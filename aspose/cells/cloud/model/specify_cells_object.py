"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SpecifyCellsObject:
    """SpecifyCellsObject."""
    worksheet_name: Optional[str] = None
    page_index: Optional[int] = None
    region: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.worksheet_name is not None:
            result["WorksheetName"] = self.worksheet_name
        if self.page_index is not None:
            result["PageIndex"] = self.page_index
        if self.region is not None:
            result["Region"] = self.region
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
