"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class WorksheetMovingRequest:
    """Used by workbook moving requests."""
    destination_worksheet: Optional[str] = None
    position: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.destination_worksheet is not None:
            result["DestinationWorksheet"] = self.destination_worksheet
        if self.position is not None:
            result["Position"] = self.position
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
