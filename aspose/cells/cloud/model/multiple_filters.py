"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class MultipleFilters:
    """Represents the multiple filter collection."""
    match_blank: Optional[bool] = None
    multiple_filter_list: Optional[List[MultipleFilter]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.match_blank is not None:
            result["MatchBlank"] = self.match_blank
        if self.multiple_filter_list is not None:
            result["MultipleFilterList"] = [x.to_dict() for x in self.multiple_filter_list]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
