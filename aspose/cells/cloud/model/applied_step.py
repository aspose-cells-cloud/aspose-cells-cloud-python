"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AppliedStep:
    """Each data manipulation step that is performed when you get the query data."""
    step_name: Optional[str] = None
    applied_operate: Optional[AppliedOperate] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.step_name is not None:
            result["StepName"] = self.step_name
        if self.applied_operate is not None:
            result["AppliedOperate"] = self.applied_operate.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
