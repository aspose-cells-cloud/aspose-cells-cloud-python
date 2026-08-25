"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class LegendEntries:
    """Sure, please provide me with the features you would like me to summarize in one sentence for the class summary."""
    legend_entry_list: Optional[List[LinkElement]] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.legend_entry_list is not None:
            result["legendEntryList"] = [x.to_dict() for x in self.legend_entry_list]
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
