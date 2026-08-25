"""Data models for the Aspose.Cells Cloud SDK for Python."""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class ConvertWorksheetTaskParameter:
    """Represents convert worksheet task parameter."""
    data_source: Optional[DataSource] = None
    workbook: Optional[FileSource] = None
    sheet: Optional[str] = None
    target_data_source: Optional[DataSource] = None
    target: Optional[FileSource] = None
    format_: Optional[str] = None
    area: Optional[str] = None
    page_index: Optional[int] = None
    vertical_resolution: Optional[int] = None
    horizontal_resolution: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        if self.data_source is not None:
            result["DataSource"] = self.data_source.to_dict()
        if self.workbook is not None:
            result["Workbook"] = self.workbook.to_dict()
        if self.sheet is not None:
            result["Sheet"] = self.sheet
        if self.target_data_source is not None:
            result["TargetDataSource"] = self.target_data_source.to_dict()
        if self.target is not None:
            result["Target"] = self.target.to_dict()
        if self.format_ is not None:
            result["Format"] = self.format_
        if self.area is not None:
            result["Area"] = self.area
        if self.page_index is not None:
            result["PageIndex"] = self.page_index
        if self.vertical_resolution is not None:
            result["VerticalResolution"] = self.vertical_resolution
        if self.horizontal_resolution is not None:
            result["HorizontalResolution"] = self.horizontal_resolution
        return result

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)
