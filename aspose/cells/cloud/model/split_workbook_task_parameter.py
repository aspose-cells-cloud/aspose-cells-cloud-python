"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class SplitWorkbookTaskParameter:
    """Represents split workbook task parameter."""
    workbook: Optional[FileSource] = None
    destination_file_position: Optional[FileSource] = None
    data_source: Optional[DataSource] = None
    target_data_source: Optional[DataSource] = None
    destination_file_format: Optional[str] = None
    split_name_rule: Optional[str] = None
    vertical_resolution: Optional[int] = None
    horizontal_resolution: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.workbook is not None:
            result["Workbook"] = self.workbook.to_dict()
        if self.destination_file_position is not None:
            result["DestinationFilePosition"] = self.destination_file_position.to_dict()
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.target_data_source is not None:
            result["TargetDataSource"] = self.target_data_source.to_dict()
        if self.destination_file_format is not None:
            result["DestinationFileFormat"] = self.destination_file_format
        if self.split_name_rule is not None:
            result["SplitNameRule"] = self.split_name_rule
        if self.vertical_resolution is not None:
            result["VerticalResolution"] = self.vertical_resolution
        if self.horizontal_resolution is not None:
            result["HorizontalResolution"] = self.horizontal_resolution
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
