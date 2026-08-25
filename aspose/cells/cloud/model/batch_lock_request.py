"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class BatchLockRequest:
    """Indicates batch lock file request"""
    source_folder: Optional[str] = None
    source_storage: Optional[str] = None
    match_condition: Optional[MatchConditionRequest] = None
    password: Optional[str] = None
    out_folder: Optional[str] = None
    out_storage: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.source_folder is not None:
            result["SourceFolder"] = self.source_folder
        if self.source_storage is not None:
            result["SourceStorage"] = self.source_storage
        if self.match_condition is not None:
            result["MatchCondition"] = self.match_condition.to_dict()
        if self.password is not None:
            result["Password"] = self.password
        if self.out_folder is not None:
            result["OutFolder"] = self.out_folder
        if self.out_storage is not None:
            result["OutStorage"] = self.out_storage
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
