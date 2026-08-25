"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ImportXMLRequest:
    """Indicates import xml data request"""
    xml_file_source: Optional[DataSource] = None
    import_position: Optional[ImportPosition] = None
    xml_content: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.xml_file_source is not None:
            result["XMLFileSource"] = self.xml_file_source.to_dict()
        if self.import_position is not None:
            result["ImportPosition"] = self.import_position.to_dict()
        if self.xml_content is not None:
            result["XMLContent"] = self.xml_content
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
