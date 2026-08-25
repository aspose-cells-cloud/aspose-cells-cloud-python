"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TilePicOption:
    """Represents tile picture as texture."""
    offset_x: Optional[float] = None
    offset_y: Optional[float] = None
    scale_x: Optional[float] = None
    scale_y: Optional[float] = None
    alignment_type: Optional[str] = None
    mirror_type: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.offset_x is not None:
            result["OffsetX"] = self.offset_x
        if self.offset_y is not None:
            result["OffsetY"] = self.offset_y
        if self.scale_x is not None:
            result["ScaleX"] = self.scale_x
        if self.scale_y is not None:
            result["ScaleY"] = self.scale_y
        if self.alignment_type is not None:
            result["AlignmentType"] = self.alignment_type
        if self.mirror_type is not None:
            result["MirrorType"] = self.mirror_type
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
