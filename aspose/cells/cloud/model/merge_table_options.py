"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class MergeTableOptions:
    """MergeTableOptions."""
    main_table: Optional[CombinationSourceData] = None
    secondary_table: Optional[CombinationSourceData] = None
    data_merge_type: Optional[str] = None
    overwrite_main_table: Optional[bool] = None
    sync_data_to_target_workbook: Optional[bool] = None
    merged_data_to_position: Optional[DataOutputLocation] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.main_table is not None:
            result["MainTable"] = self.main_table.to_dict()
        if self.secondary_table is not None:
            result["SecondaryTable"] = self.secondary_table.to_dict()
        if self.data_merge_type is not None:
            result["DataMergeType"] = self.data_merge_type
        if self.overwrite_main_table is not None:
            result["OverwriteMainTable"] = self.overwrite_main_table
        if self.sync_data_to_target_workbook is not None:
            result["SyncDataToTargetWorkbook"] = self.sync_data_to_target_workbook
        if self.merged_data_to_position is not None:
            result["MergedDataToPosition"] = self.merged_data_to_position.to_dict()
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
