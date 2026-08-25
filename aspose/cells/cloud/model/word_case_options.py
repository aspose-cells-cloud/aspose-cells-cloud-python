"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class WordCaseOptions:
    """I'm here to assist you. Please provide the features you would like me to summarize for the class."""
    data_source: Optional[DataSource] = None
    file_info: Optional[FileInfo] = None
    word_case_type: Optional[str] = None
    scope_options: Optional[ScopeOptions] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.file_info is not None:
            result["FileInfo"] = self.file_info.to_dict()
        if self.word_case_type is not None:
            result["WordCaseType"] = self.word_case_type
        if self.scope_options is not None:
            result["ScopeOptions"] = self.scope_options.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
