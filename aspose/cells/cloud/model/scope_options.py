"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ScopeOptions:
    """Specifies the range of cells within the worksheet where the spreadsheet operations will be performed. This parameter allows users to define the exact area to be processed, ensuring that operations are applied only to the designated cells."""
    scope: Optional[str] = None
    scope_items: Optional[List[ScopeItem]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.scope is not None:
            result["Scope"] = self.scope
        if self.scope_items is not None:
            result["ScopeItems"] = [x.to_dict() for x in self.scope_items]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
