"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class DataSource:
    """Represents data source."""
    data_source_type: Optional[str] = None
    data_path: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source_type is not None:
            result["DataSourceType"] = self.data_source_type
        if self.data_path is not None:
            result["DataPath"] = self.data_path
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
