"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TaskDescription:
    """Represents task description."""
    task_type: Optional[str] = None
    task_parameter: Optional[TaskParameter] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.task_type is not None:
            result["TaskType"] = self.task_type
        if self.task_parameter is not None:
            result["TaskParameter"] = self.task_parameter.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
