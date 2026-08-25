"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DropBars:
    """Represents the up/down bars in a chart."""
    area: Optional[Area] = None
    border: Optional[Line] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.area is not None:
            result["Area"] = self.area.to_dict()
        if self.border is not None:
            result["Border"] = self.border.to_dict()
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
