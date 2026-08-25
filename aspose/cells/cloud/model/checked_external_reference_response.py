"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CheckedExternalReferenceResponse:
    """CheckedExternalReferenceResponse."""
    reference_other_workbook: Optional[bool] = None
    reference_other_worksheet: Optional[bool] = None
    formulas: Optional[List[str]] = None
    code: Optional[int] = None
    status: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.reference_other_workbook is not None:
            result["ReferenceOtherWorkbook"] = self.reference_other_workbook
        if self.reference_other_worksheet is not None:
            result["ReferenceOtherWorksheet"] = self.reference_other_worksheet
        if self.formulas is not None:
            result["Formulas"] = self.formulas
        if self.code is not None:
            result["Code"] = self.code
        if self.status is not None:
            result["Status"] = self.status
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
