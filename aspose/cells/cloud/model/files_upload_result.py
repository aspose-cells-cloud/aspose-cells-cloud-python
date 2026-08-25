"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FilesUploadResult:
    """File upload result"""
    uploaded: Optional[List[str]] = None
    errors: Optional[List[Error]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.uploaded is not None:
            result["Uploaded"] = self.uploaded
        if self.errors is not None:
            result["Errors"] = [x.to_dict() for x in self.errors]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
