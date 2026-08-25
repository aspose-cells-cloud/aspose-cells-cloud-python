"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ObjectExist:
    """Object exists"""
    exists: Optional[bool] = None
    is_folder: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.exists is not None:
            result["Exists"] = self.exists
        if self.is_folder is not None:
            result["IsFolder"] = self.is_folder
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
