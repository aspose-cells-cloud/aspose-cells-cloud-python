"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class WorkbookOperateParameter:
    """Represents workbook operate parameter."""
    operate_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.operate_type is not None:
            result["OperateType"] = self.operate_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
