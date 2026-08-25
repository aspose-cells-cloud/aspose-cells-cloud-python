"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DiscUsage:
    """Class for disc space information."""
    used_size: Optional[int] = None
    total_size: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.used_size is not None:
            result["UsedSize"] = self.used_size
        if self.total_size is not None:
            result["TotalSize"] = self.total_size
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
