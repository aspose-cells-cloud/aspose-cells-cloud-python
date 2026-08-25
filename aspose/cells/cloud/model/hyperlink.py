"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Hyperlink:
    """Encapsulates the object that represents a hyperlink."""
    address: Optional[str] = None
    area: Optional[CellArea] = None
    screen_tip: Optional[str] = None
    text_to_display: Optional[str] = None
    link_type: Optional[str] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.address is not None:
            result["Address"] = self.address
        if self.area is not None:
            result["Area"] = self.area.to_dict()
        if self.screen_tip is not None:
            result["ScreenTip"] = self.screen_tip
        if self.text_to_display is not None:
            result["TextToDisplay"] = self.text_to_display
        if self.link_type is not None:
            result["LinkType"] = self.link_type
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
