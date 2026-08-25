"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class BatchSplitRequest:
    """Class summary: Identifying key features of a statistical dataset and methods for data analysis."""
    source_folder: Optional[str] = None
    source_storage: Optional[str] = None
    match_condition: Optional[MatchConditionRequest] = None
    format_: Optional[str] = None
    from_index: Optional[int] = None
    to_index: Optional[int] = None
    out_folder: Optional[str] = None
    out_storage: Optional[str] = None
    region: Optional[str] = None
    save_options: Optional[SaveOptions] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.source_folder is not None:
            result["SourceFolder"] = self.source_folder
        if self.source_storage is not None:
            result["SourceStorage"] = self.source_storage
        if self.match_condition is not None:
            result["MatchCondition"] = self.match_condition.to_dict()
        if self.format_ is not None:
            result["Format"] = self.format_
        if self.from_index is not None:
            result["FromIndex"] = self.from_index
        if self.to_index is not None:
            result["ToIndex"] = self.to_index
        if self.out_folder is not None:
            result["OutFolder"] = self.out_folder
        if self.out_storage is not None:
            result["OutStorage"] = self.out_storage
        if self.region is not None:
            result["Region"] = self.region
        if self.save_options is not None:
            result["SaveOptions"] = self.save_options.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
