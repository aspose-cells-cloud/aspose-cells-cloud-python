"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FilesResult:
    """Class features: Weekly lectures, group projects, midterm and final exams, and participation in class discussions."""
    files: Optional[List[FileInfo]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.files is not None:
            result["Files"] = [x.to_dict() for x in self.files]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
