"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ProtectWorkbookRequest:
    """Indicates protect workbook request"""
    aways_open_read_only: Optional[bool] = None
    encrypt_with_password: Optional[str] = None
    protect_current_sheet: Optional[Protection] = None
    protect_all_sheets: Optional[Protection] = None
    protect_workbook_structure: Optional[str] = None
    digital_signature: Optional[DigitalSignature] = None
    mark_as_final: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.aways_open_read_only is not None:
            result["AwaysOpenReadOnly"] = self.aways_open_read_only
        if self.encrypt_with_password is not None:
            result["EncryptWithPassword"] = self.encrypt_with_password
        if self.protect_current_sheet is not None:
            result["ProtectCurrentSheet"] = self.protect_current_sheet.to_dict()
        if self.protect_all_sheets is not None:
            result["ProtectAllSheets"] = self.protect_all_sheets.to_dict()
        if self.protect_workbook_structure is not None:
            result["ProtectWorkbookStructure"] = self.protect_workbook_structure
        if self.digital_signature is not None:
            result["DigitalSignature"] = self.digital_signature.to_dict()
        if self.mark_as_final is not None:
            result["MarkAsFinal"] = self.mark_as_final
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
