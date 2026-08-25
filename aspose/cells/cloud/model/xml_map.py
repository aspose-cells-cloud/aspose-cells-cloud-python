"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class XmlMap:
    """Represents Xml map information."""
    name: Optional[str] = None
    root_element_name: Optional[str] = None
    data_binding: Optional[XmlDataBinding] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.name is not None:
            result["Name"] = self.name
        if self.root_element_name is not None:
            result["RootElementName"] = self.root_element_name
        if self.data_binding is not None:
            result["DataBinding"] = self.data_binding.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
