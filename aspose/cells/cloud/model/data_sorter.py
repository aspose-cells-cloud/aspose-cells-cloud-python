"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataSorter:
    """Summary description for DataSorter."""
    case_sensitive: Optional[bool] = None
    has_headers: Optional[bool] = None
    key_list: Optional[List[SortKey]] = None
    sort_left_to_right: Optional[bool] = None
    sort_as_number: Optional[bool] = None
    keys: Optional[List[DataSorterKey]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.case_sensitive is not None:
            result["CaseSensitive"] = self.case_sensitive
        if self.has_headers is not None:
            result["HasHeaders"] = self.has_headers
        if self.key_list is not None:
            result["KeyList"] = [x.to_dict() for x in self.key_list]
        if self.sort_left_to_right is not None:
            result["SortLeftToRight"] = self.sort_left_to_right
        if self.sort_as_number is not None:
            result["SortAsNumber"] = self.sort_as_number
        if self.keys is not None:
            result["Keys"] = [x.to_dict() for x in self.keys]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
