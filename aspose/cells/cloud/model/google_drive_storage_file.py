"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
import datetime
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class GoogleDriveStorageFile:
    """GoogleDriveStorageFile."""
    mime_type: Optional[str] = None
    name: Optional[str] = None
    is_folder: Optional[bool] = None
    modified_date: Optional[datetime.datetime] = None
    size: Optional[int] = None
    path: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.mime_type is not None:
            result["MimeType"] = self.mime_type
        if self.name is not None:
            result["Name"] = self.name
        if self.is_folder is not None:
            result["IsFolder"] = self.is_folder
        if self.modified_date is not None:
            result["ModifiedDate"] = self.modified_date
        if self.size is not None:
            result["Size"] = self.size
        if self.path is not None:
            result["Path"] = self.path
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
