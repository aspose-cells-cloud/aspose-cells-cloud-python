"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class FormulaSettings:
    """Settings of formulas and calculation."""
    calculate_on_open: Optional[bool] = None
    calculate_on_save: Optional[bool] = None
    force_full_calculation: Optional[bool] = None
    calculation_mode: Optional[str] = None
    calculation_id: Optional[str] = None
    enable_iterative_calculation: Optional[bool] = None
    max_iteration: Optional[int] = None
    max_change: Optional[float] = None
    precision_as_displayed: Optional[bool] = None
    enable_calculation_chain: Optional[bool] = None
    preserve_padding_spaces: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.calculate_on_open is not None:
            result["CalculateOnOpen"] = self.calculate_on_open
        if self.calculate_on_save is not None:
            result["CalculateOnSave"] = self.calculate_on_save
        if self.force_full_calculation is not None:
            result["ForceFullCalculation"] = self.force_full_calculation
        if self.calculation_mode is not None:
            result["CalculationMode"] = self.calculation_mode
        if self.calculation_id is not None:
            result["CalculationId"] = self.calculation_id
        if self.enable_iterative_calculation is not None:
            result["EnableIterativeCalculation"] = self.enable_iterative_calculation
        if self.max_iteration is not None:
            result["MaxIteration"] = self.max_iteration
        if self.max_change is not None:
            result["MaxChange"] = self.max_change
        if self.precision_as_displayed is not None:
            result["PrecisionAsDisplayed"] = self.precision_as_displayed
        if self.enable_calculation_chain is not None:
            result["EnableCalculationChain"] = self.enable_calculation_chain
        if self.preserve_padding_spaces is not None:
            result["PreservePaddingSpaces"] = self.preserve_padding_spaces
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
