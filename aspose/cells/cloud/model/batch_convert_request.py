"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class BatchConvertRequest:
    """Indicates batch convert file request"""
    source_folder: Optional[str] = None
    source_storage: Optional[str] = None
    match_condition: Optional[MatchConditionRequest] = None
    format_: Optional[str] = None
    out_folder: Optional[str] = None
    out_storage: Optional[str] = None
    region: Optional[str] = None
    page_wide_fit_on_per_sheet: Optional[bool] = None
    page_tall_fit_on_per_sheet: Optional[bool] = None
    save_options: Optional[SaveOptions] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.source_folder is not None:
            result["SourceFolder"] = self.source_folder
        if self.source_storage is not None:
            result["SourceStorage"] = self.source_storage
        if self.match_condition is not None:
            result["MatchCondition"] = self.match_condition.to_dict()
        if self.format_ is not None:
            result["Format"] = self.format_
        if self.out_folder is not None:
            result["OutFolder"] = self.out_folder
        if self.out_storage is not None:
            result["OutStorage"] = self.out_storage
        if self.region is not None:
            result["Region"] = self.region
        if self.page_wide_fit_on_per_sheet is not None:
            result["PageWideFitOnPerSheet"] = self.page_wide_fit_on_per_sheet
        if self.page_tall_fit_on_per_sheet is not None:
            result["PageTallFitOnPerSheet"] = self.page_tall_fit_on_per_sheet
        if self.save_options is not None:
            result["SaveOptions"] = self.save_options.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
