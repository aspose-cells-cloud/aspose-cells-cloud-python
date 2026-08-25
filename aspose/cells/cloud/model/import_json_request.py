"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ImportJsonRequest:
    """Indicates import xml data request"""
    json_file_source: Optional[DataSource] = None
    import_position: Optional[ImportPosition] = None
    json_content: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.json_file_source is not None:
            result["JsonFileSource"] = self.json_file_source.to_dict()
        if self.import_position is not None:
            result["ImportPosition"] = self.import_position.to_dict()
        if self.json_content is not None:
            result["JsonContent"] = self.json_content
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
