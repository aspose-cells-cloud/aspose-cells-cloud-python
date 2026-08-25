"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AbstractCalculationEngine:
    """Represents user's custom calculation engine to extend the default calculation engine of Aspose.Cells."""
    is_param_literal_required: Optional[bool] = None
    is_param_array_mode_required: Optional[bool] = None
    process_built_in_functions: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.is_param_literal_required is not None:
            result["IsParamLiteralRequired"] = self.is_param_literal_required
        if self.is_param_array_mode_required is not None:
            result["IsParamArrayModeRequired"] = self.is_param_array_mode_required
        if self.process_built_in_functions is not None:
            result["ProcessBuiltInFunctions"] = self.process_built_in_functions
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
