"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FilesList:
    """Files list"""
    value: Optional[List[StorageFile]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.value is not None:
            result["Value"] = [x.to_dict() for x in self.value]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
