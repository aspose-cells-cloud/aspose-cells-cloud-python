"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class TextureFill:
    """Encapsulates the object that represents texture fill format"""
    type_: Optional[str] = None
    transparency: Optional[float] = None
    scale: Optional[float] = None
    tile_pic_option: Optional[TilePicOption] = None
    pic_format_option: Optional[PicFormatOption] = None
    image: Optional[LinkElement] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.transparency is not None:
            result["Transparency"] = self.transparency
        if self.scale is not None:
            result["Scale"] = self.scale
        if self.tile_pic_option is not None:
            result["TilePicOption"] = self.tile_pic_option.to_dict()
        if self.pic_format_option is not None:
            result["PicFormatOption"] = self.pic_format_option.to_dict()
        if self.image is not None:
            result["Image"] = self.image.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
