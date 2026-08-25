"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class LoadData:
    """Loading data information."""
    load_to: Optional[LoadTo] = None
    data_query: Optional[DataQuery] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.load_to is not None:
            result["LoadTo"] = self.load_to.to_dict()
        if self.data_query is not None:
            result["DataQuery"] = self.data_query.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
