"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FileSource:
    """I'm sorry, I just realized you didn't provide any features for me to summarize. Please provide the features you'd like me to summarize for the class."""
    file_source_type: Optional[str] = None
    file_path: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.file_source_type is not None:
            result["FileSourceType"] = self.file_source_type
        if self.file_path is not None:
            result["FilePath"] = self.file_path
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
