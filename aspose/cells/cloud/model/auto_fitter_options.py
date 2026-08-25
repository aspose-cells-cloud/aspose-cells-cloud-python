"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AutoFitterOptions:
    """Represents all auto fitter options."""
    auto_fit_merged_cells_type: Optional[str] = None
    ignore_hidden: Optional[bool] = None
    only_auto: Optional[bool] = None
    default_edit_language: Optional[str] = None
    max_row_height: Optional[float] = None
    auto_fit_wrapped_text_type: Optional[str] = None
    format_strategy: Optional[str] = None
    for_rendering: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.auto_fit_merged_cells_type is not None:
            result["AutoFitMergedCellsType"] = self.auto_fit_merged_cells_type
        if self.ignore_hidden is not None:
            result["IgnoreHidden"] = self.ignore_hidden
        if self.only_auto is not None:
            result["OnlyAuto"] = self.only_auto
        if self.default_edit_language is not None:
            result["DefaultEditLanguage"] = self.default_edit_language
        if self.max_row_height is not None:
            result["MaxRowHeight"] = self.max_row_height
        if self.auto_fit_wrapped_text_type is not None:
            result["AutoFitWrappedTextType"] = self.auto_fit_wrapped_text_type
        if self.format_strategy is not None:
            result["FormatStrategy"] = self.format_strategy
        if self.for_rendering is not None:
            result["ForRendering"] = self.for_rendering
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
