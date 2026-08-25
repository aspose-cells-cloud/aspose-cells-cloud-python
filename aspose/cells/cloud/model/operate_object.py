"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class OperateObject:
    """Represents operate object."""
    operate_object_type: Optional[str] = None
    position: Optional[OperateObjectPosition] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.operate_object_type is not None:
            result["OperateObjectType"] = self.operate_object_type
        if self.position is not None:
            result["Position"] = self.position.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
