"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ConditionalFormatting:
    """I'm here to help! Please provide me with the features that need to be summarized."""
    sqref: Optional[str] = None
    format_conditions: Optional[List[FormatCondition]] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.sqref is not None:
            result["sqref"] = self.sqref
        if self.format_conditions is not None:
            result["FormatConditions"] = [x.to_dict() for x in self.format_conditions]
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
