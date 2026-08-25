"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AutoFilter:
    """Represents autofiltering for the specified worksheet."""
    filter_columns: Optional[List[FilterColumn]] = None
    range_: Optional[str] = None
    sorter: Optional[DataSorter] = None
    show_filter_button: Optional[bool] = None
    link: Optional[Link] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.filter_columns is not None:
            result["FilterColumns"] = [x.to_dict() for x in self.filter_columns]
        if self.range_ is not None:
            result["Range"] = self.range_
        if self.sorter is not None:
            result["Sorter"] = self.sorter.to_dict()
        if self.show_filter_button is not None:
            result["ShowFilterButton"] = self.show_filter_button
        if self.link is not None:
            result["link"] = self.link.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
