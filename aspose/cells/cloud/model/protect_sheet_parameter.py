"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ProtectSheetParameter:
    """Class Summary: The features discussed include natural language processing, image recognition, data visualization, clustering, regression, classification, and recommendation systems."""
    protection_type: Optional[str] = None
    password: Optional[str] = None
    allow_edit_area: Optional[List[str]] = None
    allow_deleting_column: Optional[str] = None
    allow_deleting_row: Optional[str] = None
    allow_filtering: Optional[str] = None
    allow_formatting_cell: Optional[str] = None
    allow_formatting_column: Optional[str] = None
    allow_formatting_row: Optional[str] = None
    allow_inserting_column: Optional[str] = None
    allow_inserting_hyperlink: Optional[str] = None
    allow_inserting_row: Optional[str] = None
    allow_selecting_locked_cell: Optional[str] = None
    allow_selecting_unlocked_cell: Optional[str] = None
    allow_sorting: Optional[str] = None
    allow_using_pivot_table: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.protection_type is not None:
            result["ProtectionType"] = self.protection_type
        if self.password is not None:
            result["Password"] = self.password
        if self.allow_edit_area is not None:
            result["AllowEditArea"] = self.allow_edit_area
        if self.allow_deleting_column is not None:
            result["AllowDeletingColumn"] = self.allow_deleting_column
        if self.allow_deleting_row is not None:
            result["AllowDeletingRow"] = self.allow_deleting_row
        if self.allow_filtering is not None:
            result["AllowFiltering"] = self.allow_filtering
        if self.allow_formatting_cell is not None:
            result["AllowFormattingCell"] = self.allow_formatting_cell
        if self.allow_formatting_column is not None:
            result["AllowFormattingColumn"] = self.allow_formatting_column
        if self.allow_formatting_row is not None:
            result["AllowFormattingRow"] = self.allow_formatting_row
        if self.allow_inserting_column is not None:
            result["AllowInsertingColumn"] = self.allow_inserting_column
        if self.allow_inserting_hyperlink is not None:
            result["AllowInsertingHyperlink"] = self.allow_inserting_hyperlink
        if self.allow_inserting_row is not None:
            result["AllowInsertingRow"] = self.allow_inserting_row
        if self.allow_selecting_locked_cell is not None:
            result["AllowSelectingLockedCell"] = self.allow_selecting_locked_cell
        if self.allow_selecting_unlocked_cell is not None:
            result["AllowSelectingUnlockedCell"] = self.allow_selecting_unlocked_cell
        if self.allow_sorting is not None:
            result["AllowSorting"] = self.allow_sorting
        if self.allow_using_pivot_table is not None:
            result["AllowUsingPivotTable"] = self.allow_using_pivot_table
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
