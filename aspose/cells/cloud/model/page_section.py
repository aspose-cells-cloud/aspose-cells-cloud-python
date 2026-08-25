"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PageSection:
    """Class summary: Includes interactive discussions, group projects, guest speakers, and practical applications of course material."""
    section: Optional[int] = None
    context: Optional[str] = None
    picture: Optional[str] = None
    fisrt_page_context: Optional[str] = None
    even_page_context: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.section is not None:
            result["Section"] = self.section
        if self.context is not None:
            result["Context"] = self.context
        if self.picture is not None:
            result["Picture"] = self.picture
        if self.fisrt_page_context is not None:
            result["FisrtPageContext"] = self.fisrt_page_context
        if self.even_page_context is not None:
            result["EvenPageContext"] = self.even_page_context
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
