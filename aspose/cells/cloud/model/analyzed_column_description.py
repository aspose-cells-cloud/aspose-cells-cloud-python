"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class AnalyzedColumnDescription:
    """Represents description of analyzed column."""
    index: Optional[int] = None
    column_index: Optional[int] = None
    title: Optional[str] = None
    repetition_rate: Optional[float] = None
    column_data_data_type: Optional[str] = None
    number_category_type: Optional[str] = None
    text_category_type: Optional[str] = None
    style_number: Optional[int] = None
    column_data_exception_description: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.index is not None:
            result["Index"] = self.index
        if self.column_index is not None:
            result["ColumnIndex"] = self.column_index
        if self.title is not None:
            result["Title"] = self.title
        if self.repetition_rate is not None:
            result["RepetitionRate"] = self.repetition_rate
        if self.column_data_data_type is not None:
            result["ColumnDataDataType"] = self.column_data_data_type
        if self.number_category_type is not None:
            result["NumberCategoryType"] = self.number_category_type
        if self.text_category_type is not None:
            result["TextCategoryType"] = self.text_category_type
        if self.style_number is not None:
            result["StyleNumber"] = self.style_number
        if self.column_data_exception_description is not None:
            result["columnDataExceptionDescription"] = self.column_data_exception_description
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
