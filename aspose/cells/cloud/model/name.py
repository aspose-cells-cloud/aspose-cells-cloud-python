"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Name:
    """Represents a defined name for a range of cells."""
    comment: Optional[str] = None
    worksheet_index: Optional[int] = None
    is_referred: Optional[bool] = None
    is_visible: Optional[bool] = None
    r1_c1_refers_to: Optional[str] = None
    refers_to: Optional[str] = None
    text: Optional[str] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.comment is not None:
            result["Comment"] = self.comment
        if self.worksheet_index is not None:
            result["WorksheetIndex"] = self.worksheet_index
        if self.is_referred is not None:
            result["IsReferred"] = self.is_referred
        if self.is_visible is not None:
            result["IsVisible"] = self.is_visible
        if self.r1_c1_refers_to is not None:
            result["R1C1RefersTo"] = self.r1_c1_refers_to
        if self.refers_to is not None:
            result["RefersTo"] = self.refers_to
        if self.text is not None:
            result["Text"] = self.text
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
