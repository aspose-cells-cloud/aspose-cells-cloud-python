"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CustomParserConfig:
    """I'm happy to help! Please provide me with the features you would like me to summarize for the class."""
    column_index: Optional[int] = None
    parse_method: Optional[str] = None
    custom_style: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.column_index is not None:
            result["ColumnIndex"] = self.column_index
        if self.parse_method is not None:
            result["ParseMethod"] = self.parse_method
        if self.custom_style is not None:
            result["CustomStyle"] = self.custom_style
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
