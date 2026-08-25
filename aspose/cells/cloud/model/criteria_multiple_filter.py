"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CriteriaMultipleFilter:
    """1. Collaboration: Students will have the opportunity to work together on group projects and assignments. 2. Critical Thinking: Students will be encouraged to analyze, evaluate, and interpret information in a meaningful way. 3. Hands-on Learning: Students will participate in experiential activities to apply theoretical knowledge in practical settings. 4. Technology Integration: Students will utilize various digital tools and platforms to enhance their learning experience. 5. Communication Skills: Students will develop effective verbal and written communication skills through presentations and written assignments."""
    criteria: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.criteria is not None:
            result["Criteria"] = self.criteria
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
