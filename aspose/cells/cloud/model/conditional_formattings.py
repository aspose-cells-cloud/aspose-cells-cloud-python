"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ConditionalFormattings:
    """Encapsulates a collection of  objects."""
    count: Optional[int] = None
    conditional_formatting_list: Optional[List[ConditionalFormatting]] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.count is not None:
            result["Count"] = self.count
        if self.conditional_formatting_list is not None:
            result["ConditionalFormattingList"] = [x.to_dict() for x in self.conditional_formatting_list]
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
