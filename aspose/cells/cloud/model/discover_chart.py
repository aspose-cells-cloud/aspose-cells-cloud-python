"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DiscoverChart:
    """Represents a chart, which is a chart created based on data analysis of a table."""
    name: Optional[str] = None
    sheet_name: Optional[str] = None
    title: Optional[str] = None
    type_: Optional[str] = None
    data_range: Optional[str] = None
    thumbnail: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.sheet_name is not None:
            result["SheetName"] = self.sheet_name
        if self.title is not None:
            result["Title"] = self.title
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.data_range is not None:
            result["DataRange"] = self.data_range
        if self.thumbnail is not None:
            result["Thumbnail"] = self.thumbnail
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
