"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Workbook:
    """Represents a root object to create an Excel spreadsheet."""
    file_name: Optional[str] = None
    links: Optional[List[Link]] = None
    worksheets: Optional[LinkElement] = None
    default_style: Optional[LinkElement] = None
    document_properties: Optional[LinkElement] = None
    names: Optional[LinkElement] = None
    settings: Optional[LinkElement] = None
    is_write_protected: Optional[str] = None
    is_protected: Optional[str] = None
    is_encryption: Optional[str] = None
    password: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.file_name is not None:
            result["FileName"] = self.file_name
        if self.links is not None:
            result["Links"] = [x.to_dict() for x in self.links]
        if self.worksheets is not None:
            result["Worksheets"] = self.worksheets.to_dict()
        if self.default_style is not None:
            result["DefaultStyle"] = self.default_style.to_dict()
        if self.document_properties is not None:
            result["DocumentProperties"] = self.document_properties.to_dict()
        if self.names is not None:
            result["Names"] = self.names.to_dict()
        if self.settings is not None:
            result["Settings"] = self.settings.to_dict()
        if self.is_write_protected is not None:
            result["IsWriteProtected"] = self.is_write_protected
        if self.is_protected is not None:
            result["IsProtected"] = self.is_protected
        if self.is_encryption is not None:
            result["IsEncryption"] = self.is_encryption
        if self.password is not None:
            result["Password"] = self.password
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
