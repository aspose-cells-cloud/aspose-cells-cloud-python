"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CellsDocumentProperty:
    """Cells document property."""
    name: Optional[str] = None
    value: Optional[str] = None
    is_linked_to_content: Optional[str] = None
    source: Optional[str] = None
    type_: Optional[str] = None
    is_generated_name: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.value is not None:
            result["Value"] = self.value
        if self.is_linked_to_content is not None:
            result["IsLinkedToContent"] = self.is_linked_to_content
        if self.source is not None:
            result["Source"] = self.source
        if self.type_ is not None:
            result["Type"] = self.type_
        if self.is_generated_name is not None:
            result["IsGeneratedName"] = self.is_generated_name
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
