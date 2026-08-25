"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AppliedOperate:
    """A data operation that is used to obtain a query of data."""
    applied_operate_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.applied_operate_type is not None:
            result["AppliedOperateType"] = self.applied_operate_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
