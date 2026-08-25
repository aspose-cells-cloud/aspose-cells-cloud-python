"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ConditionalFormattingIcon:
    """Represents  the custom  icon of conditional formatting rule."""
    image_data: Optional[str] = None
    index: Optional[int] = None
    type_: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.image_data is not None:
            result["ImageData"] = self.image_data
        if self.index is not None:
            result["Index"] = self.index
        if self.type_ is not None:
            result["Type"] = self.type_
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
