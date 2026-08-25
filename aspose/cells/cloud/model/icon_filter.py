"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class IconFilter:
    """Represents icon filter."""
    icon_id: Optional[int] = None
    icon_set_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.icon_id is not None:
            result["IconId"] = self.icon_id
        if self.icon_set_type is not None:
            result["IconSetType"] = self.icon_set_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
