"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class RenderingWatermark:
    """RenderingWatermark."""
    rotation: Optional[float] = None
    scale_to_page_percent: Optional[int] = None
    opacity: Optional[float] = None
    is_background: Optional[bool] = None
    text: Optional[str] = None
    font: Optional[RenderingFont] = None
    image: Optional[List[bytes]] = None
    h_alignment: Optional[str] = None
    v_alignment: Optional[str] = None
    offset_x: Optional[float] = None
    offset_y: Optional[float] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.rotation is not None:
            result["Rotation"] = self.rotation
        if self.scale_to_page_percent is not None:
            result["ScaleToPagePercent"] = self.scale_to_page_percent
        if self.opacity is not None:
            result["Opacity"] = self.opacity
        if self.is_background is not None:
            result["IsBackground"] = self.is_background
        if self.text is not None:
            result["Text"] = self.text
        if self.font is not None:
            result["Font"] = self.font.to_dict()
        if self.image is not None:
            result["Image"] = self.image
        if self.h_alignment is not None:
            result["HAlignment"] = self.h_alignment
        if self.v_alignment is not None:
            result["VAlignment"] = self.v_alignment
        if self.offset_x is not None:
            result["OffsetX"] = self.offset_x
        if self.offset_y is not None:
            result["OffsetY"] = self.offset_y
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
