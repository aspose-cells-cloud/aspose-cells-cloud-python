"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class CopyOptions:
    """Represents the copy options."""
    column_character_width: Optional[bool] = None
    copy_invalid_formulas_as_values: Optional[bool] = None
    copy_names: Optional[bool] = None
    extend_to_adjacent_range: Optional[bool] = None
    refer_to_destination_sheet: Optional[bool] = None
    refer_to_sheet_with_same_name: Optional[bool] = None
    copy_theme: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.column_character_width is not None:
            result["ColumnCharacterWidth"] = self.column_character_width
        if self.copy_invalid_formulas_as_values is not None:
            result["CopyInvalidFormulasAsValues"] = self.copy_invalid_formulas_as_values
        if self.copy_names is not None:
            result["CopyNames"] = self.copy_names
        if self.extend_to_adjacent_range is not None:
            result["ExtendToAdjacentRange"] = self.extend_to_adjacent_range
        if self.refer_to_destination_sheet is not None:
            result["ReferToDestinationSheet"] = self.refer_to_destination_sheet
        if self.refer_to_sheet_with_same_name is not None:
            result["ReferToSheetWithSameName"] = self.refer_to_sheet_with_same_name
        if self.copy_theme is not None:
            result["CopyTheme"] = self.copy_theme
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
