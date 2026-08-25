"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CellsCloudFileInfo:
    """CellsCloudFileInfo."""
    name: Optional[str] = None
    size: Optional[int] = None
    folder: Optional[str] = None
    storage: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.size is not None:
            result["Size"] = self.size
        if self.folder is not None:
            result["Folder"] = self.folder
        if self.storage is not None:
            result["Storage"] = self.storage
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
