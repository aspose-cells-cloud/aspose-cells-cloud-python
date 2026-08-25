"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SaveOptionsData:
    """SaveOptionsData."""
    save_options: Optional[SaveOptions] = None
    filename: Optional[str] = None
    storage_name: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.save_options is not None:
            result["SaveOptions"] = self.save_options.to_dict()
        if self.filename is not None:
            result["Filename"] = self.filename
        if self.storage_name is not None:
            result["StorageName"] = self.storage_name
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
