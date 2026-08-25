"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CheckedFormulaErrorsResponse:
    """CheckedFormulaErrorsResponse."""
    is_formulas_errors: Optional[bool] = None
    formulas_errors: Optional[List[str]] = None
    code: Optional[int] = None
    status: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.is_formulas_errors is not None:
            result["IsFormulasErrors"] = self.is_formulas_errors
        if self.formulas_errors is not None:
            result["FormulasErrors"] = self.formulas_errors
        if self.code is not None:
            result["Code"] = self.code
        if self.status is not None:
            result["Status"] = self.status
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
