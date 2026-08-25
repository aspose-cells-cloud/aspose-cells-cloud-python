"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SaveFilesToCloudResult:
    """Represents save file to cloud result."""
    saved_files: Optional[List[Link]] = None
    description: Optional[str] = None
    out_file_list: Optional[List[DataSource]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.saved_files is not None:
            result["SavedFiles"] = [x.to_dict() for x in self.saved_files]
        if self.description is not None:
            result["Description"] = self.description
        if self.out_file_list is not None:
            result["OutFileList"] = [x.to_dict() for x in self.out_file_list]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
