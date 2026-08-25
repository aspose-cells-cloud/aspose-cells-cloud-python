"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TextItem:
    """TextItem."""
    filename: Optional[str] = None
    worksheet: Optional[str] = None
    position: Optional[str] = None
    content: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.filename is not None:
            result["Filename"] = self.filename
        if self.worksheet is not None:
            result["Worksheet"] = self.worksheet
        if self.position is not None:
            result["Position"] = self.position
        if self.content is not None:
            result["Content"] = self.content
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
