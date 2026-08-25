"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FileInfo:
    """Represents file information."""
    filename: Optional[str] = None
    file_size: Optional[int] = None
    file_content: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.filename is not None:
            result["Filename"] = self.filename
        if self.file_size is not None:
            result["FileSize"] = self.file_size
        if self.file_content is not None:
            result["FileContent"] = self.file_content
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
