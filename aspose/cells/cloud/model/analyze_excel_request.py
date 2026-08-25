"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AnalyzeExcelRequest:
    """Can you please provide the features that you would like me to summarize for the class?"""
    files: Optional[List[FileInfo]] = None
    need_thumbnail: Optional[bool] = None
    build_suggestoin_sheet: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.files is not None:
            result["Files"] = [x.to_dict() for x in self.files]
        if self.need_thumbnail is not None:
            result["NeedThumbnail"] = self.need_thumbnail
        if self.build_suggestoin_sheet is not None:
            result["BuildSuggestoinSheet"] = self.build_suggestoin_sheet
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
