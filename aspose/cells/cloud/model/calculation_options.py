"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CalculationOptions:
    """Represents options for calculation."""
    calc_stack_size: Optional[int] = None
    ignore_error: Optional[bool] = None
    precision_strategy: Optional[str] = None
    recursive: Optional[bool] = None
    custom_engine: Optional[AbstractCalculationEngine] = None
    calculation_monitor: Optional[AbstractCalculationMonitor] = None
    linked_data_sources: Optional[List[Workbook]] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.calc_stack_size is not None:
            result["CalcStackSize"] = self.calc_stack_size
        if self.ignore_error is not None:
            result["IgnoreError"] = self.ignore_error
        if self.precision_strategy is not None:
            result["PrecisionStrategy"] = self.precision_strategy
        if self.recursive is not None:
            result["Recursive"] = self.recursive
        if self.custom_engine is not None:
            result["CustomEngine"] = self.custom_engine.to_dict()
        if self.calculation_monitor is not None:
            result["CalculationMonitor"] = self.calculation_monitor.to_dict()
        if self.linked_data_sources is not None:
            result["LinkedDataSources"] = [x.to_dict() for x in self.linked_data_sources]
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
