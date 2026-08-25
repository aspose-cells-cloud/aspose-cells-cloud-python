"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class MatchConditionRequest:
    """Indicates the match condition that needs to be processed for the file name."""
    regex_pattern: Optional[str] = None
    full_match_conditions: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.regex_pattern is not None:
            result["RegexPattern"] = self.regex_pattern
        if self.full_match_conditions is not None:
            result["FullMatchConditions"] = self.full_match_conditions
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
