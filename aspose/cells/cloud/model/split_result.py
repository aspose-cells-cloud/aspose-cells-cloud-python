"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SplitResult:
    """Represents the result of the file split."""
    documents: Optional[List[CellsCloudFileInfo]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.documents is not None:
            result["Documents"] = [x.to_dict() for x in self.documents]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
