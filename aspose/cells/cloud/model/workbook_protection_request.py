"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class WorkbookProtectionRequest:
    """Used by workbook protection requests."""
    protection_type: Optional[str] = None
    password: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.protection_type is not None:
            result["ProtectionType"] = self.protection_type
        if self.password is not None:
            result["Password"] = self.password
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
