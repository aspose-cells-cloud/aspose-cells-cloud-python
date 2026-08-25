"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FormulaFormatCondition:
    """Class summary: This class covers various features related to data visualization and graphical representation of data sets."""
    formula1: Optional[str] = None
    formula2: Optional[str] = None
    operator: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.formula1 is not None:
            result["Formula1"] = self.formula1
        if self.formula2 is not None:
            result["Formula2"] = self.formula2
        if self.operator is not None:
            result["Operator"] = self.operator
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
