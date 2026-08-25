"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PdfSecurityOptions:
    """PdfSecurityOptions."""
    annotations_permission: Optional[bool] = None
    assemble_document_permission: Optional[bool] = None
    extract_content_permission: Optional[bool] = None
    fill_forms_permission: Optional[bool] = None
    full_quality_print_permission: Optional[bool] = None
    modify_document_permission: Optional[bool] = None
    owner_password: Optional[str] = None
    print_permission: Optional[bool] = None
    user_password: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.annotations_permission is not None:
            result["AnnotationsPermission"] = self.annotations_permission
        if self.assemble_document_permission is not None:
            result["AssembleDocumentPermission"] = self.assemble_document_permission
        if self.extract_content_permission is not None:
            result["ExtractContentPermission"] = self.extract_content_permission
        if self.fill_forms_permission is not None:
            result["FillFormsPermission"] = self.fill_forms_permission
        if self.full_quality_print_permission is not None:
            result["FullQualityPrintPermission"] = self.full_quality_print_permission
        if self.modify_document_permission is not None:
            result["ModifyDocumentPermission"] = self.modify_document_permission
        if self.owner_password is not None:
            result["OwnerPassword"] = self.owner_password
        if self.print_permission is not None:
            result["PrintPermission"] = self.print_permission
        if self.user_password is not None:
            result["UserPassword"] = self.user_password
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
