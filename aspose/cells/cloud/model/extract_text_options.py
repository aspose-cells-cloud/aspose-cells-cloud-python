"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ExtractTextOptions:
    """I'm happy to help! Could you please provide me with the features you would like me to summarize for you?"""
    name: Optional[str] = None
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    worksheet: Optional[str] = None
    range_: Optional[str] = None
    extract_text_type: Optional[str] = None
    before_text: Optional[str] = None
    after_text: Optional[str] = None
    before_position: Optional[int] = None
    after_position: Optional[int] = None
    out_position_range: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.worksheet is not None:
            result["Worksheet"] = self.worksheet
        if self.range_ is not None:
            result["Range"] = self.range_
        if self.extract_text_type is not None:
            result["ExtractTextType"] = self.extract_text_type
        if self.before_text is not None:
            result["BeforeText"] = self.before_text
        if self.after_text is not None:
            result["AfterText"] = self.after_text
        if self.before_position is not None:
            result["BeforePosition"] = self.before_position
        if self.after_position is not None:
            result["AfterPosition"] = self.after_position
        if self.out_position_range is not None:
            result["OutPositionRange"] = self.out_position_range
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
