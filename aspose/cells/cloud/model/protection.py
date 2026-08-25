"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class Protection:
    """Represents the various types of protection options available for a worksheet."""
    allow_deleting_column: Optional[bool] = None
    allow_deleting_row: Optional[bool] = None
    allow_filtering: Optional[bool] = None
    allow_formatting_cell: Optional[bool] = None
    allow_formatting_column: Optional[bool] = None
    allow_formatting_row: Optional[bool] = None
    allow_inserting_column: Optional[bool] = None
    allow_inserting_hyperlink: Optional[bool] = None
    allow_inserting_row: Optional[bool] = None
    allow_sorting: Optional[bool] = None
    allow_using_pivot_table: Optional[bool] = None
    allow_editing_content: Optional[bool] = None
    allow_editing_object: Optional[bool] = None
    allow_editing_scenario: Optional[bool] = None
    password: Optional[str] = None
    allow_selecting_locked_cell: Optional[bool] = None
    allow_selecting_unlocked_cell: Optional[bool] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
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
        if self.allow_sorting is not None:
            result["AllowSorting"] = self.allow_sorting
        if self.allow_using_pivot_table is not None:
            result["AllowUsingPivotTable"] = self.allow_using_pivot_table
        if self.allow_editing_content is not None:
            result["AllowEditingContent"] = self.allow_editing_content
        if self.allow_editing_object is not None:
            result["AllowEditingObject"] = self.allow_editing_object
        if self.allow_editing_scenario is not None:
            result["AllowEditingScenario"] = self.allow_editing_scenario
        if self.password is not None:
            result["Password"] = self.password
        if self.allow_selecting_locked_cell is not None:
            result["AllowSelectingLockedCell"] = self.allow_selecting_locked_cell
        if self.allow_selecting_unlocked_cell is not None:
            result["AllowSelectingUnlockedCell"] = self.allow_selecting_unlocked_cell
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
