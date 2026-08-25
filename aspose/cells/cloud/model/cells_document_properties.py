"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CellsDocumentProperties:
    """Excel properties"""
    document_property_list: Optional[List[CellsDocumentProperty]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.document_property_list is not None:
            result["DocumentPropertyList"] = [x.to_dict() for x in self.document_property_list]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
