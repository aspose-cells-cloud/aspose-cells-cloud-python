"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ColorScale:
    """Describe the ColorScale conditional formatting rule. This conditional formatting rule creates a gradated color scale on the cells."""
    max_cfvo: Optional[ConditionalFormattingValue] = None
    max_color: Optional[Color] = None
    mid_cfvo: Optional[ConditionalFormattingValue] = None
    mid_color: Optional[Color] = None
    min_cfvo: Optional[ConditionalFormattingValue] = None
    min_color: Optional[Color] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.max_cfvo is not None:
            result["MaxCfvo"] = self.max_cfvo.to_dict()
        if self.max_color is not None:
            result["MaxColor"] = self.max_color.to_dict()
        if self.mid_cfvo is not None:
            result["MidCfvo"] = self.mid_cfvo.to_dict()
        if self.mid_color is not None:
            result["MidColor"] = self.mid_color.to_dict()
        if self.min_cfvo is not None:
            result["MinCfvo"] = self.min_cfvo.to_dict()
        if self.min_color is not None:
            result["MinColor"] = self.min_color.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
