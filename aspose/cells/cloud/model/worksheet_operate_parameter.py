"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class WorksheetOperateParameter:
    """Represents worksheet operate parameter."""
    name: Optional[str] = None
    sheet_type: Optional[str] = None
    new_name: Optional[str] = None
    moving_request: Optional[WorksheetMovingRequest] = None
    operate_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.sheet_type is not None:
            result["SheetType"] = self.sheet_type
        if self.new_name is not None:
            result["NewName"] = self.new_name
        if self.moving_request is not None:
            result["MovingRequest"] = self.moving_request.to_dict()
        if self.operate_type is not None:
            result["OperateType"] = self.operate_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
