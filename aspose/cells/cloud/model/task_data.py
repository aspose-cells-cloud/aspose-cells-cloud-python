"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TaskData:
    """Represents task data."""
    tasks: Optional[List[TaskDescription]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.tasks is not None:
            result["Tasks"] = [x.to_dict() for x in self.tasks]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
