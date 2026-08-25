"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class MergedCells:
    """Sure, could you please provide me with the features you would like me to summarize?"""
    count: Optional[int] = None
    merged_cell_list: Optional[List[LinkElement]] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.count is not None:
            result["Count"] = self.count
        if self.merged_cell_list is not None:
            result["MergedCellList"] = [x.to_dict() for x in self.merged_cell_list]
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
