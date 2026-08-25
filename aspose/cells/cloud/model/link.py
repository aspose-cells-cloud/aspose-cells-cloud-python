"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Link:
    """I'm glad to help! Please provide me with the features you would like me to summarize."""
    href: Optional[str] = None
    rel: Optional[str] = None
    title: Optional[str] = None
    type_: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.href is not None:
            result["Href"] = self.href
        if self.rel is not None:
            result["Rel"] = self.rel
        if self.title is not None:
            result["Title"] = self.title
        if self.type_ is not None:
            result["Type"] = self.type_
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
