"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class HyperlinkResponse:
    """Represents the Hyperlink Response."""
    hyperlink: Optional[Hyperlink] = None
    code: Optional[int] = None
    status: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.hyperlink is not None:
            result["Hyperlink"] = self.hyperlink.to_dict()
        if self.code is not None:
            result["Code"] = self.code
        if self.status is not None:
            result["Status"] = self.status
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
