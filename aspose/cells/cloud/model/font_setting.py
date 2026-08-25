"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FontSetting:
    """Represents a range of characters within the cell text."""
    font: Optional[Font] = None
    length: Optional[int] = None
    start_index: Optional[int] = None
    text_options: Optional[TextOptions] = None
    type_: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.font is not None:
            result["Font"] = self.font.to_dict()
        if self.length is not None:
            result["Length"] = self.length
        if self.start_index is not None:
            result["StartIndex"] = self.start_index
        if self.text_options is not None:
            result["TextOptions"] = self.text_options.to_dict()
        if self.type_ is not None:
            result["Type"] = self.type_
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
