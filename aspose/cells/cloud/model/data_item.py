"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataItem:
    """Represents data item."""
    data_item_type: Optional[str] = None
    value: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_item_type is not None:
            result["DataItemType"] = self.data_item_type
        if self.value is not None:
            result["Value"] = self.value
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
