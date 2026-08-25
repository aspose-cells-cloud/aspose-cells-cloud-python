"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TextWaterMarkerRequest:
    """Indicates text water marker request."""
    text: Optional[str] = None
    font_name: Optional[str] = None
    font_size: Optional[int] = None
    height: Optional[int] = None
    width: Optional[int] = None
    image_adapt_option: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.text is not None:
            result["Text"] = self.text
        if self.font_name is not None:
            result["FontName"] = self.font_name
        if self.font_size is not None:
            result["FontSize"] = self.font_size
        if self.height is not None:
            result["Height"] = self.height
        if self.width is not None:
            result["Width"] = self.width
        if self.image_adapt_option is not None:
            result["ImageAdaptOption"] = self.image_adapt_option
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
