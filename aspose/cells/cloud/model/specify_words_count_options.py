"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SpecifyWordsCountOptions:
    """SpecifyWordsCountOptions."""
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    search_word: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.search_word is not None:
            result["SearchWord"] = self.search_word
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
