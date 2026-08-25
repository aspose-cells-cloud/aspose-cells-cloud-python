"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class WriteProtection:
    """Specifies write protection settings for a workbook."""
    author: Optional[str] = None
    recommend_read_only: Optional[bool] = None
    is_write_protected: Optional[bool] = None
    password: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.author is not None:
            result["Author"] = self.author
        if self.recommend_read_only is not None:
            result["RecommendReadOnly"] = self.recommend_read_only
        if self.is_write_protected is not None:
            result["IsWriteProtected"] = self.is_write_protected
        if self.password is not None:
            result["Password"] = self.password
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
