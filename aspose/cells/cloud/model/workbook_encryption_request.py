"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class WorkbookEncryptionRequest:
    """Used by workbook encryption/decryption requests."""
    encryption_type: Optional[str] = None
    key_length: Optional[int] = None
    password: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.encryption_type is not None:
            result["EncryptionType"] = self.encryption_type
        if self.key_length is not None:
            result["KeyLength"] = self.key_length
        if self.password is not None:
            result["Password"] = self.password
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
